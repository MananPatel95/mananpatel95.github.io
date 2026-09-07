#!/usr/bin/env python3
"""Snapshot delayed CME futures last prices into tools/data/futures-prices.json."""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "tools" / "data" / "futures-prices.json"

YAHOO_SYMBOLS = {
    "ES": "ES=F",
    "MES": "MES=F",
    "NQ": "NQ=F",
    "MNQ": "MNQ=F",
    "YM": "YM=F",
    "MYM": "MYM=F",
    "RTY": "RTY=F",
    "M2K": "M2K=F",
    "CL": "CL=F",
    "MCL": "MCL=F",
}

CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=5d"
USER_AGENT = "mananpatel.info-futures-calculator/1.0"


def load_existing() -> dict:
    if not OUTPUT.exists():
        return {}
    try:
        return json.loads(OUTPUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def fetch_chart(yahoo_symbol: str) -> dict:
    request = urllib.request.Request(
        CHART_URL.format(symbol=yahoo_symbol),
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))
    result = payload["chart"]["result"][0]
    meta = result["meta"]
    price = meta.get("regularMarketPrice")
    if price is None:
        raise ValueError(f"No regularMarketPrice for {yahoo_symbol}")
    previous_close = meta.get("chartPreviousClose")
    if previous_close is None:
        previous_close = meta.get("previousClose")
    closes = [
        close
        for close in (result.get("indicators", {}).get("quote", [{}])[0].get("close") or [])
        if close is not None
    ]
    if (previous_close in (None, price)) and len(closes) >= 2:
        previous_close = closes[-2]
    market_time = meta.get("regularMarketTime")
    as_of = (
        datetime.fromtimestamp(market_time, tz=timezone.utc).isoformat()
        if market_time
        else datetime.now(timezone.utc).isoformat()
    )
    change = None
    change_percent = None
    if previous_close not in (None, 0):
        change = round(price - previous_close, 6)
        change_percent = round((price - previous_close) / previous_close * 100, 4)
    return {
        "yahooSymbol": yahoo_symbol,
        "price": price,
        "previousClose": previous_close,
        "change": change,
        "changePercent": change_percent,
        "dayHigh": meta.get("regularMarketDayHigh"),
        "dayLow": meta.get("regularMarketDayLow"),
        "asOf": as_of,
        "exchange": meta.get("exchangeName") or meta.get("fullExchangeName"),
    }


def main() -> int:
    existing = load_existing()
    prices = dict(existing.get("prices") or {})
    errors = []

    for symbol, yahoo_symbol in YAHOO_SYMBOLS.items():
        try:
            prices[symbol] = fetch_chart(yahoo_symbol)
            print(f"{symbol:4} {yahoo_symbol:7} {prices[symbol]['price']}")
        except (urllib.error.URLError, urllib.error.HTTPError, KeyError, ValueError, TimeoutError) as exc:
            errors.append(f"{symbol} ({yahoo_symbol}): {exc}")
            print(f"{symbol:4} {yahoo_symbol:7} FAILED {exc}", file=sys.stderr)
        time.sleep(0.25)

    fetched = [symbol for symbol in YAHOO_SYMBOLS if symbol in prices and "price" in prices[symbol]]
    if not fetched:
        print("No prices fetched; leaving existing file unchanged.", file=sys.stderr)
        return 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    snapshot = {
        "updatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": "Yahoo Finance delayed quotes",
        "prices": {symbol: prices[symbol] for symbol in YAHOO_SYMBOLS if symbol in prices},
    }
    OUTPUT.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    if errors:
        print("Partial update; some symbols failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

// Saves checkboxes, notes and reading-list fields in this browser so the guide
// can be worked through over several days. Each field is keyed by page + data-key.
(function () {
    var page = document.body.getAttribute('data-guide');
    var store = {
        get: function (k) {
            try { return localStorage.getItem(page + ':' + k); } catch (e) { return null; }
        },
        set: function (k, v) {
            try { localStorage.setItem(page + ':' + k, v); } catch (e) {}
        }
    };

    var fields = document.querySelectorAll('input[type="checkbox"], textarea, input[type="text"]');
    fields.forEach(function (el, i) {
        var key = el.getAttribute('data-key') || el.type + '-' + i;
        var saved = store.get(key);
        if (el.type === 'checkbox') {
            el.checked = saved === '1';
            el.addEventListener('change', function () {
                store.set(key, el.checked ? '1' : '0');
                updateProgress();
            });
        } else {
            if (saved !== null) el.value = saved;
            el.addEventListener('input', function () { store.set(key, el.value); });
        }
    });

    function updateProgress() {
        var boxes = document.querySelectorAll('input[type="checkbox"]');
        var done = 0;
        boxes.forEach(function (b) { if (b.checked) done++; });
        var label = document.getElementById('progress-label');
        var bar = document.getElementById('progress-bar');
        if (label) label.textContent = done + ' of ' + boxes.length + ' done';
        if (bar) bar.style.width = (boxes.length ? (done / boxes.length) * 100 : 0) + '%';
    }
    updateProgress();
})();

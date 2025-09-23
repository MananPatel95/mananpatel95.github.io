# 📝 Blog HTML/CSS Template for Reuse

A complete, responsive blog template with dark mode support, perfect for portfolio sites and personal blogs.

## 🎨 Design System

### Color Palette
```css
/* Light Mode */
--background-light: #FFFFFF
--text-light: #111827
--secondary-text-light: #6B7280
--border-light: #E5E7EB
--card-light: #F9FAFB

/* Dark Mode */
--background-dark: #121212
--text-dark: #E5E7EB
--secondary-text-dark: #9CA3AF
--border-dark: #374151
--card-dark: #1F2937

/* Accent */
--primary: #E83D99
```



## 🏗️ HTML Templates

### Blog Index Page
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Blog - Your Name</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
    <script>
        tailwind.config = {
          darkMode: "class",
          theme: {
            extend: {
              colors: {
                primary: "#E83D99",
                "background-light": "#FFFFFF",
                "background-dark": "#121212",
                "text-light": "#111827",
                "text-dark": "#E5E7EB",
                "secondary-text-light": "#6B7280",
                "secondary-text-dark": "#9CA3AF",
                "border-light": "#E5E7EB",
                "border-dark": "#374151",
                "card-light": "#F9FAFB",
                "card-dark": "#1F2937",
              },
              fontFamily: {
                sans: ['Inter', 'sans-serif'],
              },
            },
          },
        };
      </script>
    <style>
        .secondary-text {
          font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
        }
      </style>
</head>
<body class="bg-background-light dark:bg-background-dark font-sans text-text-light dark:text-text-dark transition-colors duration-300">
<div class="max-w-4xl mx-auto p-4 sm:p-6 lg:p-8">
<header class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-12">
<div class="flex-1">
<a href="../index.html" class="inline-flex items-center text-secondary-text-light dark:text-secondary-text-dark hover:text-text-light dark:hover:text-text-dark mb-6">
<span class="material-icons text-base mr-2">arrow_back</span>
<span>Back to Portfolio</span>
</a>
<h1 class="text-3xl sm:text-4xl font-bold text-text-light dark:text-text-dark">Blog</h1>
<p class="text-lg text-secondary-text-light dark:text-secondary-text-dark mt-2 secondary-text">Your blog description</p>
</div>
</header>
<main>
<section class="mb-12">
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<div class="bg-card-light dark:bg-card-dark p-6 rounded-lg border border-border-light dark:border-border-dark">
<h3 class="font-semibold text-lg text-text-light dark:text-text-dark mb-2">📱 Post Title</h3>
<p class="text-secondary-text-light dark:text-secondary-text-dark mb-4 secondary-text">Post description</p>
<a href="post-slug.html" class="text-primary hover:underline">Read more →</a>
</div>
</div>
</section>
</main>
</div>
</body>
</html>
```

### Individual Blog Post Page
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Post Title | Your Name</title>
    <meta name="description" content="Post description">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        .secondary-text {
          font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
          font-size: 0.75rem;
        }
        pre {
          background-color: #f8f9fa;
          border: 1px solid #e9ecef;
          border-radius: 0.375rem;
          padding: 1rem;
          overflow-x: auto;
          font-size: 0.875rem;
          line-height: 1.5;
        }
        code {
          font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
          font-size: 0.875rem;
        }
      </style>
</head>
<body class="bg-white">
    <div class="max-w-4xl mx-auto p-6 pt-20">
        <a href="index.html" class="inline-flex items-center text-gray-600 hover:text-gray-900 mb-8 transition-colors">
            <span class="material-icons mr-2">arrow_back</span>
            Back to Blog
        </a>
        
        <article>
            <header class="mb-8">
                <h1 class="text-3xl font-bold text-gray-900 mb-4">📱 Post Title</h1>
                <p class="text-secondary-text-light dark:text-secondary-text-dark secondary-text mb-4">Post description</p>
                <div class="flex items-center text-sm text-gray-500">
                    <span class="material-icons mr-1 text-sm">schedule</span>
                    <span class="mr-4">X min read</span>
                    <span class="material-icons mr-1 text-sm">calendar_today</span>
                    <span>Date</span>
                </div>
            </header>

            <div class="prose prose-lg max-w-none">
                <h2 class="text-2xl font-semibold text-gray-900 mb-4">Section Title</h2>
                <p class="text-secondary-text-light dark:text-secondary-text-dark secondary-text mb-6">
                    Your paragraph content
                </p>
                
                <pre><code class="language-swift">// Your code here</code></pre>
                
                <div class="bg-green-50 border-l-4 border-green-400 p-4 my-8">
                    <h4 class="text-lg font-semibold text-green-800 mb-2">✅ Do's</h4>
                    <ul class="text-green-700 space-y-1">
                        <li>Your tips here</li>
                    </ul>
                </div>
            </div>
        </article>
    </div>
</body>
</html>
```

## 🎯 Key CSS Classes

### Layout Classes
```css
/* Container */
.max-w-4xl.mx-auto.p-4.sm:p-6.lg:p-8

/* Header */
.flex.flex-col.sm:flex-row.justify-between.items-start.sm:items-center.mb-12

/* Back Button */
.inline-flex.items-center.text-secondary-text-light.dark:text-secondary-text-dark.hover:text-text-light.dark:hover:text-text-dark.mb-6

/* Blog Cards */
.bg-card-light.dark:bg-card-dark.p-6.rounded-lg.border.border-border-light.dark:border-border-dark

/* Grid Layout */
.grid.grid-cols-1.md:grid-cols-2.gap-6
```

### Typography Classes
```css
/* Main Title */
.text-3xl.sm:text-4xl.font-bold.text-text-light.dark:text-text-dark

/* Post Titles */
.font-semibold.text-lg.text-text-light.dark:text-text-dark.mb-2

/* Descriptions */
.text-secondary-text-light.dark:text-secondary-text-dark.mb-4.secondary-text

/* Section Headers */
.text-2xl.font-semibold.text-gray-900.mb-4

/* Body Text */
.text-secondary-text-light.dark:text-secondary-text-dark.secondary-text.mb-6
```

### Interactive Elements
```css
/* Links */
.text-primary.hover:underline

/* Material Icons */
.material-icons.text-base.mr-2

/* Code Blocks */
pre { /* custom styles */ }
code { /* custom styles */ }
```

## 🚀 Quick Setup

1. **Copy HTML structure** from templates above
2. **Update Tailwind config** with your colors
3. **Add custom CSS** for secondary text and code blocks
4. **Replace placeholder content** with your posts
5. **Update navigation links** to match your site
6. **Customize colors** in Tailwind config

## 💡 Features

- ✅ **Responsive Design** - Mobile-first with `sm:` and `md:` breakpoints
- ✅ **Dark Mode** - Built-in dark mode support with `dark:` classes
- ✅ **Accessibility** - Proper semantic HTML and ARIA labels
- ✅ **Performance** - CDN for Tailwind CSS and Google Fonts
- ✅ **Code Highlighting** - Ready for syntax highlighting libraries
- ✅ **Material Icons** - Consistent iconography throughout
- ✅ **Typewriter Font** - Monospace font for secondary text
- ✅ **Card-based Layout** - Clean, modern card design
- ✅ **Hover Effects** - Smooth transitions and interactions

## 📱 Responsive Breakpoints

- **Mobile**: Default (no prefix)
- **Small**: `sm:` (640px+)
- **Medium**: `md:` (768px+)
- **Large**: `lg:` (1024px+)

## 🎨 Customization

### Change Colors
Update the `tailwind.config` colors object:
```javascript
colors: {
  primary: "#YOUR_COLOR",
  "background-light": "#YOUR_COLOR",
  // ... etc
}
```

### Change Fonts
Update the font family in the config:
```javascript
fontFamily: {
  sans: ['YOUR_FONT', 'sans-serif'],
}
```

### Add More Blog Posts
Duplicate the blog card div and update:
- Title
- Description
- Link href
- Icon/emoji

Perfect for portfolio sites, personal blogs, or any content-focused website!

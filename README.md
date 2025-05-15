# Latest Online Tools

This is a website that provides a collection of free online tools.

## Clean URLs

This site uses clean URLs (without .html extensions) for better SEO and user experience.

### How it works on GitHub Pages

This site uses a directory-based approach for clean URLs on GitHub Pages:

1. Instead of using `popular-tools.html`, we create a `popular-tools/index.html` file
2. Instead of using `all-tools.html`, we create a `all-tools/index.html` file

With this approach:
- When someone visits `/popular-tools/`, the server automatically serves the `popular-tools/index.html` file
- When someone visits `/all-tools/`, the server automatically serves the `all-tools/index.html` file

This works on both GitHub Pages and local development servers without any special configuration.

### Configuration

We also include a `_config.yml` file with the following settings:

```yaml
permalink: pretty
defaults:
  - scope:
      path: ""
    values:
      layout: default
  - scope:
      path: "all-tools"
    values:
      permalink: /all-tools/
  - scope:
      path: "popular-tools"
    values:
      permalink: /popular-tools/
```

This ensures that GitHub Pages correctly handles the URLs and provides a fallback for any edge cases.

### 404 Page

A custom 404 page (`404.html`) is included to handle any missing pages. GitHub Pages automatically uses this file when a page is not found.

## Deployment

To deploy this site to GitHub Pages:

1. Push the code to a GitHub repository
2. Go to the repository settings
3. Under "GitHub Pages", select the branch you want to deploy (usually `main` or `master`)
4. The site will be available at `https://yourusername.github.io/repository-name/`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
# Latest Online Tools

This is a website that provides a collection of free online tools.

## Clean URLs

This site uses clean URLs (without .html extensions) for better SEO and user experience.

### How it works on GitHub Pages

GitHub Pages automatically handles clean URLs when you add the following to your `_config.yml` file:

```yaml
permalink: pretty
```

With this configuration:
- When someone visits `/popular-tools`, GitHub Pages will serve the `popular-tools.html` file
- When someone visits `/all-tools`, GitHub Pages will serve the `all-tools.html` file

This works automatically without needing .htaccess rules, which GitHub Pages doesn't process.

### Local Development

When developing locally with a simple HTTP server (like Python's http.server), you'll need to access the HTML files directly with their .html extension:

- http://localhost:8080/index.html
- http://localhost:8080/popular-tools.html
- http://localhost:8080/all-tools.html

But when deployed to GitHub Pages, the clean URLs will work correctly.

## Deployment

To deploy this site to GitHub Pages:

1. Push the code to a GitHub repository
2. Go to the repository settings
3. Under "GitHub Pages", select the branch you want to deploy (usually `main` or `master`)
4. The site will be available at `https://yourusername.github.io/repository-name/`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
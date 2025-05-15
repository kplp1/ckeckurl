import http.server
import socketserver
import os
import re
from urllib.parse import urlparse

PORT = 8080

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        
        # Handle root path
        if path == "/":
            return super().do_GET()
        
        # Handle clean URLs (without .html extension)
        if not path.endswith('.html') and not path.endswith('/') and '.' not in os.path.basename(path):
            # Check if a corresponding HTML file exists
            html_path = path + '.html'
            if os.path.exists('.' + html_path):
                self.path = html_path
                return super().do_GET()
            
            # Check if a directory with index.html exists
            dir_path = path
            if os.path.exists('.' + dir_path) and os.path.isdir('.' + dir_path):
                index_path = os.path.join(dir_path, 'index.html')
                if os.path.exists('.' + index_path):
                    self.path = index_path
                    return super().do_GET()
        
        # Default behavior for all other paths
        return super().do_GET()

# Create the server
Handler = CleanURLHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at http://localhost:{PORT}")
print("Clean URLs are enabled - you can access pages without .html extension")
httpd.serve_forever()

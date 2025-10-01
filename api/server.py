from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from data_handler import DataHandler
from auth import check_auth

# Initialize transaction store
data_handler = DataHandler()

class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def _authenticate(self):
        if not check_auth(self.headers.get("Authorization")):
            self._set_headers(401)
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
            return False
        return True

    def do_GET(self):
        if not self._authenticate():
            return

        parsed = urlparse(self.path)
        path_parts = parsed.path.strip("/").split("/")

        if len(path_parts) == 1 and path_parts[0] == "transactions":
            self._set_headers(200)
            self.wfile.write(json.dumps(data_handler.get_all()).encode())

        elif len(path_parts) == 2 and path_parts[0] == "transactions":
            tid = path_parts[1]
            transaction = data_handler.get_one(tid)
            if transaction:
                self._set_headers(200)
                self.wfile.write(json.dumps(transaction).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Not Found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_POST(self):
        if not self._authenticate():
            return

        if self.path == "/transactions":
            length = int(self.headers["Content-Length"])
            body = json.loads(self.rfile.read(length))
            new_tx = data_handler.add(body)
            self._set_headers(201)
            self.wfile.write(json.dumps(new_tx).encode())

    def do_PUT(self):
        if not self._authenticate():
            return

        path_parts = self.path.strip("/").split("/")
        if len(path_parts) == 2 and path_parts[0] == "transactions":
            tid = path_parts[1]
            length = int(self.headers["Content-Length"])
            body = json.loads(self.rfile.read(length))
            updated = data_handler.update(tid, body)
            if updated:
                self._set_headers(200)
                self.wfile.write(json.dumps(updated).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    def do_DELETE(self):
        if not self._authenticate():
            return

        path_parts = self.path.strip("/").split("/")
        if len(path_parts) == 2 and path_parts[0] == "transactions":
            tid = path_parts[1]
            deleted = data_handler.delete(tid)
            if deleted:
                self._set_headers(200)
                self.wfile.write(json.dumps({"message": "Deleted"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Not Found"}).encode())


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
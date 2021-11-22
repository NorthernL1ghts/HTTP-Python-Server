# Python 3 HTTP Server Example

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "10.1.181.163"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "UTF-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "UTF-8"))
        self.wfile.write(bytes("<body>", "UTF-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "UTF-8"))
        self.wfile.write(bytes("</body></html>", "UTF-8"))

if __name__ == "__main__":
    webserver = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass 
    
    webserver.server_close()
    print("server stopped.")

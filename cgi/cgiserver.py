from http.server import CGIHTTPRequestHandler, HTTPServer

server = HTTPServer(('', 8080), CGIHTTPRequestHandler)
server.serve_forever()

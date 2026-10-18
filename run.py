import http.server, socketserver, webbrowser, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8000
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as s:
    print(f"Open http://localhost:{PORT}  (Ctrl+C to stop)")
    webbrowser.open(f"http://localhost:{PORT}")
    s.serve_forever()

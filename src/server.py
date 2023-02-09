from http.server import BaseHTTPRequestHandler, HTTPServer
import server_funcs

hostName = "localhost"
serverPort = 8011

class Server(BaseHTTPRequestHandler):
  
    def do_GET(self):
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
      self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
      self.wfile.write(bytes("<body>", "utf-8"))
      self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
      self.wfile.write(bytes("</body></html>", "utf-8"))
      #print out output info for given commit or list of commits if in top directory
        #ie change above code to print out file <standard name for info file>, assuming every directory will have a file by that name
            #(or similar name: info_*)

    
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_byte_data = self.rfile.read(content_len)
        body_data = server_funcs.parse_post_data(post_byte_data)
        temp_path = server_funcs.create_temp_path()

        self.send_response(200)
        server_funcs.build(body_data, temp_path)
        #check if build suceeded - yes, continue with test, else skip to save results
        server_funcs.test()
        server_funcs.save_results()
        server_funcs.restore()


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

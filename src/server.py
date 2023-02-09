from http.server import BaseHTTPRequestHandler, HTTPServer
import server_funcs

hostName = "localhost"
serverPort = 8011

class Server(BaseHTTPRequestHandler):
    """
    A simple server with a do_GET method and a do_POST method. 
    The server is a continuous integration server that can be connected to different github webhooks 
    to perform automatic tests on newly pushed changes.
    """

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
        """
        Handles incoming http POST requests. 
        Parses it, builds + tests corresponding repository and saves the result.
        """
        content_len = int(self.headers.get('Content-Length'))
        post_byte_data = self.rfile.read(content_len)
        body_data = server_funcs.parse_post_data(post_byte_data)
        temp_path = server_funcs.create_temp_path()

        self.send_response(200)
        build_res = server_funcs.build(body_data, temp_path)
        #check if build suceeded - yes, continue with test, else skip to save results
        test_res = server_funcs.test()
        out = server_funcs.save_results(body_data, build_res, test_res, temp_path)
        print(out) # Out should be input for notify()
        server_funcs.restore()


# Starts up the server on selected port
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

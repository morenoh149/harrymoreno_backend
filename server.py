#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, read, sep
from postgres import Postgres
import cgi

PORT_NUMBER = 8080
db = Postgres("postgres://jrandom@localhost/blog")
db.run("CREATE TABLE foo (bar text, baz int)")

#This class will handle any incoming request from the browser
class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path=="/":
            self.path="/index_example3.html"
        try:
            #Check the file extension required and set the right mime type
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir + sep + self.path, 'rb')
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        if self.path=="/newsletter_signup":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    'REQUEST_METHOD': 'POST',
                    'CONTENT_TYPE': self.headers['Content-Type'],
                }
            )
            self.send_response(200)
            self.end_headers()
            submitted_email = form["email"].value
            db.run("insert into emails values ('%(email)'", {"email": submitted_email})
            self.wfile.write(str.encode("Thanks for signing up %s !\n" % submitted_email))
            return

try:
    #Create a web server and define the handler to manage the incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ', PORT_NUMBER)

    #Wait forever for incoming http rewquests
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()

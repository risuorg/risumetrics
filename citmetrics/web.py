#!/usr/bin/env python
# encoding: utf-8
# Copyright (C)  2018 Pablo Iranzo Gómez <Pablo.Iranzo@gmail.com>

import datetime
import json
import os
import random
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        """
        Sets headers and Return Code
        :return:
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """
        Processes GET requests
        """
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        """
        Sets headers on requests
        """
        self._set_headers()

    def do_POST(self):
        """
        Processes POST requests
        """
        content_length = int(self.headers['Content-Length'])  # <--- data size
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        filename = "%s-%s.json" % (datetime.datetime.now().strftime("%Y%m%d-%H%M%S"), random.random())
        print("Incoming file: %s" % filename)
        try:
            with open(filename, 'w') as fd:
                json.dump(json.loads(post_data.decode('utf-8')), fd, indent=2)
        except:
            os.remove(filename)
            with open("%s.txt" % filename, 'w') as fd:
                fd.write(post_data.decode('utf-8'))

        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


def run(server_class=HTTPServer, handler_class=S, port=80):
    """
    Main code loop for the http server that stores the files received via http POST
    :param server_class:
    :param handler_class:
    :param port:
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

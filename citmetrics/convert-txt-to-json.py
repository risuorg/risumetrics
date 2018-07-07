#!/usr/bin/env python
# encoding: utf-8
# Copyright (C)  2018 Pablo Iranzo Gómez <Pablo.Iranzo@gmail.com>

import datetime
import json
import os
import random
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer



def main():
    files = []
    folders = [os.path.dirname(__file__)]# Walk the folders and subfolders for files based on our criteria
    for folder in folders:
        for items in os.walk(folder, followlinks=True):
            root = items[0]
            filenames = items[2]

            for filename in filenames:
                filepath = os.path.join(root, filename)
                passesextension = False
                if os.path.splitext(filepath)[1] == '.txt':
                    files.append(filepath)

    for filename in files:
        contents = open(filename,'r').read()
        newcontents = "\n".join(contents.split("\n")[3:-2])

        # Remove the .txt ending
        newfilename = "%s" % os.path.splitext(filename)[0]

        try:
            with open(newfilename, 'w') as fd:
                json.dump(json.loads(newcontents, fd, indent=2))
        except:
            os.remove(newfilename)
            print("Failed to convert file: %s" % filename)




if __name__ == "__main__":
    from sys import argv

    main()

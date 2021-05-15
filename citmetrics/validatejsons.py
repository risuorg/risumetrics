#!/usr/bin/env python
# encoding: utf-8
# Copyright (C)  2018 Pablo Iranzo Gómez <Pablo.Iranzo@gmail.com>
#
# Description: validate jsons as valid for risu or remove in case of corruption

import json
import os


def main():
    files = []
    folders = [os.getcwd()]  # Walk the folders and subfolders for files based on our criteria
    for folder in folders:
        for items in os.walk(folder, followlinks=True):
            root = items[0]
            filenames = items[2]

            for filename in filenames:
                filepath = os.path.join(root, filename)
                if os.path.splitext(filepath)[1] == '.json' and 'risu' in filename:
                    files.append(filepath)

    for filename in files:
        print("Processing file: %s" % filename)
        try:
            json.load(open(filename, 'r'))
        except:
            print("Processing failed, removing file")
            os.remove(filename)


if __name__ == "__main__":
    main()

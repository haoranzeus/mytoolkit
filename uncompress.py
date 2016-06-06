#!/usr/bin/python3

import os
import sys

def usage():
    print("usage:")
    print("\tuncompress.py <pathname>")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit()

    rootdir = sys.argv[1]
    files = [];
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            files += [filename];

    for tarfile in files:
        os.system("tar -zxvf " + tarfile)


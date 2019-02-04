#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

"""Startup Script with Command Line parsing."""

import sys
import getopt
# load the service entry point
# from service import runDebug as run
from service import run

def main(argv):
    """Main entry point of our rest service."""
    debug = False
    port = 5000
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["debug=", "port="])
    except getopt.GetoptError:
        print ('main.py -debug true|false -port 5000')
        # sys.exit(2)
    for opt, arg in opts:
        if (opt == '-h' or opt == '--help'):
            print ('-d <debugmode> -p <port>')
            sys.exit()
        elif opt in ("-d", "--debug"):
            debug = True
        elif opt in ("-p", "--port"):
            port = arg
    run()
if __name__ == "__main__":
    main(sys.argv[1:])
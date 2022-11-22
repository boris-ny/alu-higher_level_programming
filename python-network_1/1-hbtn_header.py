#!/usr/bin/python3
'''X-Request-Id variable in header.'''
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header['X-Request-Id'])

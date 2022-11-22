#!/usr/bin/python3
'''Module 3-error_code.py'''
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

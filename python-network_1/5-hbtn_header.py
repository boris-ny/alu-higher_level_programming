#!/usr/bin/python3
'''Module 5-hbtn_header.py'''
import requests
import sys
if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    print(html.headers.get('X-Request-Id'))

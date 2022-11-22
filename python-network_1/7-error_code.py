#!/usr/bin/python3
'''Module 7-error_code.py'''
import requests
import sys
if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    if html.status_code >= 400:
        print("Error code: {}".format(html.status_code))
    else:
        print(html.text)

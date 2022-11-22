#!/usr/bin/python3
'''Module 4-hbtn_status.py'''
import requests
if __name__ == "__main__":
    html = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))

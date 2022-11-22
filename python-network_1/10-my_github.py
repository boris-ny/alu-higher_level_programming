#!/usr/bin/python3
'''Module 10-my_github.py'''
import requests
import sys
if __name__ == "__main__":
    url = 'https://api.github.com/user'
    html = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(html.json().get('id'))

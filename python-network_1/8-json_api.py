#!/usr/bin/python3
'''Module 8-json_api.py'''
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        r = ""
    else:
        r = sys.argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': r})
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

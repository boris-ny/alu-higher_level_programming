#!/usr/bin/python3
""" Github API """
import requests
import sys
if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                             sys.argv[1])
    response = requests.get(url)
    try:
        json = response.json()
        for i in range(10):
            print("{}: {}".format(json[i].get('sha'),
                                  json[i].get('commit').get('author').get('name')))
    except:
        pass

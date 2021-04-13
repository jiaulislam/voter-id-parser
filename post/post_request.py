import requests
import sys

"""
module_name: post_reqeust.py

This module will help to post data as a json object and
will print json post status code as return
"""

def post_data(url, json_value):
    try:
        request = requests.post(url, json=json_value)
    except Exception as e:
        sys.exit(e)
    else:
        return f"STATUS<{request.status_code}>"
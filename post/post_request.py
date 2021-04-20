import requests

"""
module_name: post_request.py

This module will help to post data as a json object and
will print json post status code as return
"""


def post_data(url, json_value):
    """
    Post the data to shared URL/API with provided JSON data.

    return STATUS_CODE<201> if success else exception with STATUS_CODE
    """
    try:
        request = requests.post(url, json=json_value)
    except Exception as e:
        print(e)
    else:
        return f"STATUS<{request.status_code}>"

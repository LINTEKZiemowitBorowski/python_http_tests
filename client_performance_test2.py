#!/usr/bin/python

import urllib
import httplib2
import json
import time

base_uri = "http://localhost:8080"
headers = {"Connection": "keep-alive"}
json_headers = {"Connection": "keep-alive", "Content-type": "application/json"}
start_time = time.time()

http = httplib2.Http()
for i in range(0, 200):
    response, content = http.request(
        base_uri,
        "GET",
        headers=headers)

    data = {"A": 1, "B": 2}
    url_values = urllib.urlencode(data)
    response, content = http.request(
        base_uri + "/sum?" + url_values,
        "GET",
        headers=headers)

    data = {"A": 2, "B": 3}
    values = urllib.urlencode(data)
    response, content = http.request(
        base_uri + "/multiple",
        "POST",
        headers=headers,
        body=values)

    response, content = http.request(
        base_uri + "/jsonresponse",
        "GET",
        headers=headers)

    data = {"A": 5, "B": 6, "C": "3"}
    values = json.dumps(data)
    response, content = http.request(
        base_uri + "/jsonrequest",
        "POST",
        headers=json_headers,
        body=values)

    data = {"data": {"A": "A", "B": {"C": ["D", "E"], "F": ["G", "H"]}}}
    values = json.dumps(data)
    response, content = http.request(
        base_uri + "/jsonrequestcomplexdata",
        "POST",
        headers=json_headers,
        body=values)

stop_time = time.time()
print "Done, execution time: %f" % (stop_time - start_time)


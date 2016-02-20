#!/usr/bin/python

import urllib
import httplib2
import json

base_uri = "http://localhost:10000"
headers = {"Connection": "keep-alive"}
json_headers = {"Connection": "keep-alive", "Content-type": "application/json"}

http = httplib2.Http()

response, content = http.request(base_uri, headers=headers)
print response
print content

data = {"A": 1, "B": 2}
url_values = urllib.urlencode(data)
response, content = http.request(base_uri + "/sum?" + url_values, headers=headers)
print response
print content

data = {"A": 2, "B": 3}
values = urllib.urlencode(data)
response, content = http.request(base_uri + "/multiple", "POST", headers=headers, body=values)
print response
print content

response, content = http.request(base_uri + "/jsonresponse", headers=headers)
print response
print content

data = {"A": 5, "B": 6, "C": "3"}
values = json.dumps(data)
response, content = http.request(base_uri + "/jsonrequest", "POST", headers=json_headers, body=values)
print response
print content

data = {"data": {"A": "A", "B": {"C": ["D", "E"], "F": ["G", "H"]}}}
values = json.dumps(data)
response, content = http.request(base_uri + "/jsonrequestcomplexdata", "POST", headers=json_headers, body=values)
print response
print content
print "Done"

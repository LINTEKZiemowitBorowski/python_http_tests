#!/usr/bin/python

import requests
import json

base_uri = "http://localhost:8080"

print "Test 1"

response = requests.get(url=base_uri)
resp_read = response.text
print "Response class: %s" % resp_read.__class__
print resp_read + "\n"

print "Test 2, sum"

data = {"A": 1, "B": 2}
response = requests.get(url=base_uri + "/sum?", params=data)
resp_read = response.text
print "Response class: %s" % resp_read.__class__
print resp_read + "\n"

print "Test3, multiple"

data = {"A": 2, "B": 3}
req = requests.post(url=base_uri + "/multiple", params=data)
resp_read = response.text
print "Response class: %s" % resp_read.__class__
print resp_read + "\n"

print "Test4, JSON response"

response = requests.get(url=base_uri + "/jsonresponse")
resp_read = response.json()
print "Response class: %s" % resp_read.__class__
print ("%s\n" % resp_read)

print "Test5, JSON request"

data = {"A": 5, "B": 6, "C": "3"}
data_json = json.dumps(data)
response = requests.post(url=base_uri + "/jsonrequest", data=data_json,
                         headers={'content-type': 'application/json'})
resp_read = response.text
print "Response class: %s" % resp_read.__class__
print resp_read + "\n"

print "Test6, JSON request with complex data"

data = {"data": {"A": "A", "B": {"C": ["D", "E"], "F": ["G", "H"]}}}
data_json = json.dumps(data)
response = requests.post(url=base_uri + "/jsonrequestcomplexdata", data=data_json,
                         headers={'content-type': 'application/json'})
print "Data sent: %s" % str(data["data"])
print "Data received: %s\n" % response.json()

print "Done"

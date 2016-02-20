#!/usr/bin/python

import urllib
import urllib2
import json

base_uri = "http://localhost:10000"

print "Test 1"

req = urllib2.Request(url=base_uri)
response = urllib2.urlopen(req)
print response.read()

print "Test 2, sum"

data = {"A": 1, "B": 2}
url_values = urllib.urlencode(data)
req = urllib2.Request(url=base_uri + "/sum?" + url_values)
response = urllib2.urlopen(req)
print response.read()

print "Test3, multiple"

data = {"A": 2, "B": 3}
values = urllib.urlencode(data)
req = urllib2.Request(url=base_uri + "/multiple", data=values)
response = urllib2.urlopen(req)
print response.read()

print "Test4, JSON response"

req = urllib2.Request(url=base_uri + "/jsonresponse")
response = urllib2.urlopen(req)
print response.read()

print "Test5, JSON request"

data = {"A": 5, "B": 6, "C": "3"}
data_json = json.dumps(data)
req = urllib2.Request(
    url=base_uri + "/jsonrequest",
    data=data_json,
    headers={'content-type': 'application/json'})
response = urllib2.urlopen(req)
print response.read()

print "Test6, JSON request with complex data"

data = {"data": {"A": "A", "B": {"C": ["D", "E"], "F": ["G", "H"]}}}
data_json = json.dumps(data)
req = urllib2.Request(
    url=base_uri + "/jsonrequestcomplexdata",
    data=data_json,
    headers={'content-type': 'application/json'})
response = urllib2.urlopen(req)
print "Data sent: %s" % str(data["data"])
content = response.read()
received = json.loads(content)
print "Data received: %s" % str(received)

print "Done"

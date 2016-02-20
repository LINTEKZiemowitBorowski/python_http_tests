#!/usr/bin/python

import urllib
import urllib2
import json
import time

base_uri = "http://localhost:10000"
start_time = time.time()

for i in range(0, 200):
    req = urllib2.Request(url=base_uri)
    response = urllib2.urlopen(req)

    data = {"A": 1, "B": 2}
    url_values = urllib.urlencode(data)
    req = urllib2.Request(url=base_uri + "/sum?" + url_values)
    response = urllib2.urlopen(req)

    data = {"A": 2, "B": 3}
    values = urllib.urlencode(data)
    req = urllib2.Request(url=base_uri + "/multiple", data=values)
    response = urllib2.urlopen(req)

    req = urllib2.Request(url=base_uri + "/jsonresponse")
    response = urllib2.urlopen(req)

    data = {"A": 5, "B": 6, "C": "3"}
    data_json = json.dumps(data)
    req = urllib2.Request(
        url=base_uri + "/jsonrequest", data=data_json, headers={'content-type': 'application/json'})
    response = urllib2.urlopen(req)

    data = {"data": {"A": "A", "B": {"C": ["D", "E"], "F": ["G", "H"]}}}
    data_json = json.dumps(data)
    req = urllib2.Request(
        url=base_uri + "/jsonrequestcomplexdata", data=data_json, headers={'content-type': 'application/json'})
    response = urllib2.urlopen(req)

stop_time = time.time()
print "Done, execution time: %f" % (stop_time - start_time)


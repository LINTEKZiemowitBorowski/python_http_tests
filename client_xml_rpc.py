#!/usr/bin/python

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:8080', verbose=False)

print "Test 1"
print server.hello_world()

print "Test 2, sum"
params = {"A": 1, "B": 2}
print server.sum(params)

print "Test3, multiple"
params = {"A": 2, "B": 3}
print server.multiple(params)

print "Test4, JSON response"
print server.json_response()

print "Test5, request"
params = {"A": 5, "B": 6, "C": "3"}
print server.request(params)

print "Test6, request with complex data"
params = {"data": {"A": "A", "B": {"C": ["D", "E"], "F": ["G", "H"]}}}
print "Params sent: %s" % str(params["data"])
print "Params received: %s" % server.complex_request(params)

print "Done"


#!/usr/bin/python

import SimpleXMLRPCServer

def hello_world():
    return "Hello world !"


def sum(params):
    result = "Sum: No parameters found."
    try:
        a = int(params['A'])
        b = int(params['B'])
        result = "Result: %d" %(a + b)
    except Exception, e:
        result = ("Sum error: %s" %str(e))
    return result


def multiple(params):
    result = "Multiple: No parameters found."
    try:
        a = int(params['A'])
        b = int(params['B'])
        result = "Result: %d" %(a * b)
    except Exception, e:
        result = ("Multiple error: %s" %str(e))
    return result


def json_response():
    structure = {"A": "A", "B":{"C":["D","E"], "F":["G", "H"]}}
    return structure


def request(params):
    result = "Request: No parameters found."
    try:
        a = params['A']
        b = params['B']
        c = int(params['C'])
        d = a + b + c
        result = "Result, value A: %d value B: %d, value C: %d, sum: %d" %(a, b, c, d)
    except Exception, e:
        result = ("Request error: %s" %str(e))
    return result


def complex_request(params):
    result = "Complex request data: No parameters found."
    try:
        data = params['data']
        result = str(data)
    except Exception, e:
        result = ("JSON request complex data error: %s" %str(e))
    return result

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8080))
server.register_function(hello_world)
server.register_function(sum)
server.register_function(multiple)
server.register_function(json_response)
server.register_function(request)
server.register_function(complex_request)
server.serve_forever()

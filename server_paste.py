#!/usr/bin/python

import bottle


@bottle.get('/')
def hello_world():
    return "Hello world !"


@bottle.get('/sum')
def sum():
    result = "Sum: No parameters found."
    try:
        a = int (bottle.request.query.A)
        b = int (bottle.request.query.B)
        result = "Result: %d" %(a + b)
    except Exception, e:
        result = ("Sum error: %s" %str(e))
    return result


@bottle.post('/multiple')
def multiple():
    result = "Multiple: No parameters found."
    try:
        a = int (bottle.request.forms.A)
        b = int (bottle.request.forms.B)
        result = "Result: %d" %(a * b)
    except Exception, e:
        result = ("Multiple error: %s" %str(e))
    return result


@bottle.get('/jsonresponse')
def jsonresponse():
    structure = {"A": "A", "B":{"C":["D","E"], "F":["G", "H"]}}
    return structure


@bottle.post('/jsonrequest')
def jsonrequest():
    result = "JSON request: No parameters found."
    try:
        a = bottle.request.json['A']
        b = bottle.request.json['B']
        c = int (bottle.request.json['C'])
        d = a + b + c
        result = "Result, value A: %d value B: %d, value C: %d, sum: %d" %(a, b, c, d)
    except Exception, e:
        result = ("JSON request error: %s" %str(e))
    return result


@bottle.post('/jsonrequestcomplexdata')
def jsonrequestcomplexdata():
    result = "JSON request complex data: No parameters found."
    try:
        data = bottle.request.json['data']
        result = data
    except Exception, e:
        result = ("JSON request complex data error: %s" %str(e))
    return result



bottle.debug(False)
bottle.run(server='paste', host='localhost', port=8080)

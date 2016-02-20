#!/usr/bin/python

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world !"


@app.route('/sum')
def sum_numbers():
    try:
        a = int(request.args.get("A"))
        b = int(request.args.get("B"))
        result = "Result: %d" % (a + b)
    except Exception, e:
        result = ("Sum error: %s" % str(e))
    return result


@app.route('/multiple', methods=["POST"])
def multiple():
    try:
        a = int(request.form["A"])
        b = int(request.form["B"])
        result = "Result: %d" % (a * b)
    except Exception, e:
        result = ("Multiple error: %s" % str(e))
    return result


@app.route('/jsonresponse')
def json_response():
    structure = {"A": "A", "B": {"C": ["D", "E"], "F": ["G", "H"]}}
    return jsonify(**structure)


@app.route('/jsonrequest', methods=["POST"])
def json_request():
    try:
        a = request.json['A']
        b = request.json['B']
        c = int(request.json['C'])
        d = a + b + c
        result = "Result, value A: %d value B: %d, value C: %d, sum: %d" % (a, b, c, d)
    except Exception, e:
        result = ("JSON request error: %s" % str(e))
    return result


@app.route('/jsonrequestcomplexdata', methods=["POST"])
def json_request_complex_data():
    try:
        data = request.json['data']
        return jsonify(**data)
    except Exception, e:
        return ("JSON request complex data error: %s" % str(e))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

data = {}

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    print('Action:' + req.get("result").get("action"))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    print(r)
    return r


def processRequest(req):
    if req.get("result").get("action") != 'jam.location.get':
        return {}

    print(req.get("result").get("parameters"))
    #location = req.get("result").get("parameters").get("Location")
    #location = []

    #data.setdefault('locations', []).append(location)

    res = makeWebhookResult(data)
    return res


def makeWebhookResult(data):
#    return data
    #locations = ''.join(data['locations'])
    print("Response:")

    return {
        "speech": "response",
        "displayText": "response",
        # "data": data,
        "contextOut": [{"name":"sendinvoicebyemail","lifespan":0},{"name":"prompt","lifespan":5}],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')

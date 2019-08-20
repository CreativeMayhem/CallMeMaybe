#!/usr/bin/python


import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.web
import plivo
import ssl
import os
import re
import time
from tornado_http_auth import DigestAuthMixin, BasicAuthMixin, auth_required


#User Variable Section

#The script won't run if you don't uncomment the credential line. This is to remind you to CHANGE THE PASSWORD.
#credentials = {'cmm': 'Cleh5Y6D&86?E4sUQ9Lq'}
PORT = 443
Listeners = []

certfile = "/etc/letsencrypt/live/CHANGEME/fullchain.pem"
keyfile = "/etc/letsencrypt/live/CHANGEME/privkey.pem"

externalurl = "https://YourCmmPublicAddress.com"

authid = "CHANGEME"
authtoken = "CHANGEME"

# Web page HTML definitions
HTML_INDEX = """
<!DOCTYPE html>
<html>
<head>
<title>Call Me Maybe</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3pro.css">
</head>
<body>

<p>&nbsp;</p>
<div class="w3-container w3-card" style="text-align: center;">
<h1 style="text-align: center;"><strong><span style="font-family: Verdana,Geneva,sans-serif;"><em><span style="color: #2c82c9;">Call Me Maybe</span></em></span></strong></h1>
<input type="button" value="Spoof Call" onclick="window.location.href='/call'">
<input type="button" value="Spoof SMS" onclick="window.location.href='/message'">
</div>
</body>
"""

HTML_CALL = """
<!DOCTYPE html>
<html>
<head>
<title>Call Me Maybe</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3pro.css">
</head>
<body>

<p>&nbsp;</p>
<div class="w3-container w3-card">
<h1 style="text-align: center;"><strong><span style="font-family: Verdana,Geneva,sans-serif;"><em><span style="color: #2c82c9;">Call Me Maybe</span></em></span></strong></h1>
<iframe width="0" height="0" border="0" name="emptyframe" id="emptyframe"></iframe>
<form action="./makecall" method="post">
<div style="margin-bottom: 5px; text-align: center;">
<p id="spoofnumberentry"><strong><span style="font-family: Tahoma,Geneva,sans-serif;">Number to Spoof:</span></strong></p>
<input autocomplete="off" name="spoofnumber" type="text"/>
<p id="victimnumberentry" style="text-align: center;"><strong>Victim to Call</strong></p>
<input autocomplete="off" name="victimnumber" type="text"/>
<p id="yournumberentry" style="text-align: center;"><strong>Your Number:</strong></p>
<input autocomplete="off" name="yournumber" type="text"/></div>
<div style="text-align: center;"><input type="submit" value="Call" /></div>
</form></div>

</body>
"""

HTML_MESSAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Call Me Maybe</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3pro.css">
</head>
<body>

<p>&nbsp;</p>
<div class="w3-container w3-card">
<h1 style="text-align: center;"><strong><span style="font-family: Verdana,Geneva,sans-serif;"><em><span style="color: #2c82c9;">Call Me Maybe</span></em></span></strong></h1>
<iframe width="0" height="0" border="0" name="emptyframe" id="emptyframe"></iframe>
<form action="./sendmessage" method="post">
<div style="margin-bottom: 5px; text-align: center;">
<p id="spoofnumberentry"><strong><span style="font-family: Tahoma,Geneva,sans-serif;">Number to Spoof:</span></strong></p>
<input autocomplete="off" name="spoofnumber" type="text"/>
<p id="victimnumberentry" style="text-align: center;"><strong>Victim to SMS</strong></p>
<input autocomplete="off" name="victimnumber" type="text"/>
<p id="smsentry" style="text-align: center;"><strong>Message:</strong></p>
<input autocomplete="off" name="smscontent" type="text"/></div>
<div style="text-align: center;"><input type="submit" value="Send" /></div>
</form></div>

</body>
"""

HTML_REDIRECT = """
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Refresh" content="4; url=/" />
  </head>
  <body>
    <p>Successfully Executed!.</p>
  </body>
</html>
"""

class IndexHandler(DigestAuthMixin, tornado.web.RequestHandler):
    @auth_required(realm='Protected', auth_func=credentials.get)
    def get(self):
        self.write(HTML_INDEX)
class IndexHandlerCall(DigestAuthMixin, tornado.web.RequestHandler):
    @auth_required(realm='Protected', auth_func=credentials.get)
    def get(self):
        self.write(HTML_CALL)
		
class IndexHandlerMessage(DigestAuthMixin, tornado.web.RequestHandler):
    @auth_required(realm='Protected', auth_func=credentials.get)
    def get(self):
        self.write(HTML_MESSAGE)
        
class MakeCallFunction(DigestAuthMixin, tornado.web.RequestHandler):
    @auth_required(realm='Protected', auth_func=credentials.get)
    def post(self):
        global spoofnumber
        global victimnumber
        global yournumber
        global XMLCALL
        spoofnumber  = self.get_argument('spoofnumber')
        victimnumber  = self.get_argument('victimnumber')
        yournumber  = self.get_argument('yournumber')
        XMLCALL = '<Response><Dial callerId="' + str(spoofnumber) + '"><Number>' + str(victimnumber) + '</Number></Dial></Response>'
        client = plivo.RestClient(auth_id=authid, auth_token=authtoken)
        response = client.calls.create(
                from_ = spoofnumber,
                to_= yournumber,
                answer_url = externalurl + '/voiceanswer.xml',
                answer_method='POST', )
        print(response)
        self.redirect('/success')
		
class SendMessageFunction(DigestAuthMixin, tornado.web.RequestHandler):
    @auth_required(realm='Protected', auth_func=credentials.get)
    def post(self):
        global spoofnumber
        global victimnumber
        global smscontent
        spoofnumber  = self.get_argument('spoofnumber')
        victimnumber  = self.get_argument('victimnumber')
        smscontent  = self.get_argument('smscontent')
        client = plivo.RestClient(auth_id=authid, auth_token=authtoken)
        response = client.messages.create(
                src = spoofnumber,
                dst = victimnumber,
                text = smscontent, )
        print(response)
        self.redirect('/success')
		
class VoiceAnswerFunction(DigestAuthMixin, tornado.web.RequestHandler):
    def post(self):
        self.write(XMLCALL)

class Success(tornado.web.RequestHandler):
    def get(self):
        self.write(HTML_REDIRECT)

application = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/call', IndexHandlerCall),
    (r'/message', IndexHandlerMessage),
    (r'/makecall', MakeCallFunction),
    (r'/sendmessage',SendMessageFunction),
    (r'/voiceanswer.xml', VoiceAnswerFunction),
    (r'/success', Success),
])

http_server = tornado.httpserver.HTTPServer(application, ssl_options={
        "certfile": certfile,
        "keyfile": keyfile,
		"ssl_version": ssl.PROTOCOL_TLSv1_2,
        "ciphers": "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH",
    })
http_server.listen(PORT)
tornado.ioloop.IOLoop.instance().start()

#!/usr/bin/python

import sys, string
import httplib2
import requests
import json
import time
import datetime
import Adafruit_DHT

# Nest API auth token.
# See here for details: https://developer.nest.com/documentation/cloud/how-to-auth
nestauthtoken = "NestAuthToken"

# Nest device ID.
nestdeviceid = "NestDeviceID"

# Host you want to post to: localhost would be an
# emoncms installation on this computer, this could
# be changed to emoncms.org to post to emoncms.org.
emoncmshost = "http://emoncms.org"

# Location of emoncms install on your server, the
# standard setup is to place it in a folder called emoncms
# To post to emoncms.org change this to blank: ""
emoncmspath = ""

# Write apikey of emoncms account.
emoncmsapikey = "EmoncmsApiKey"

# Node id youd like the emontx to appear from.
nodeid = 0

# Define HTTP connection to emoncms host.
emoncmsconn = httplib2.Http()

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT22

# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4


try:
  # Read in json from Nest API - Your Nest API token goes here after devices?auth=
  r = requests.get('https://developer-api.nest.com/devices?auth='+nestauthtoken)
except ValueError:
  print ("Error contacting Nest API.")
  print (msg)
else:
  data = r.json()
  # Print data to console in JSON format.
  print (json.dumps(data, sort_keys=False, indent=4))
  # Assign temperature and humidity values to new variables.
  temp = data['thermostats'][nestdeviceid]['ambient_temperature_f']
  humidity = data['thermostats'][nestdeviceid]['humidity']
  DHThumidity, DHTtemperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)

  try:
# Send to emoncms.  
   print ("Send data to EmonCMS")
   resp, content = emoncmsconn.request(emoncmshost+"/input/post.json?apikey="+emoncmsapikey+"&node="+str(nodeid)+"&json={AmbientTempF:"+str(temp)+"}")
   print (resp)
   resp, content = emoncmsconn.request(emoncmshost+"/input/post.json?apikey="+emoncmsapikey+"&node="+str(nodeid)+"&json={DHT22_TempF:"+str(DHTtemperature)+"}")
   print (resp)
   resp, content = emoncmsconn.request(emoncmshost+"/input/post.json?apikey="+emoncmsapikey+"&node="+str(nodeid)+"&json={Humidity:"+str(humidity)+"}")
   print (resp)
   resp, content = emoncmsconn.request(emoncmshost+"/input/post.json?apikey="+emoncmsapikey+"&node="+str(nodeid)+"&json={DHT22_Humidity:"+str(DHThumidity)+"}")
   print (resp)
  except ValueError:
   print ("Error sending to emoncms.")
   print (msg)

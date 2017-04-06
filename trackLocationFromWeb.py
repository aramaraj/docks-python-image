#trackLocationFromWeb.py
#this class has the folowing services
#/track?name=<value> GET method
#sendSms - method to send SMS messages
import urllib
import json
import re
import uuid
from time import sleep
from uuid import getnode as get_mac
import web
from  geoCodeMacId import GeoWifi
import json as simplejson
import web
import json as simplejson
from urllib2 import *
import  smtplib
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
from flask import json
from flask import Flask, url_for
from flask import request
app = Flask(__name__)

#app = web.application(urls, globals())
#connection = urlopen('http://localhost:8983/solr/geotags/select?wt=json&indent=true&q=name:ashok&sort=_version_+desc')

@app.route('/')
def api_root():
    return 'Welcome'
    
@app.route('/track')
def api_track():
	if 'name' in request.args:
	  name =request.args['name']
	  getLatLong(name)
	  print name
	  return getLatLong(name)
		
          
def sendSms(lat,lng,name):
      #msg = MIMEMutipart('alternative')
      #msg['From'] = 'devops97@gmail.com'
      #msg['To'] = '6122229044@txt.att.net'
      #msg['Subject'] = 'simple email in python'
      #text = "http://maps.google.com/?q="
      text = "Location of  "+name+" is maps.google.com/?q="+"%.9f" % lat+","+"%.9f" % lng
      sender='devops97@gmail.com'
      receivers=['6122229044@txt.att.net']
      password='Walmart$123'
      #message='http://maps.google.com/?q='+lat+','+lng+''
      #message = 'ashok'
      try:
         	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
         	smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.ehlo()
                smtpObj.login(sender, password)
                smtpObj.sendmail(sender, receivers,text)
               	smtpObj.quit()
      except smtplib.SMTPException:
                print "Error: Unable to send mail"

def getLatLong(name):
	geo =  GeoWifi()
	serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
	key = 'AIzaSyANfnJH2TKPkGwScOy3IS3FPYcXP5dDuvo'	
	mac_id_key = 'AIzaSyAp8Ud-ZvbaFS0LYxbHk6a1-Uf-AhUIiWg'
	latlong = '37.3005408,-121.9263776'
	macid =  ':'.join(re.findall('..', '%012x' % uuid.getnode()))
	print macid
	latlong=geo.request(mac_id_key,macid)
	print 'latlong from mac address lookup',latlong 
	url = serviceurl + urllib.urlencode({'key':key,'latlng': latlong})
	print 'Retrieving', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'
	
	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ===='
		print data
		
	
	print json.dumps(js, indent=4)		
	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lng"]
	print 'lat',lat,'lng',lng
	location = js['results'][0]['formatted_address']
	sendSms(lat,lng,name)
	return "Location of the Delivery truck number "+name+"  is  "+location +" and Map URL is http://maps.google.com/?q="+"%.9f" % lat+","+"%.9f" % lng 

if __name__ == "__main__":
   # app = web.application(urls, globals())
    app.run(host='0.0.0.0')

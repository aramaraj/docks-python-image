import sys
import urllib
import urllib2
import json
import time
#
# geoCodeMacId.py
# GeoWifi
# this class is used for getting the Lat Long based on the Mac Id.using the geoLocate API 
# author: aramaraj

class GeoWifi():

	HEADERS = { 'Content-Type' : 'application/json' }

	def request(self,key, addr1):
		print "I am in request"
		url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + "AIzaSyAp8Ud-ZvbaFS0LYxbHk6a1-Uf-AhUIiWg"
		text = self.buildJson( addr1)
		print text
		req = urllib2.Request(url, text, self.HEADERS)
		res = urllib2.urlopen(req)
		body = res.read()
		print body
		return self.parseResponse(body)
	def buildJson(self,addr1):
		obj = {}
		obj[ "wifiAccessPoints" ] = self.buildAddressList(addr1)
		text = json.dumps(obj)
		return text
	def buildAddressList(self,addr1):
		list = []
		list.append(self.buildAddress(addr1) )
		return list
	def buildAddress(self,addr):
		dict = { "macAddress": addr }
		return dict
	def parseResponse(self,res):
		obj = json.loads(res)
		if obj["location"] is None:        
			print res
			return None
		if obj["location"]["lat"] is None:   
			print res
			return None
		if obj["location"]["lng"] is None:   
			print res
			return None
		if obj["accuracy"] is None: 
			accuracy = 0  
		else:
			accuracy = obj["accuracy"]  	
		ret = {}	
		ret["lat"] = obj["location"]["lat"]
		ret["lng"] = obj["location"]["lng"]		
		ret["accuracy"] = accuracy	
			
		return  "%.9f" % ret["lat"]+","+"%.9f" % ret["lng"]

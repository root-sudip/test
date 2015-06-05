import requests
import eventlet

eventlet.monkey_patch() 
with eventlet.Timeout(10):    
	requests.get("http://www.example.com/", verify=False)
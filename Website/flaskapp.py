# from urllib import request
from flask import Flask, render_template, url_for
from flask import request
import requests
import json
import urllib.request
import logging


app = Flask(__name__, static_url_path='/static')

@app.route("/",methods = ["POST","GET"])
def home():


	return render_template('app2.html')


@app.route("/<name>", methods = ["POST","GET"])
def switch(name):

	url = "https://dev-onem2m.iiit.ac.in/~/in-cse/in-name/AE-WiSUN/Data"
	header = {
		"X-M2M-Origin": "devtest:devtest",
		"Content-type": "application/json;ty=4"
        	}

	on = {
		"m2m:cin" :{
			"con":".onsf"
			}
		}
	off = {
		"m2m:cin" :{
			"con":".offsf"
			}
		}

	if (name == "on"):
		x = requests.post(url, headers=header,json =on )
		app.logger.info(x)
		return render_template('app3.html')

	elif (name == "off"):
		x = requests.post(url, headers=header,json =off )
		app.logger.info(x)
		return render_template('app2.html')



if __name__ == "__main__":
	app.run(debug = False,host = '0.0.0.0')
	#app.run()

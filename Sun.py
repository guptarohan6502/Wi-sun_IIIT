#script for api request on weather and sunrise/sunset time(SCRC)
import requests,json
from datetime import date
from datetime import datetime
import socket
UDP_IP =  "fd12:3456::5232:5fff:fe42:8a37"
UDP_IP1 = "fd12:3456::b6e3:f9ff:fea6:2e7"
UDP_IP2 = "fd12:3456::b6e3:f9ff:fea6:331"
UDP_IP3 = "fd12:3456::b6e3:f9ff:fea6:314"
UDP_PORT = 5001 # Port 
HOST_IP="fd12:3456::1"
PORT = 5005
def lights_on():
    while True:
        MESSAGE = ".allon"

        print ("UDP target IP:", UDP_IP) 
        print ("UDP target port:", UDP_PORT) 
        print ("message:", MESSAGE) 

        message_bytes = str.encode(MESSAGE) 
        sock = socket.socket(socket.AF_INET6, # Internet
                            socket.SOCK_DGRAM) # UDP
        sock.sendto(message_bytes, (UDP_IP, UDP_PORT))
        sock.sendto(message_bytes, (UDP_IP1, UDP_PORT))
        sock.sendto(message_bytes, (UDP_IP2, UDP_PORT))
        sock.sendto(message_bytes, (UDP_IP3, UDP_PORT))
        while True:
            
            sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            sock.bind((HOST_IP, PORT))
            data, addr = sock.recvfrom(2048) # buffer size is 2048 bytes
            print ("received message:", data)
def lights_off():
    while True:
        MESSAGE = ".alloff"

        print ("UDP target IP:", UDP_IP) 
        print ("UDP target port:", UDP_PORT) 
        print ("message:", MESSAGE) 

        message_bytes = str.encode(MESSAGE) 
        sock = socket.socket(socket.AF_INET6, # Internet
                            socket.SOCK_DGRAM) # UDP
        sock.sendto(message_bytes, (UDP_IP, UDP_PORT))
        sock.sendto(message_bytes, (UDP_IP1, UDP_PORT))
        sock.sendto(message_bytes, (UDP_IP2, UDP_PORT))
        sock.sendto(message_bytes, (UDP_IP3, UDP_PORT))
        while True:
            
            sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            sock.bind((HOST_IP, PORT))
            data, addr = sock.recvfrom(2048) # buffer size is 2048 bytes
            print ("received message:", data)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY ="hyderabad"
API_KEY = "4d29fcac0c909243f658b030414e3363"
location="17.387140, 78.491684"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response1 = requests.get(URL)

if response1.status_code == 200:

   data = response1.json()
   main = data['main']
   # temperature = main['temp']
   # humidity = main['humidity']
   # pressure = main['pressure']
   # feels_like = main['feels_like']
   # report = data['weather']
   # print(f"{CITY:-^30}")
   # print(f"Temperature: {temperature-273.15}")
   # print(f"Humidity: {humidity}")
   # print(f"feels_like: {feels_like}")
   # print(f"Pressure: {pressure}")
   # print(f"Weather Report: {report[0]['description']}")
else:

   print("Error in the HTTP  1 request."
         "Please try again.")

#api request for the sunrise and sunshine time below


url3 = "https://geo-services-by-mvpc-com.p.rapidapi.com/sun_positions"
todays_date=date.today()
print(todays_date)
querystring = {"location":str(location),"date":str(todays_date),"time":str()}

headers = {
   "X-RapidAPI-Key": "8a504f900emshb457c757695d1eep143046jsn51da1ed2ff04",
   "X-RapidAPI-Host": "geo-services-by-mvpc-com.p.rapidapi.com"
}

req = requests.request("GET", url3, headers=headers, params=querystring)
response=req.json()
response_str=json.dumps(response,indent=2)
sunrise_time=response['data']['sunrise']
sunset_time=response['data']['sunset']
sunrise_slice_time=list(sunrise_time[11:19])
sunset_slice_time=list(sunset_time[11:19])
print('Sunrise time in your loc is',sunrise_slice_time)
print('sunset time in your loc is',sunset_slice_time)

#light on/off depending on the sunrise/set time below
now_time=datetime.now()
current_time=now_time.strftime("%H:%M:%S")
current_slice_time=list(current_time)
# print('the current time in list is',current_slice_time) #uncomment if needed

if current_slice_time==sunrise_slice_time:
   lights_off()
   print("Lights Off")
elif current_slice_time==sunset_slice_time:
   lights_on()
   print("Lights Off")
else:
   print("Waiting for Sunrise/Sunset")


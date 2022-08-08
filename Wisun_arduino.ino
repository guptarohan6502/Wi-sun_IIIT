#include <SoftwareSerial.h>
const int RelayPin = A0;
SoftwareSerial mySerial(7, 8);//rx,tx
int relayState = 0;      // variable to store the read value

void setup()
{
delay(5000);
Serial.begin(9600);
mySerial.begin(9600);
//pinMode(13, OUTPUT);
pinMode(LED_BUILTIN, OUTPUT);
pinMode(RelayPin, OUTPUT);
digitalWrite(RelayPin, HIGH);
Serial.println("sending connect command");
Serial.println(F("Initialize System"));
mySerial.println("wisun connect");
}
void loop()
{
String str="";
while(mySerial.available())
{
str=mySerial.readStringUntil('\n');
Serial.println(str);
Serial.println(str.substring(1,3));
delay(5);
if(str.substring(1,13)=="IPv6 address")
{
Serial.println("working");
mySerial.println("wisun udp_server 5001");
mySerial.println("wisun udp_client fd12:3456::1 5005");
}
if(str.substring(1,6)=="allon")
{
//acd.setPower(MAX_POWER);
digitalWrite(RelayPin,LOW);
digitalWrite(LED_BUILTIN, HIGH);
mySerial.println("wisun socket_write 4 \"Node 6 is on\"");
relayState = digitalRead(RelayPin);
Serial.println("on");
}
if(str.substring(1,7)=="alloff")
{
digitalWrite(RelayPin,HIGH);
digitalWrite(LED_BUILTIN, LOW);
mySerial.println("wisun socket_write 4 \"Node 6 is off!\"");
relayState = digitalRead(RelayPin);
//Serial.println("off");
}
if(str.substring(1,4)=="on6")
{
digitalWrite(RelayPin,LOW);
digitalWrite(LED_BUILTIN, HIGH);
mySerial.println("wisun socket_write 4 \"Node 6 is on!\"");
relayState = digitalRead(RelayPin);

Serial.println("off");
}
if(str.substring(1,5)=="off6")
{
digitalWrite(RelayPin,HIGH);
digitalWrite(LED_BUILTIN, LOW);
mySerial.println("wisun socket_write 4 \"Node 6 is off!\"");
relayState = digitalRead(RelayPin);
Serial.println("off");
}
if(str.substring(1,5)=="sts6")
{
  if (relayState == HIGH)
mySerial.println("wisun socket_write 4 \"Node 6 is off!\"");
 else
mySerial.println("wisun socket_write 4 \"Node 6 is on!\"");
}
}
if (Serial.available()) 
{ 
mySerial.write(Serial.read());
}
}

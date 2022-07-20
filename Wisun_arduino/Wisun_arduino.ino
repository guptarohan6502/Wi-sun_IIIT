#include <SoftwareSerial.h>
#include <RBDdimmer.h>//https://github.com/RobotDynOfficial/RBDDimmer
//Parameters
const int zeroCrossPin = 2;
const int acdPin = 3;
int MIN_POWER = 21;
int MAX_POWER = 45;
//Variables
int power = 0;
//Objects
SoftwareSerial mySerial(7, 8);//rx,tx
dimmerLamp acd(acdPin);
void setup(){
delay(5000);
Serial.begin(9600);
mySerial.begin(9600);
pinMode(13, OUTPUT);
Serial.println("sending connect command");
Serial.println(F("Initialize System"));
acd.begin(NORMAL_MODE, ON);
mySerial.println("wisun connect");
}
void loop(){
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
//delay(500);
mySerial.println("wisun udp_server 5001");
//delay(1000);
mySerial.println("wisun udp_client fd12:3456::1 5005");
}
if(str.substring(1,3)=="on")
{
acd.setPower(MAX_POWER);
mySerial.println("wisun socket_write 4 \"its on!\"");
Serial.println("on");
}
if(str.substring(1,3)=="off")
{
acd.setPower(0);
Serial.println("off");
mySerial.println("wisun socket_write 4 \"its off!\"");
}
if(str.substring(1,4)=="dim")
{
acd.setPower(MIN_POWER);
//Serial.println("dim");
}
}
if (Serial.available()) {
mySerial.write(Serial.read());
}
}

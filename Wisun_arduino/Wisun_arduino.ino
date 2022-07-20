//Libraries
#include <SoftwareSerial.h>
#include <RBDdimmer.h>//https://github.com/RobotDynOfficial/RBDDimmer
//Parameters
const int zeroCrossPin  = 2;
const int acdPin  = 3;
int MIN_POWER  = 21;
int MAX_POWER  = 36;
//Variables
int power  = 0;
//Objects
SoftwareSerial mySerial(10, 11);//rx,tx
dimmerLamp acd(acdPin);
void setup(){

Serial.println("sending connect command");
pinMode(13, OUTPUT);
Serial.begin(9600);
Serial.println(F("Initialize System"));
acd.begin(NORMAL_MODE, ON);
mySerial.begin(9600);
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
  delay(500);
  mySerial.println("wisun udp_server 5001");
 } 
 if(str.substring(1,3)=="on")
 {
  acd.setPower(MAX_POWER);
  //Serial.println("on");
 }
  if(str.substring(1,3)=="of")
 {
  acd.setPower(0);
  //Serial.println("off");
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

//Libraries
#include <SoftwareSerial.h>
#include <RBDdimmer.h>//https://github.com/RobotDynOfficial/RBDDimmer
//Parameters
const int zeroCrossPin  = 2;
const int acdPin  = 3;
int MIN_POWER  = 21;
int MAX_POWER  = 45;
//Variables
int power  = 0;
String str="";
//Objects
SoftwareSerial mySerial(7, 8);//rx,tx
dimmerLamp acd(acdPin);

void setup(){
pinMode(LED_BUILTIN, OUTPUT);
pinMode(A0, OUTPUT);
Serial.begin(9600);
Serial.println("sending connect command");
Serial.println(F("Initialize System"));
acd.begin(NORMAL_MODE, ON);
mySerial.begin(9600);
mySerial.println("wisun connect");
 digitalWrite(LED_BUILTIN, HIGH);   
 delay(5000);                       
 digitalWrite(LED_BUILTIN, LOW);   

while(mySerial.available())
 {
 digitalWrite(LED_BUILTIN, HIGH);   
 delay(1000);                       
 digitalWrite(LED_BUILTIN, LOW);   
 delay(100); 
str=mySerial.readStringUntil('\n');
 Serial.println(str);
 Serial.println(str.substring(1,3));
 delay(5);
  if(str.substring(1,3)=="Fa")
  {
   
 digitalWrite(LED_BUILTIN, HIGH);   
 delay(1000);                       
 digitalWrite(LED_BUILTIN, LOW);   
 delay(1000); 
  break;
  }
  mySerial.println("wisun connect");

    }
  
  }
  
  
void loop(){
 
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
 if(str.substring(0,2)=="on")
 {
  digitalWrite(A0,LOW);
  //Serial.println("on");
 }
  if(str.substring(0,2)=="of")
 {
  digitalWrite(A0,HIGH);
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

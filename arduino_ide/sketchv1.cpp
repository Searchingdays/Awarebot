# define interval 1000  // track data every second or else it will be too much

# define interval2 20 // for 50 Hz frequency
// 
int prevtime =0;
int currtime;
float t=0;
float h=0;
int p =0;
//int ir = 0;   have to read on ir transmission and receiving
uint8_t c=0;

int mag =0 ;
int sound =0 ;
uint8_t s=0;
int sum = 0;
int c2;
int p2=0;

#include "DHT.h"

#define sample 20

int arr[sample];

#define DHTPIN 7 


#define DHTTYPE DHT11

DHT tnh(DHTPIN, DHTTYPE);

void setup() {
  
pinMode(A4, INPUT);          // magnet analog pin
pinMode(A5, INPUT);          // sound analog pin
pinMode(4, INPUT); 
pinMode(A3, INPUT);         // heartbeat sensor
pinMode(A2, INPUT);         // ir receiver

tnh.begin();
Serial.begin(9600);   
}

void loop() {

  currtime = millis();

  if (currtime - prevtime > interval){
    prevtime = currtime;


     h = tnh.readHumidity();

    t = tnh.readTemperature();

  }


  c2 = millis();

  if (c2 - p2 > interval2){

    p2 = c2;
    mag = analogRead(A4);
    sound = analogRead(A5);
    p = analogRead(A3);
  }                       // read sensors every 20ms

    if(t || h ){
  //Serial.print("temp:");
  Serial.print(t);
  Serial.print("\t");
  Serial.print(h);
  Serial.print("\t");
  //Serial.print("sound:");
  Serial.print(sound);
  Serial.print("\t");
  //Serial.print("mag:");
  Serial.print(mag);
  Serial.print("\t");
  //Serial.print(s);
  Serial.print(p);
  Serial.print("\t");
  //Serial.print(sum);
  Serial.print("\n");
  
}


  //}

    // arr[c] = p;
    // c = c+1;

    // if ( c== 19){

    // for(int i=0; i<20; i++){
    //     sum = sum + arr[i];
    // }
    // sum = sum/20 ;

    // Serial.print("hb\n");
    // Serial.print(sum);

    sum =0;

    c=0;

    //}
    //ir = analogRead(A2);

    //s = digitalRead(4);

}
  // put your main code here, to run repeatedly:

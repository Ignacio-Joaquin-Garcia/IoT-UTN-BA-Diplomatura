#include <SoftwareSerial.h>

SoftwareSerial bt(7,8);
int pinEstadoBt = 4;

void setup() {
  Serial.begin(9600);
  bt.begin(9600);
  pinMode(pinEstadoBt, INPUT);
}

void loop() {
  if (bt.available() > 0) {
      //"status-x-y-z"
      String mensaje = "";
      while(bt.available() > 0){
        char c = bt.read();
        mensaje += c;
      }
      
      Serial.println(mensaje);
      
  }

  if (Serial.available() > 0) {
      bt.write(Serial.read());
  }
  delay(200);
}

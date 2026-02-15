#include <Stepper.h>
Stepper motorPasoAPaso(2048,5,4,3,2);
String comandoSerial = "";
bool parar = false;

void setup() {
  motorPasoAPaso.setSpeed(2);
  Serial.begin(9600);
}

void loop() {
  if(!parar){
    motorPasoAPaso.step(-1024);
    delay(2000);
  }
}
void serialEvent(){
  while(Serial.available()>0){
    char charRecibido = (char) Serial.read();
    if (charRecibido == '\n' || charRecibido == '\r') {
      comandoSerial.trim();
      
      if (comandoSerial == "stop") {
        parar = true;
        Serial.println("Motor DETENIDO");
      } 
      else if (comandoSerial == "start") {
        parar = false;
        Serial.println("Motor INICIADO");
      }
      comandoSerial = ""; 
    } else {
      comandoSerial += charRecibido;
      Serial.println(comandoSerial);
    }
  }
}
#include <SoftwareSerial.h>
SoftwareSerial moduloBT(9,10);
int pinLed = 3;

void setup() {
  pinMode(pinLed, OUTPUT);
  Serial.begin(9600);
  moduloBT.begin(9600);
  Serial.println("Inicio");
  digitalWrite(pinLed, LOW);
}

void loop() {
  if(moduloBT.available()>0){
    
    int rawData = moduloBT.read(); 
    Serial.print("Recibido (Decimal): ");
    Serial.println(rawData);       
    
    char letra = (char)rawData;    
    Serial.print("Recibido (Letra): ");
    Serial.println(letra);

    
    if(letra == '0'){
      digitalWrite(pinLed, LOW);
    }
    if(letra == '1'){
      digitalWrite(pinLed, HIGH);
    }
  }
  if(Serial.available()>0){
    moduloBT.write(Serial.read());

  }

}

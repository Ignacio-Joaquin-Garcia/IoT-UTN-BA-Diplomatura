#include <IRremote.hpp>
const int RECV_PIN = 11;
const int ledPins[3] = {5, 4, 3};

void parpadeoLed(int pinLed){
  digitalWrite(ledPins[pinLed], HIGH);
  delay(1500);
  digitalWrite(ledPins[pinLed], LOW);
}

void setup() {
  // put your setup code here, to run once:
  IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(IrReceiver.decode()){
    if (IrReceiver.decodedIRData.protocol != UNKNOWN) {
      Serial.println("El protocolo viene de una fuente desconocida!");
    } else {
      Serial.println("Posible señal con ruido");
    }
    IrReceiver.printIRResultShort(&Serial);
    uint16_t comando = IrReceiver.decodedIRData.command;
    delay(10);
    switch (comando){
      case 0x11: //Boton 1
        parpadeoLed(0);
        break;
      case 0x12: //Boton 2
        parpadeoLed(1);
        break;
      case 0x13: //Boton 3
        parpadeoLed(2);
        break;
      case 0x14: //Boton 4
        for(int i =0; i<=3;i++){
          for(int j = 0; j<3;j++){
            digitalWrite(ledPins[j], HIGH);
            delay(500);
            digitalWrite(ledPins[j], LOW);
            delay(500);
          }
          for(int j = 0; j<3;j++){
            digitalWrite(ledPins[j], HIGH);
            delay(500);
          }
          digitalWrite(ledPins[i], LOW);
        }
        delay(100);
        digitalWrite(ledPins[0], LOW);
        digitalWrite(ledPins[1], LOW);
        digitalWrite(ledPins[2], LOW);
         
        break;
      case 0xB: //PowerButton
        digitalWrite(ledPins[0], HIGH);
        digitalWrite(ledPins[1], HIGH);
        digitalWrite(ledPins[2], HIGH);
        delay(2000);
        digitalWrite(ledPins[0], LOW);
        digitalWrite(ledPins[1], LOW);
        digitalWrite(ledPins[2], LOW);
        break;
      
      default:
        for(int i = 0;i<5;i++){
          digitalWrite(ledPins[0], HIGH);
          digitalWrite(ledPins[1], HIGH);
          digitalWrite(ledPins[2], HIGH);
          delay(50);
          digitalWrite(ledPins[0], LOW);
          digitalWrite(ledPins[1], LOW);
          digitalWrite(ledPins[2], LOW);
          delay(50);
        }
        break;
    }
    Serial.println(comando,HEX);
    IrReceiver.resume();
  }


}

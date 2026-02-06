#include <IRremote.h>

int pinLed = 3;
int pinReceptorIR = 11;
IRrecv irrecv(pinReceptorIR);
decode_results resultados;

void setup() {
  DDRD = B10010100;
  pinMode(pinReceptorIR, INPUT);
  irrecv.enableIRIn();
  Serial.begin(9600);
}

void loop() {
  if(irrecv.decode(&resultados)){
    digitalWrite(pinLed, HIGH);
    Serial.println(resultados.value, HEX);
    irrecv.resume();
    delay(10);
    delay(1000);
    digitalWrite(pinLed,LOW);
  }
}

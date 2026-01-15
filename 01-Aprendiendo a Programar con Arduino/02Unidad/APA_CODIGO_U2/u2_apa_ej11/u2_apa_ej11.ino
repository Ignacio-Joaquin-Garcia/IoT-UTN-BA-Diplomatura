int pinAnalogico = A0;
void setup(){
  Serial.begin(9600);
}

void loop(){
  analogWrite(pinAnalogico, 255);
}
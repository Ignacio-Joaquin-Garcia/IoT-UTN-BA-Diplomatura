void setup(){
  Serial.begin(9600);
}

void loop(){
  //defino variables
  int pinPotenciometro = A0;
  int pinLed = A1;
  int valorPotenciometro;
  
  //hago operaciones
  valorPotenciometro = analogRead(pinPotenciometro);
  valorPotenciometro = map(valorPotenciometro, 0,1023,0,255);
  Serial.println(valorPotenciometro);
  analogWrite(pinLed, valorPotenciometro);
}
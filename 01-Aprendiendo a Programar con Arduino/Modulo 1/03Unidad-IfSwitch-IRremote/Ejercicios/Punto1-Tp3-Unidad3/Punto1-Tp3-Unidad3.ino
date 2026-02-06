int pinesBoton[3] = {6,7,8};
int pinesLeds[2] = {11,10};

void setup() {
  //CONFIGURACION BOTONES
  DDRD = B00111111; 
  //CONFIGURACION LEDS SALIDAS
  DDRB = B00110000;
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int botonPresionado;
  if(digitalRead(pinesBoton[0])){
    botonPresionado = 0;
  }
  if(digitalRead(pinesBoton[1])){
    botonPresionado = 1;
  }
  if(digitalRead(pinesBoton[2])){
    botonPresionado = 2;
  }
  if((digitalRead(pinesBoton[0]) || digitalRead(pinesBoton[1]) || digitalRead(pinesBoton[2])) == 0){
    botonPresionado = -1;
  }
  switch (botonPresionado){
    case 0:
      for(int i = 0;i<256;i++){
        
        analogWrite(pinesLeds[0], i);
        delay(50);
        Serial.println(i);
      };
      break;
    case 1:
      for(int i = 255;i>=0;i--){
        analogWrite(pinesLeds[1], i);
        delay(50);
      }
      break;
    case 2:
      for(int i = 0; i<=5;i++){
        analogWrite(pinesLeds[0], 255);
        analogWrite(pinesLeds[1], 255);
        delay(50);
        analogWrite(pinesLeds[0], 0);
        analogWrite(pinesLeds[1], 0);
        delay(50);
      };
      break;
    default:
      analogWrite(pinesLeds[0], 0);
      analogWrite(pinesLeds[1], 0);
      break;
  }
  Serial.println(botonPresionado);
  delay(100);
}

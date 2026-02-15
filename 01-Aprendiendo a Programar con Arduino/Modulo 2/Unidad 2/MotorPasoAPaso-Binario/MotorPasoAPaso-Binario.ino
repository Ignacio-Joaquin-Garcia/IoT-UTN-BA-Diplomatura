byte PasoSimple[4] = {0b00100000, 0b00010000, 0b00001000, 0b00000100};
byte PasoDoble[4] =  {0b00110000, 0b00011000, 0b00001100, 0b00100100};
void setup() {
  DDRD = 0xFF;
}

void loop() {
  for(int j = 0; j<500; j++){
    for(int i = 0;i<4;i++){
      PORTD = PasoSimple[i];
      delay(15);
    }
  }
  delay(2000);
  for(int j = 0; j<500; j++){
    for(int i = 0;i<4;i++){
      PORTD = PasoDoble[i];
      delay(15);
    }
  }
}

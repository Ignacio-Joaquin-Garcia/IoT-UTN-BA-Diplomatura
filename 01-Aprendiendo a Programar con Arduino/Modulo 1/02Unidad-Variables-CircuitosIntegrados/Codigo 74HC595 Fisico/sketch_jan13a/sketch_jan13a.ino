int pinPulso = 2;
int pinBinario = 3;
int pinSubir = 4;

int pinPrueba = 12;


void setup()
{
  pinMode(pinPulso, OUTPUT);
  pinMode(pinBinario, OUTPUT);
  pinMode(pinSubir, OUTPUT);
  pinMode(pinPrueba, OUTPUT);
}

void loop()
{
  /*
  digitalWrite(pinSubir, LOW);
  digitalWrite(pinBinario, HIGH);
  for(int i=0; i<8;i++){
    digitalWrite(pinPulso, HIGH);
    digitalWrite(pinPulso, LOW);
  };
  digitalWrite(pinSubir, HIGH);
  digitalWrite(pinPrueba, HIGH);
  delay(500);
  */
  for(int i = 0; i<255;i++){
    digitalWrite(pinSubir, LOW); 
    shiftOut(pinBinario, pinPulso, MSBFIRST, i);
    digitalWrite(pinSubir, HIGH); 
    delay(100);
  }

 
}

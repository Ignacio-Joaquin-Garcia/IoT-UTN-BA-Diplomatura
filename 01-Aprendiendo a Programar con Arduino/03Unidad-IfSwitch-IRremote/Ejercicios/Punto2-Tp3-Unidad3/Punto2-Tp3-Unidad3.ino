int pinLecturaPotenciometro = A0;
int pinLedRojo = 11;
int pinLedVerde = 10;
int pinLedAzul = 9;

void setup() {
  DDRB = B00001110;
  Serial.begin(9600);
}

void loop() {
  int valorPotenciometro;
  for(int i = 0; i<=255; i++){
    valorPotenciometro = analogRead(pinLecturaPotenciometro);
    analogWrite(pinLedRojo, i);
    delay(valorPotenciometro);
    Serial.println("Rojo");
    Serial.println(valorPotenciometro);
  }
  for(int j = 0; j<=255; j++){
    valorPotenciometro = analogRead(pinLecturaPotenciometro);
    analogWrite(pinLedVerde, j);
    delay(valorPotenciometro);
    Serial.println("Verde");
    Serial.println(valorPotenciometro);
  }
  for(int n = 0; n<=255; n++){
    valorPotenciometro = analogRead(pinLecturaPotenciometro);
    analogWrite(pinLedAzul, n);
    delay(valorPotenciometro);
    Serial.println("Azul");
    Serial.println(valorPotenciometro);
  };
};

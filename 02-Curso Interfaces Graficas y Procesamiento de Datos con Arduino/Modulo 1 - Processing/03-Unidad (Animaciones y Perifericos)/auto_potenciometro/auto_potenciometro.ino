int potenciometro = A0;

void setup() {
  pinMode(potenciometro, INPUT);
  Serial.begin(9600);
}

void loop() {
  int valorPotenciometro = analogRead(potenciometro);
  Serial.println(valorPotenciometro);
  delay(1000);
}

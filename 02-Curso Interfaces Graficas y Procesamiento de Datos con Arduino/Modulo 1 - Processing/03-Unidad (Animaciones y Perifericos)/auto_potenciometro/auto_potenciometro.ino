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

/*
void serialEvent(){
  if(Serial.available() > 0){
    String data = Serial.readStringUntil('\n');
    Serial.println(data);    
  }
}
*/
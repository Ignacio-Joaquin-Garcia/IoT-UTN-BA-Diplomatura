String comando = "";
int pinRele = 8;

void setup() {
  pinMode(pinRele, OUTPUT);
  Serial.begin(9600);
}

void loop() {
}

void serialEvent() {
  while (Serial.available() > 0) {
    char l = Serial.read();

    if (l == '\r') continue;

    if (l == '\n') {
      if (comando == "circuito 1") {
        digitalWrite(pinRele, HIGH);
      }

      if (comando == "circuito 2") {
        digitalWrite(pinRele, LOW);
      }

      comando = "";
    } 
    else {
      comando += l;
    }
  }
}
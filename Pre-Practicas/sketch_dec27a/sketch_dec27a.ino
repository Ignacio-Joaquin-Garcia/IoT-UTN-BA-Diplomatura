int pinLecturaPotenciometro = A0;
int pinLedAnalogico = 3;

void setup() {
  // put your setup code here, to run once:
  pinMode(pinLecturaPotenciometro, INPUT);
  pinMode(pinLedAnalogico, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valorPotenciometro = analogRead(pinLecturaPotenciometro);
  int valorAnalogicoLed = map(valorPotenciometro,0,1023,0,255);
  Serial.println(valorAnalogicoLed);
  analogWrite(pinLedAnalogico, valorAnalogicoLed);
}
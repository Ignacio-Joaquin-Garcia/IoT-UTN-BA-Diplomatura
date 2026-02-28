int pinVoltaje = A0;
float lectorVol;
float voltaje;


int corriente = 3;
int power = 255;

void setup() {
  // put your setup code here, to run once:
  pinMode(corriente, OUTPUT);
  pinMode(pinVoltaje, INPUT);
  Serial.begin(9600);

  
}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(corriente, power);
  lectorVol = analogRead(pinVoltaje);
  voltaje = (5.*lectorVol)/1023.;
  Serial.print("lector: ");
  Serial.println(lectorVol);
  Serial.print("Vol: ");
  Serial.println(voltaje);
  delay(100);
}

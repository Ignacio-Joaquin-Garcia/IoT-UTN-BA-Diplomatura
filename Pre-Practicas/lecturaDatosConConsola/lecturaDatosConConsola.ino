int ledV = 2;
String msg1 = "Ingrese 1 o 0 si quiere prender o apagar el led";
int onOff;
int dt = 200;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledV, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(msg1);
  while (Serial.available() == 0) {};
  onOff = Serial.parseInt();

  Serial.println(onOff);
  if(onOff == 1){
    digitalWrite(ledV, HIGH);
  }
  if(onOff == 0){
    digitalWrite(ledV, LOW);
  }
  delay(dt);
}

int ledR = 7;
int ledY = 4;
int ledG = 2;

String msgOn = "Ingresa led a prender: (rojo, verde o amarillo)";
String ledOn;
String msgOff = "Quieres apagar algun led? (rojo, verde o amarillo)";
String ledOff;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledR, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledG, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(msgOn);
  while(Serial.available() == 0){};
  ledOn = Serial.readString();

  if(ledOn == "rojo"){digitalWrite(ledR, 1);}
  if(ledOn == "amarillo"){digitalWrite(ledY, 1);}
  if(ledOn == "verde"){digitalWrite(ledG, 1);}

  Serial.println(msgOff);
  while(Serial.available() == 0){};
  ledOff = Serial.readString();

  if(ledOff == "rojo"){digitalWrite(ledR, 0);}
  if(ledOff == "amarillo"){digitalWrite(ledY, 0);}
  if(ledOff == "verde"){digitalWrite(ledG, 0);}
}

int ledR = 7;
int ledY = 4;
int ledG = 2;

String msgOn = "Ingresa led a prender: (rojo, verde, amarillo, todos, o apagarTodos)";
String ledOn;
int swLedOn;

int dtMinus = 60;
int dt = 120;
int dtPlus = 240;
int i;

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

  if (ledOn == "rojo"){swLedOn = 1;}
  else if (ledOn == "amarillo"){swLedOn = 2;}
  else if (ledOn == "verde"){swLedOn = 3;}
  else if (ledOn == "todos"){swLedOn = 4;}
  else if (ledOn == "apagarTodos"){swLedOn = 5;}



  switch (swLedOn){  // El Switch no acepta strings
    case 1:
      digitalWrite(ledR, HIGH);
      digitalWrite(ledY, LOW);
      digitalWrite(ledG, LOW);
      swLedOn = 999;
      break;

    case 2:
      digitalWrite(ledR, LOW);
      digitalWrite(ledY, HIGH);
      digitalWrite(ledG, LOW);
      swLedOn = 999;
      break;

    case 3:
      digitalWrite(ledR, LOW);
      digitalWrite(ledY, LOW);
      digitalWrite(ledG, HIGH);
      swLedOn = 999;
      break;

    case 4:
      digitalWrite(ledR, HIGH);
      digitalWrite(ledY, HIGH);
      digitalWrite(ledG, HIGH);
      swLedOn = 999;
      break;

    case 5:
      digitalWrite(ledR, LOW);
      digitalWrite(ledY, LOW);
      digitalWrite(ledG, LOW);
      swLedOn = 999;
      break;

    default:
      for(i=1;i<=5;i++){
        digitalWrite(ledR, LOW);
        digitalWrite(ledY, LOW);
        digitalWrite(ledG, LOW);
        delay(dtPlus);

        digitalWrite(ledR, LOW);
        digitalWrite(ledY, LOW);
        digitalWrite(ledG, HIGH);
        delay(dt);

        digitalWrite(ledR, LOW);
        digitalWrite(ledY, HIGH);
        digitalWrite(ledG, LOW);
        delay(dt);

        digitalWrite(ledR, HIGH);
        digitalWrite(ledY, LOW);
        digitalWrite(ledG, LOW);
        delay(dt);

        digitalWrite(ledR, LOW);
        digitalWrite(ledY, HIGH);
        digitalWrite(ledG, LOW);
        delay(dt);

        digitalWrite(ledR, LOW);
        digitalWrite(ledY, LOW);
        digitalWrite(ledG, HIGH);
        delay(dt);

        digitalWrite(ledR, LOW);
        digitalWrite(ledY, HIGH);
        digitalWrite(ledG, LOW);
        delay(dt);

        digitalWrite(ledR, HIGH);
        digitalWrite(ledY, LOW);
        digitalWrite(ledG, LOW);
        delay(dt);
      }
  }
}

int buzzerA = 3;
int input = A0;
int corrientePotenciometro = 13;

String msg1 = "Valor: "; 

int resistencia;
int dt = 250;
void setup() {
  // put your setup code here, to run once:
  pinMode(buzzerA, OUTPUT);
  pinMode(corrientePotenciometro, OUTPUT);
  pinMode(input, INPUT);
  Serial.begin(9600);
  digitalWrite(corrientePotenciometro, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  resistencia = analogRead(input);
  Serial.print(msg1);
  Serial.println(resistencia);

  if(resistencia >= 1000){
    digitalWrite(buzzerA, HIGH);
    delay(dt);
    digitalWrite(buzzerA,LOW);
  }
  if(resistencia < 1000){
    digitalWrite(buzzerA,LOW);
  }
  delay(1000);

  
}

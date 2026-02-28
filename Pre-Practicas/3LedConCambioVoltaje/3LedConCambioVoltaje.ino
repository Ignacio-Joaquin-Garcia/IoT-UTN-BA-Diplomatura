float lectorV;
float voltaje;
int pinMedidor = A0;
int pinPotenciaMedidor = 3;
int pinLedV = 4;
int pinLedA = 5;
int pinLedR = 6;

void setup() {
  // put your setup code here, to run once:
  pinMode(pinMedidor, INPUT);
  pinMode(pinPotenciaMedidor, OUTPUT);
  pinMode(pinLedV, OUTPUT);
  pinMode(pinLedA, OUTPUT);
  pinMode(pinLedR, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pinPotenciaMedidor, 1);
  lectorV = analogRead(pinMedidor);
  voltaje = (5*lectorV)/1023;
  Serial.print("Voltaje: ");
  Serial.println(voltaje);
  Serial.println(lectorV);
  
  
  if(voltaje > 4){
    digitalWrite(pinLedR, 1);
    digitalWrite(pinLedA, 0);
    digitalWrite(pinLedV, 0);
  }
  if(voltaje > 3 && voltaje <= 4){
    digitalWrite(pinLedA, 1);
    digitalWrite(pinLedV, 0);
    digitalWrite(pinLedR, 0);
  }
  if(voltaje <= 3 ){
    digitalWrite(pinLedV, 1);
    digitalWrite(pinLedR, 0);
    digitalWrite(pinLedA, 0);
  }
  
  

  
  
  delay(500);



}

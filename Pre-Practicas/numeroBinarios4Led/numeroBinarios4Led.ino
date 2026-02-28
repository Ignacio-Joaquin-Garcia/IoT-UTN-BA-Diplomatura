int pin0Bin = 8;
int pin1Bin = 9;
int pin2Bin = 10;
int pin3Bin = 11;

int pOF = LOW;

int suma = 0;
String numBinarioTexto;
int cocienteDiv;
int restoDiv;
int aux;

int numBinario;
int led1, led2, led3, led4;

void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);

  pinMode(pin0Bin,OUTPUT);
  pinMode(pin1Bin,OUTPUT);
  pinMode(pin2Bin,OUTPUT);
  pinMode(pin3Bin,OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  Serial.print("Decimal: ");
  Serial.println(suma);
  aux = suma;

  while(aux > 0){
    cocienteDiv = (aux / 2); //auto truncado gracias a variable int
    restoDiv = aux % 2;
    numBinarioTexto = restoDiv + numBinarioTexto;
    aux = cocienteDiv; 
    Serial.print("Binario: ");
    Serial.println(numBinarioTexto);
  };

  numBinario = numBinarioTexto.toInt();
  led1 = numBinario % 10000/1000;
  led2 = numBinario % 1000/100;
  led3 = numBinario % 100/10;
  led4 = numBinario % 10;
  Serial.print("led1: ");
  Serial.print(led1);
  Serial.print("  led2: ");
  Serial.print(led2);
  Serial.print("  led3: ");
  Serial.print(led3);
  Serial.print("  led4: ");
  Serial.println(led4);

  digitalWrite(pin0Bin,led1);
  digitalWrite(pin1Bin,led2);
  digitalWrite(pin2Bin,led3);
  digitalWrite(pin3Bin,led4);

  delay(5000);
  numBinarioTexto = "";
  suma = suma + 1;
}

int buzzerA = 3;

String msg1 = "Ingresa una palabra a convertir a morse: ";
String palabra;
int longitudPalabra;

int i;
char letra;

int wait = 100;
int waitP = 500;
int punto = 150;
int barra = 400;


void setup() {
  // put your setup code here, to run once:
  pinMode(buzzerA, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(msg1);
  while(Serial.available() == 0){};
  palabra = Serial.readString();
  palabra.trim(); //saca Espacios
  palabra.toLowerCase(); //pasa a minuscula

  longitudPalabra = palabra.length();
  Serial.println(longitudPalabra); //Exportamos longitud de la palabra

  for (i=0; i < longitudPalabra; i++){
    letra = palabra.charAt(i);
    if(letra == 'a'){
      digitalWrite(buzzerA, HIGH);
      delay(punto);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(barra);
      digitalWrite(buzzerA, LOW);
      delay(waitP);
    }
    if(letra == 'b'){
      digitalWrite(buzzerA, HIGH);
      delay(barra);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(punto);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(punto);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(punto);
      digitalWrite(buzzerA, LOW);
      delay(waitP);
    }
    if(letra == 'c'){
      digitalWrite(buzzerA, HIGH);
      delay(barra);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(punto);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(barra);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(punto);
      digitalWrite(buzzerA, LOW);
      delay(waitP);
    }
    if(letra == 'd'){
      digitalWrite(buzzerA, HIGH);
      delay(barra);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(punto);
      digitalWrite(buzzerA, LOW);
      delay(wait);
      digitalWrite(buzzerA, HIGH);
      delay(punto);
      digitalWrite(buzzerA, LOW);
      delay(waitP);
    }
  }

  

  
}
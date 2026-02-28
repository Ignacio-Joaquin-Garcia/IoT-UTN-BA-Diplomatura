int ledR = 6;
int ledG = 5;
int ledB = 3;

int i;
int j;
bool ledBajo;

String msg1 = "Ingresa color a prender: ";


String color;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(msg1);
  while(Serial.available() == 0){};
  color = Serial.readString();

  if(color == "rojo"){
    analogWrite(ledR, 255);
    analogWrite(ledG, 0);
    analogWrite(ledB, 0);
  }
  if(color == "azul"){
    analogWrite(ledR, 0);
    analogWrite(ledG, 0);
    analogWrite(ledB, 255);
  }
  if(color == "verde"){
    analogWrite(ledR, 0);
    analogWrite(ledG, 255);
    analogWrite(ledB, 0);
  }
  if(color == "amarillo"){
    analogWrite(ledR, 255);
    analogWrite(ledG, 255);
    analogWrite(ledB, 0);
  }
  if(color == "violeta"){
    analogWrite(ledR, 255);
    analogWrite(ledG, 0);
    analogWrite(ledB, 255);
  }
  if(color == "blanco"){
    analogWrite(ledR, 255);
    analogWrite(ledG, 255);
    analogWrite(ledB, 255);
  }
  if(color == "arcoiris"){
    analogWrite(ledR, 0);
    analogWrite(ledG, 0);
    analogWrite(ledB, 0);
    for(i=1;i<=3;i++){
       j=0;
       ledBajo = true;
      while(ledBajo){
        if(i==1){analogWrite(ledR, j);}
        else if(i==2){analogWrite(ledG, j);}
        else if(i==3){analogWrite(ledB, j);}

        if(j == 255){ledBajo = false;}
        Serial.print("j: ");
        Serial.println(j);
        j = j+1;
        delay(50);
      }
      delay(80);
    }
    
  }

  
  

}

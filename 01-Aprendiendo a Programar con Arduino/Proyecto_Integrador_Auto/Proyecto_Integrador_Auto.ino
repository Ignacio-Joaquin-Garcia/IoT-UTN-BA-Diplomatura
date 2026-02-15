//Librerias
#include <IRremote.hpp>
#include <math.h>

//Declaracion Variables
//Puertos
byte portD = 0b11111000; //0-7
byte portB = 0b00011111; //8-13
byte portC = 0b00000000; //A0-A5
int numberOfSameComandos = 0;
uint16_t lastComando = -1;
int velocidadGeneral = 1;
unsigned long interruption;
unsigned int interruptionSpeed = 650;
//Leds
class CarLeds{
  private:
  	int leftBlinker;
  	int rightBlinker;
  	int lights;
  	int brakes;
  
  	
  public:
    CarLeds(int lB, int rB, int l, int b){
      leftBlinker = lB;
      rightBlinker = rB;
      lights = l;
      brakes = b;
    }
  	bool blinkInterruptionLeft = false;
  	bool blinkInterruptionRight = false;
  	int actualBlinks = 0;
  	int countBlinks;
    void lightsOn(){
      digitalWrite(lights, HIGH); 
    }
  	void lightsOff(){
      digitalWrite(lights, LOW); 
    }
    void brakesOn(){
      digitalWrite(brakes, HIGH);
    }
  	void brakesOff(){
      digitalWrite(brakes, LOW); 
    }
    void leftBlink(int numberBlink){
      blinkInterruptionLeft = true;
      blinkInterruptionRight = false;
      rightBlinkOff();
      countBlinks = numberBlink;
      actualBlinks = 0;
    }
  	void leftBlinkOn(){
      digitalWrite(leftBlinker, HIGH);
      actualBlinks++;
    }
  	void leftBlinkOff(){
      digitalWrite(leftBlinker, LOW);
      actualBlinks++;
    }
  	void rightBlink(int numberBlink){
      blinkInterruptionRight = true;
      blinkInterruptionLeft = false;
      leftBlinkOff();
      countBlinks = numberBlink;
      actualBlinks = 0;
    }
  	void rightBlinkOn(){
      digitalWrite(rightBlinker, HIGH);
      actualBlinks++;
    }
  	void rightBlinkOff(){
      digitalWrite(rightBlinker, LOW);
      actualBlinks++;
    }
};
CarLeds carLeds(11, 8, 3, 4);
int blinkNumber = 8;
//IRremote
const int RECV_PIN = 2;
IRsend irsend;
//Sensor Ultrasonico

//Servo

//Motores
class DCEngine{
  private:
  	int enable;
  	int powerPin;
  	int gndPin;
  public:
    DCEngine(int e, int p, int g){
      enable = e;
      powerPin = p;
      gndPin = g;
    }
    int isMotorOn(){
      return digitalRead(enable);
    }
    void motorOn(){
      digitalWrite(enable, HIGH);
    }
  	void motorOff(){
      digitalWrite(enable, LOW);
    }
    void moveForward(int velocidad){
      digitalWrite(enable, HIGH);
      analogWrite(powerPin, velocidad);
      digitalWrite(gndPin, LOW);
    }
  	void moveBackwards(int velocidad){
      digitalWrite(enable, HIGH);
      analogWrite(gndPin, velocidad);
      digitalWrite(powerPin, LOW);
    }
};
DCEngine motor1(7,5,6);
DCEngine motor2(12,10,9);


//Funciones Adicionales Motores
void moveForward(int velocidad){
  motor1.moveForward(velocidad);
  motor2.moveForward(velocidad);
}
void moveBackwards(int velocidad){
  motor1.moveBackwards(velocidad);
  motor2.moveBackwards(velocidad);
}
void moveRight(int velocidad){
  motor1.moveForward(velocidad);
  motor2.moveBackwards(velocidad / 2);
}
void moveLeft(int velocidad){
  motor2.moveForward(velocidad);
  motor1.moveBackwards(velocidad / 2);
}
void putMotorsOn(){
  motor1.motorOn();
  motor2.motorOn();
}
void putMotorsOff(){
  motor1.motorOff();
  motor2.motorOff();
}



void setup(){
  DDRD = portD;
  DDRB = portB;
  DDRC = portC;
  IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK);
  interruption = millis();
  Serial.begin(9600);
  Serial.println("Inicio");
  
}

void loop(){
  if(millis() >= interruption){
  	interruption += interruptionSpeed;
    generateInterruption();
  }
  if(IrReceiver.decode()){
    uint16_t comando = IrReceiver.decodedIRData.command; //HEX
    Serial.print("Comando: ");
    Serial.println(comando, HEX);
    if(numberOfSameComandos != 0){
      if(lastComando == comando){
        velocidadGeneral = (int) (130 * log10(numberOfSameComandos+10));
        if(velocidadGeneral > 255){
          velocidadGeneral = 255;
        }
      }else{
        numberOfSameComandos = 0;
        velocidadGeneral = 1;
      }
    }
    lastComando = comando;
    numberOfSameComandos = numberOfSameComandos +1;
    
    switch (comando){
      case 0x0: {//Prender/Apagar
        if(motor1.isMotorOn() || motor2.isMotorOn()){
          putMotorsOff();
          carLeds.lightsOff();
        }else{
          putMotorsOn();
          carLeds.lightsOn();
        }
      	break;
      }
      case 0x1: {//Adelante
      	moveForward(velocidadGeneral);
        carLeds.brakesOff();
      	break;
      }
      case 0x9: {//Atras
        moveBackwards(velocidadGeneral);
        carLeds.brakesOn();
      	break;
      }
      case 0x6: {//Derecha
        moveRight(velocidadGeneral);
        carLeds.brakesOff();
      	break;
      }
      case 0x4: {//Izquierda
        moveLeft(velocidadGeneral);
        carLeds.brakesOff();
      	break;
      }
      case 0x8: {//Intermitente Izquierda
        carLeds.leftBlink(blinkNumber);
      	break;
      }
      case 0xA: {//Intermitente Derecha
        carLeds.rightBlink(blinkNumber);
      	break;
      }
      default: {
      	break;
      }
    }
    delay(10);
    IrReceiver.resume();
  }
  
}



void logicBlinker(bool leftRight){
  if(leftRight){
    if((carLeds.actualBlinks % 2) == 0){
      carLeds.rightBlinkOn();
  	}else{
      carLeds.rightBlinkOff();
  	}
    if(carLeds.actualBlinks == carLeds.countBlinks){
      carLeds.rightBlinkOff();
      carLeds.blinkInterruptionRight = false;
    }
  } else{
    if((carLeds.actualBlinks % 2) == 0){
      carLeds.leftBlinkOn();
  	}else{
      carLeds.leftBlinkOff();
  	}
    if(carLeds.actualBlinks == carLeds.countBlinks){
      carLeds.leftBlinkOff();
      carLeds.blinkInterruptionLeft = false;
    }
  }
}

void generateInterruption(){
  Serial.println("Interrupcion ");
  if(carLeds.blinkInterruptionLeft){
    logicBlinker(false);
  }
  if(carLeds.blinkInterruptionRight){
    logicBlinker(true);
  }
}
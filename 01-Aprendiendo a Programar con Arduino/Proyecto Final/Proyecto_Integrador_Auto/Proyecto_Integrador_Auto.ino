//Librerias
#include <IRremote.hpp>
#include <Wire.h>
#include <math.h>

//Librerias Propias
#include "CarLeds.h"
#include "CarDistance.h"
#include "CarHorn.h"
#include "DCEngine.h"

//Declaracion Variables
//Puertos
byte portD = 0b11101000; //0-7
byte portB = 0b00011111; //8-13
byte portC = 0b00001000; //A0-A5
//Propias del Codigo
uint16_t comando;
uint16_t lastComando = -1;
int numberOfSameComandos = 0;
int velocidadGeneral = 1;
unsigned long interruption;
unsigned int interruptionSpeed = 650;
bool powerOn = false;
int blinkNumber = 8;
bool manualMode = false;
int gearShiftN = -1;
//Librerias
const int RECV_PIN = 2;
IRsend irsend;
//Clases Propias
DCEngine motor1(7,5,6);
DCEngine motor2(12,10,9);
CarDistance carDistance(8,4);
CarHorn carHorn(A3);
CarLeds carLeds;

void setup(){
  DDRD = portD;
  DDRB = portB;
  DDRC = portC;
  IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK);
  Wire.begin();
  carHorn.hornSoundOff();
  carLeds.begin();
  Serial.begin(9600);
  interruption = millis();
  Serial.println("Inicio");
}

void loop(){
  millisInterruption();
  infraredSensorRecieveCommand();
}

void serialEvent(){
  if(Serial.available()>0){
    String aux = Serial.readString();
    aux.trim();
    if(aux == "stop"){
      putMotorsOff(motor1, motor2);
    }
    if(aux == "start"){
      putMotorsOn(motor1, motor2);
    }
  }
}
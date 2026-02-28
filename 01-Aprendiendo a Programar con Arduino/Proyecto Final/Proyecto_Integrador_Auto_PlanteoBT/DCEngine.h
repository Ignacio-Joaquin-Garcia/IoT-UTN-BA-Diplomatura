#ifndef DCENGINE_H  
#define DCENGINE_H
#include <Arduino.h> 
#include "CarLeds.h"

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

void gearShiftManual(DCEngine &motor1, DCEngine &motor2, int gearShiftN);
void moveForward(CarLeds &carLeds, DCEngine &motor1, DCEngine &motor2, int velocidad, bool manualMode, int gearShiftN);
void moveBackwards(CarLeds &carLeds, DCEngine &motor1, DCEngine &motor2, int velocidad, bool manualMode, int gearShiftN);
void moveRight(CarLeds &carLeds, DCEngine &motor1, DCEngine &motor2, int velocidad);
void moveLeft(CarLeds &carLeds, DCEngine &motor1, DCEngine &motor2, int velocidad);
void putMotorsOn(DCEngine &motor1, DCEngine &motor2);
void putMotorsOff(DCEngine &motor1, DCEngine &motor2);

#endif
#include "DCEngine.h"

void gearShiftManual(DCEngine &motor1, DCEngine &motor2, int gearShiftN){
  switch (gearShiftN){
    case -1: {
      motor1.moveBackwards(200);
      motor2.moveBackwards(200);
      break;
    }
    case 0: {
      motor1.moveForward(0);
      motor2.moveForward(0);
      break;
    }
    case 1: {
      motor1.moveForward(100);
      motor2.moveForward(100);
      break;
    }
    case 2: {
      motor1.moveForward(180);
      motor2.moveForward(180);
      break;
    }
    case 3: {
      motor1.moveForward(255);
      motor2.moveForward(255);
      break;
    }
  }
}
void moveForward(CarLeds &carLeds, DCEngine &motor1, DCEngine &motor2, int velocidad, bool manualMode, int gearShiftN){
  if(manualMode){
    gearShiftManual(motor1, motor2, gearShiftN);
  } else{
    motor1.moveForward(velocidad);
  	motor2.moveForward(velocidad);
  }
  carLeds.brakesOff();
}
void moveBackwards(CarLeds &carLeds, DCEngine &motor1, DCEngine &motor2, int velocidad, bool manualMode, int gearShiftN){
  if(manualMode){
    gearShiftManual(motor1, motor2, gearShiftN);
  } else{
    motor1.moveBackwards(velocidad);
  	motor2.moveBackwards(velocidad);
  }
  carLeds.brakesOn();
}
void moveRight(CarLeds &carLeds, DCEngine &motor1, DCEngine &motor2, int velocidad){
  motor1.moveForward(velocidad);
  motor2.moveBackwards(velocidad / 2);
  carLeds.brakesOff();
}
void moveLeft(CarLeds &carLeds, DCEngine &motor1, DCEngine &motor2, int velocidad){
  motor1.moveBackwards(velocidad / 2);
  motor2.moveForward(velocidad);
  carLeds.brakesOff();
}
void putMotorsOn(DCEngine &motor1, DCEngine &motor2){
  motor1.motorOn();
  motor2.motorOn();
}
void putMotorsOff(DCEngine &motor1, DCEngine &motor2){
  motor1.motorOff();
  motor2.motorOff();
}
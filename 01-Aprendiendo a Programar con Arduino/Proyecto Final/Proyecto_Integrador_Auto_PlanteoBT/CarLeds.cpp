#include "CarLeds.h"

void logicBlinker(CarLeds &carLeds, bool leftRight){
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
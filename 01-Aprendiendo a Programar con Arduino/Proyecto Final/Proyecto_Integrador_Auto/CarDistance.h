#ifndef CARDISTANCE_H
#define CARDISTANCE_H  
#include <Arduino.h> 
#include "CarHorn.h"

class CarDistance{
  private:
  	int triggerPin;
  	int echoPin;
  public:
    CarDistance(int t, int e){
      triggerPin = t;
      echoPin = e;
    };
    long getDistance(){
      //Trigger
      digitalWrite(triggerPin, LOW);
      delayMicroseconds(2);
      digitalWrite(triggerPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(triggerPin, LOW);
      //Echo
      long duration = pulseIn(echoPin, HIGH, 30000);
      //Math
      if(duration == 0) return -1;
      long distance = (duration / 58);
      return distance; 
    }
};

void checkObstacles(CarDistance carDistance, CarHorn carHorn);

#endif
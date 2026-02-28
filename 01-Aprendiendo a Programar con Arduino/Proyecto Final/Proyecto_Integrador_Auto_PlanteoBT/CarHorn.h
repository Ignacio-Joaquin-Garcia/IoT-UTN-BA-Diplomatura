#ifndef CARHORN_H  
#define CARHORN_H  
#include <Arduino.h> 

class CarHorn{
  private:
  	int pinBuzzer;
  public:
  	CarHorn(int b){
      pinBuzzer = b;
  	}
  	bool carHorning = false;
    void hornSoundOn(){
      digitalWrite(pinBuzzer, HIGH);
    }
  	void hornSoundOff(){
      digitalWrite(pinBuzzer, LOW);
    }
    void horn(){
      if(digitalRead(pinBuzzer)){
        hornSoundOff();
        carHorning = false;
      } else{
        hornSoundOn();
        carHorning = true;
      }
    }
};

#endif
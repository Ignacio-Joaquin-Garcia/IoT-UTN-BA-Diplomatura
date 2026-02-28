#ifndef CARLEDS_H  
#define CARLEDS_H
#include <Arduino.h> 
#include <Wire.h>
//Leds
class CarLeds{
  private:
  	byte ledPins = 0b00000000;
  public:
    CarLeds(){ }
    void begin(){
      sendToPCF(ledPins);
    }
    void sendToPCF(byte ledPinsP){
      Wire.beginTransmission(0x20); 
      Wire.write(ledPinsP);    
      Wire.endTransmission();
    }
  	bool blinkInterruptionLeft = false;
  	bool blinkInterruptionRight = false;
  	int actualBlinks = 0;
  	int countBlinks;
    void lightsOn(){
      bitSet(ledPins, 2);
      sendToPCF(ledPins);
    }
  	void lightsOff(){
      bitClear(ledPins, 2);
      sendToPCF(ledPins);
    }
    void brakesOn(){
      bitSet(ledPins, 1);
      sendToPCF(ledPins);
    }
  	void brakesOff(){
      bitClear(ledPins, 1);
      sendToPCF(ledPins);
    }
    void leftBlink(int numberBlink){
      blinkInterruptionLeft = true;
      blinkInterruptionRight = false;
      rightBlinkOff();
      countBlinks = numberBlink;
      actualBlinks = 0;
    }
  	void leftBlinkOn(){
      bitSet(ledPins, 0);
      sendToPCF(ledPins);
      actualBlinks++;
    }
  	void leftBlinkOff(){
      bitClear(ledPins, 0);
      sendToPCF(ledPins);
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
      bitSet(ledPins, 3);
      sendToPCF(ledPins);
      actualBlinks++;
    }
  	void rightBlinkOff(){
      bitClear(ledPins, 3);
      sendToPCF(ledPins);
      actualBlinks++;
    }
    void noMoveAllowed(){
      for(int i = 0; i<3; i++){
        lightsOn();
        brakesOn();
        delay(250);
        lightsOff();
        brakesOff();
        delay(250);
      }
    }
};

void logicBlinker(CarLeds &carLeds, bool leftRight);

#endif
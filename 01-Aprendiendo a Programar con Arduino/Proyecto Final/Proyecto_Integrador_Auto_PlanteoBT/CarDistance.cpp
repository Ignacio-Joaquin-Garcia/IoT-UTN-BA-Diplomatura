#include "CarDistance.h"

void checkObstacles(CarDistance carDistance, CarHorn carHorn){
  long distance = carDistance.getDistance();
  if((distance >= 80) && (distance < 130)){
    carHorn.hornSoundOn();
    delay(2);
    carHorn.hornSoundOff();
  } else if(distance < 80){
    carHorn.hornSoundOn();
  } else if(!carHorn.carHorning){
    carHorn.hornSoundOff();
  }
};
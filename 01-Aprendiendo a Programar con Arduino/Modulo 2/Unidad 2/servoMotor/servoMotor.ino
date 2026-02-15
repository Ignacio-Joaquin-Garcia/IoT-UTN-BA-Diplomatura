#include <Servo.h>
Servo miServoMotor;

void setup() {
  miServoMotor.attach(3);
}

void loop() {
  /*
  for(int i = 0; i<180;i++){
    miServoMotor.write(i);
    delay(200);
  }
*/
  
  miServoMotor.write(90);
  delay(2000);
  miServoMotor.write(180);
  delay(2000);
  miServoMotor.write(0);
  delay(2000);
  
}

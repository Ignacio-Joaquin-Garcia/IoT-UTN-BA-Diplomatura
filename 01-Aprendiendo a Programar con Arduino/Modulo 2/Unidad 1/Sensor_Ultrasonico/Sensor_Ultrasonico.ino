#include <NewPing.h>
#define ECHO_PIN 7
#define TRIGGER_PIN 8
#define MAX_DISTANCE 500

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

unsigned int pingSpeed = 50;
unsigned long pingTimer;

void setup() {
  pingTimer = millis();
  Serial.begin(9600);
}

void loop() {
  if(millis() >= pingTimer){
    pingTimer += pingSpeed;
    sonar.ping_timer(echoCheck);
  }

}

void echoCheck(){
  if(sonar.check_timer()){
    Serial.println(sonar.ping_result / US_ROUNDTRIP_CM);
  }
}

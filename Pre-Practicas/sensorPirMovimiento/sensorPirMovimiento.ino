int pirSensor = 7;
int pinLed = 2;

void setup(){
	pinMode(pirSensor, INPUT);
  pinMode(pinLed, OUTPUT);
	for(int i = 0; i<80;i++){
		digitalWrite(pinLed, HIGH);
		delay(500);
		digitalWrite(pinLed, LOW);
		delay(500);
	}
}
void loop(){
	bool motion = digitalRead(pirSensor);
	if(motion){
		digitalWrite(pinLed, HIGH);
		delay(100);
		digitalWrite(pinLed, LOW);
	}
}

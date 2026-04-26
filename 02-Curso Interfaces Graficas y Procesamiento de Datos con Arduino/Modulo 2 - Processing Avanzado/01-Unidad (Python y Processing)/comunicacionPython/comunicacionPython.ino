int x;
void setup(){
	Serial.begin(9600);
	Serial.setTimeout(100);
}
void loop(){
	while(!Serial.available());
	x = Serial.readStringUntil('\n').toInt();
	Serial.print(x + 1);
}
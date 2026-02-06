int entradaBoton = 7;
int salidaLed = 8;
void setup(){
	pinMode(entradaBoton, INPUT);
	pinMode(salidaLed, OUTPUT);
  	Serial.begin(9600);
}

void loop(){
 	int valorEntrada = digitalRead(entradaBoton);
  	//Serial.println(valorEntrada);
	digitalWrite(salidaLed, valorEntrada);
}
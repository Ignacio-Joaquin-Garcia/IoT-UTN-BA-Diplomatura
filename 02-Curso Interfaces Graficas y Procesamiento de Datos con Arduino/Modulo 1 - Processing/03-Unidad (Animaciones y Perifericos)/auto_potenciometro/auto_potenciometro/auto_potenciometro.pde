Auto miAuto;
import processing.serial.*;
Serial puerto;
String data = "511";
void setup(){
  size(1000, 1000);
  miAuto = new Auto(500, 500, 300);
  println(Serial.list()[0]);
  puerto = new Serial(this, Serial.list()[1], 9600);
}
void draw(){
  background(255);
  if(puerto.available() > 0){
    data = puerto.readStringUntil('\n');
    if(data != null){
      data = trim(data);
    }
  }
  println(data);
  miAuto.dibujarAuto(int(data));
  
}

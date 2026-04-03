Auto miAuto;
void setup(){
  size(1000, 1000);
  miAuto = new Auto(500, 500, 300);
  
}
void draw(){
  background(255);
  miAuto.dibujarAuto(511);
}

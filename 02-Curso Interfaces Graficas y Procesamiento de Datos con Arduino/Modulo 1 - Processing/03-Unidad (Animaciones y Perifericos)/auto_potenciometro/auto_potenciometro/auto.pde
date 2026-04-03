class Auto{
  int x;
  int y;
  
  int tamAut;
  int actualX;
  int v;
  
  PShape formaAuto;
  
  Auto(int x, int y, int tamAut){
    this.x = x;
    this.y = y;
    this.tamAut = tamAut;
    crearFormaAuto();
  }
  
  void crearFormaAuto(){
    formaAuto = createShape();
    formaAuto.beginShape();
    formaAuto.fill(0, 200, 0);
    formaAuto.vertex(0,0);
    formaAuto.vertex(50,-50);
    formaAuto.vertex(100,-100);
    formaAuto.vertex(200,-100);
    formaAuto.vertex(250,-50);
    formaAuto.vertex(tamAut,0);
    formaAuto.endShape(CLOSE);
  }
  void dibujarAuto(int v){
    float mapV = map(v, 0, 1023, -2, 2);  
    actualX += mapV;
    pushMatrix();
    translate(x - tamAut/2, y);
    shape(formaAuto, actualX, 0);
    popMatrix();
  }
  
}

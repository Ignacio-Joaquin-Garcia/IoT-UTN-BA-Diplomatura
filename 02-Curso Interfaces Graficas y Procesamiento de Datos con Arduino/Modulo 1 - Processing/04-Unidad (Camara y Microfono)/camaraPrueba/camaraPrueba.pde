import processing.video.*;

Capture cam;

void setup(){
  size(640, 480);
  
  String[] camaras = Capture.list();
  if(camaras.length == 0){
    println("No se encontraron camaras");
    exit();
  } else{
    println("Camaras Disponibles: ");
    for(int i = 0; i < camaras.length; i++){
      println(camaras[i]);
    }
    cam = new Capture(this, camaras[1]);
    cam.start();
  }
}

void draw(){
  if(cam.available() == true){
    cam.read();
  }
  image(cam, 0, 0);
}

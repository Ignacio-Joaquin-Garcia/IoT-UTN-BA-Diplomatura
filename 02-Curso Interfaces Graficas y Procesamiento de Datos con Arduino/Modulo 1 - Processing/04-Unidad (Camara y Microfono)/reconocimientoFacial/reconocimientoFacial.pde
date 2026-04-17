import gab.opencv.*;
import processing.video.*;
import java.awt.Rectangle;
import processing.serial.*;

Serial miPuerto;
String datoLeidoConEvento;
int lf = 10; // \n es 10

Capture video;
OpenCV opencv;

void setup() {
  String[] camaras = Capture.list();
  size(1080, 720);
  
  video = new Capture(this, camaras[1]);
  opencv = new OpenCV(this, 640, 480);
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);
  
  video.start();
  printArray(Serial.list());
  miPuerto = new Serial(this, Serial.list()[0], 9600);
}

void draw() {
  scale(2);
  opencv.loadImage(video);
  image(video, 0, 0);
  stroke(#FF0080);
  strokeWeight(3);

  Rectangle[] faces = opencv.detect();
  println(faces.length);

  for (int i = 0; i < faces.length; i++) {

    String mensaje = "";
    mensaje = str(faces[i].x);
    mensaje += ",";
    mensaje += str(faces[i].y);
    mensaje += "\n";
    miPuerto.write(mensaje);

    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height);

    mensaje = "";
  }
}

void serialEvent(Serial p)
{
  datoLeidoConEvento = p.readStringUntil(lf);
  println(datoLeidoConEvento);
}

void captureEvent(Capture c) {
  c.read();
}

//Modifcar cada pixel para que se reproduzca en base a su luminosidad
import processing.video.*;
int escalaDelVideo = 10;
int colum, fil;

Capture video;
String[] camaras;

void setup(){
  size(640, 480);
  colum = width / escalaDelVideo;
  fil = height / escalaDelVideo;
  camaras = Capture.list();
  video = new Capture(this, camaras[1]);
  video.start();
}

void captureEvent(Capture video){
  video.read();
}

void draw(){
  background(0);
  video.loadPixels();
  for(int i = 0; i < colum; i++){
    for(int j = 0; j < fil; j++){
      int x = i*escalaDelVideo;
      int y = j*escalaDelVideo;
      
      int loc = (video.width - x - 1) + y * video.width;
      
      color c = video.pixels[loc];
      float sz = (brightness(c) / 200) * escalaDelVideo;
      
      rectMode(CENTER);
      fill(c);
      noStroke();
      rect(x + escalaDelVideo / 2, y + escalaDelVideo / 2, sz, sz);
    }
  }
}

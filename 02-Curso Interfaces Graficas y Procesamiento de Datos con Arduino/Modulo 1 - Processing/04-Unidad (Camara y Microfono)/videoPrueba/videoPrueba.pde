import processing.video.*;
Movie myMovie;

void setup(){
  size(1920, 1080);
  myMovie = new Movie(this, "ejemVideo.mp4");
  myMovie.loop();
}
void draw(){
  tint(255, 20);
  image(myMovie, mouseX, mouseY);
}

void movieEvent(Movie m){
  m.read();
}

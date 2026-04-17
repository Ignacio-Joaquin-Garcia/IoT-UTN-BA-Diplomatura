import processing.sound.*;
AudioIn in;
Amplitude amp;
float volume = 0;

void setup(){
  size(640, 360);
  background(255);
  
  //Create the input stream
  in = new AudioIn(this, 0);
  println(in);
  amp = new Amplitude(this);
  in.play();
  amp.input(in);
}

void draw(){
  in.amp(volume);
  println(amp.analyze());
}

void keyPressed(){
  if(key == 'm'){
    if(volume < 1){
      volume+=0.1;
    }
  }
  if(key == 'l'){
    if(volume > 0){
      volume-=0.1;
    }
  }
}

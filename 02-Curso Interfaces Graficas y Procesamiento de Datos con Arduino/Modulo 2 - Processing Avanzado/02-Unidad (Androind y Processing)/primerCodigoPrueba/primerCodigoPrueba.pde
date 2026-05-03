String texto = "Bienvenidos";
void setup(){

}
void draw(){
  fill(0);
  rect(0, 0, width, height);
  if(mousePressed){
    fill(255, 0, 0);
    texto = "Tecla Presionada";
    rect(width / 2, height / 2, 200, 200); 
  } else{
    fill(0, 255, 0);
    texto = "Bienvenidos";
    ellipse(width / 2, height / 2, 100, 100);
  }
  textSize(128);
  text(texto, 0, 150);
}

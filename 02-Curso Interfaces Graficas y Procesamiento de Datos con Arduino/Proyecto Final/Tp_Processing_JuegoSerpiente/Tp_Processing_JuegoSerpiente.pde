//Librerias

//Constantes
final Direccion ARRIBA = new Direccion(0, -1);
final Direccion ABAJO = new Direccion(0, 1);
final Direccion IZQUIERDA = new Direccion(-1, 0);
final Direccion DERECHA = new Direccion(1, 0);
//Elementos del Juego
KeyboardController input = new KeyboardController();
Juego snakeGame;


void setup(){
  size(800, 600);
  background(0);
  snakeGame = new Juego(10, 10, 1000, input);
}
void draw(){
  snakeGame.update();
  snakeGame.render();
  
}
//Registros de Tecla
void keyPressed(){
  input.registrarTecla(key, keyCode);
}
void mousePressed(){
  input.registrarClick(mouseX, mouseY);  
}

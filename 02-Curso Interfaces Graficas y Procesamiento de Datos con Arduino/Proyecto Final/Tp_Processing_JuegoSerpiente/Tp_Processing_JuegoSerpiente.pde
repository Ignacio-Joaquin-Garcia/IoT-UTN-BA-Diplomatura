//Sonido
import processing.sound.*;
SoundProvider sonido;
//Serial
import processing.serial.*;
Serial miPuerto;
String mensajeSerial;
int lf = 10;

//Constantes
final Direccion ARRIBA = new Direccion(0, -1);
final Direccion ABAJO = new Direccion(0, 1);
final Direccion IZQUIERDA = new Direccion(-1, 0);
final Direccion DERECHA = new Direccion(1, 0);
//Elementos del Juego
KeyboardController inputK = new KeyboardController();
ArduinoController inputA = new ArduinoController();
Juego snakeGame;

//Sonido



void setup(){
  size(800, 600);
  background(0);
  sonido = new SoundProvider(this);
  snakeGame = new Juego(10, 10, 1000, inputK, inputA, sonido);
  printArray(Serial.list());
  miPuerto = new Serial(this, Serial.list()[1], 9600);
  miPuerto.clear();
  miPuerto.bufferUntil('\n');
}
void draw(){
  snakeGame.update();
  snakeGame.render();
  snakeGame.sonido();
}
//Registros de Tecla
void keyPressed(){
  inputK.registrarTecla(key, keyCode);
}
void mousePressed(){
  inputK.registrarClick(mouseX, mouseY);  
}

//Serial
void serialEvent(Serial p){
  mensajeSerial = p.readStringUntil(lf);
  if(mensajeSerial != null){
    if(mensajeSerial.contains("%")){
      mensajeSerial = trim(mensajeSerial);
      int x = int(mensajeSerial.substring(0, mensajeSerial.indexOf("%")));
      String restoMensaje = mensajeSerial.substring(mensajeSerial.indexOf("%")+1);
      int y = int(restoMensaje.substring(0, restoMensaje.indexOf("%")));
      restoMensaje = restoMensaje.substring(restoMensaje.indexOf("%")+1);
      int z = int(restoMensaje.substring(0));
      println("x: " + x + ", y: " + y + ", z: " + z);
      inputA.registrarDireccion(x, y, z);
    }
  }
}

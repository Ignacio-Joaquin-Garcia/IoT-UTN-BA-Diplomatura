#include <Keypad.h>
const byte filas = 4;
const byte columnas = 4;
char matrizTeclado[filas][columnas] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};
byte filasPines[filas] = {11,10,9,8};
byte columnaPines[columnas] = {7,6,5,4};
Keypad teclado = Keypad(makeKeymap(matrizTeclado), filasPines, columnaPines, filas, columnas);

void setup() {
  Serial.begin(9600);

}

void loop() {
  char teclaLeida = teclado.getKey();
  if(teclaLeida != NO_KEY){
    Serial.println(teclaLeida);
  }
  KeyState estadoTecla = teclado.getState();
}

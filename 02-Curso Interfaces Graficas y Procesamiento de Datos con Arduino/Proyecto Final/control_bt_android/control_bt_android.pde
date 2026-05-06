//Librerias
import ketai.sensors.*;
import ketai.net.bluetooth.*;
import ketai.ui.*;
//Objetos
KetaiSensor sensor;
KetaiBluetooth BT;
ArrayList listaDispositivos;
String nombreDispositivo;
long delayEntreMensaje = 0;
float accelerometerX, accelerometerY, accelerometerZ;


void setup(){
  fullScreen();
  sensor = new KetaiSensor(this);
  sensor.start();
  textAlign(CENTER, CENTER);
  textSize(displayDensity * 36);
  fullScreen();
  orientation(PORTRAIT);

  BT = new KetaiBluetooth(this);
  listaDispositivos = BT.getPairedDeviceNames();
  printArray(listaDispositivos);
  listaDispositivos.add("Cancelar");
}
void draw(){
  comunicar();
}
void onAccelerometerEvent(float x, float y, float z){
  accelerometerX = x;
  accelerometerY = y;
  accelerometerZ = z;
}

void comunicar() {
  if (nombreDispositivo != null) {
    if (millis() > delayEntreMensaje + 50) {
      String Mensaje = int(accelerometerX) + "%" + int(accelerometerY) + "%" + int(accelerometerZ) + "\n";
      BT.writeToDeviceName(nombreDispositivo, Mensaje.getBytes());
      delayEntreMensaje = millis();
    }
  }
}

void mousePressed() {
  println("Conectar BT");
  KetaiList MenuBluetooth = new KetaiList(this, listaDispositivos);
}

void onKetaiListSelection(KetaiList Klist) {
  String btSeleccionado = Klist.getSelection();
  println("Conectado a: "+ btSeleccionado);
  if (btSeleccionado.equals("Cancelar")) {
    println("Seleccion cancelada");
  } else {
    nombreDispositivo = btSeleccionado;
    BT.connectToDeviceByName(nombreDispositivo);
  }
}

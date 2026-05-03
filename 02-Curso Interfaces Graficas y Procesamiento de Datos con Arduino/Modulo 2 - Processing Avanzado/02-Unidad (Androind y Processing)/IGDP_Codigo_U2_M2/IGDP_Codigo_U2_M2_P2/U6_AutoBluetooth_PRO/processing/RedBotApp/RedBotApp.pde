import ketai.sensors.*;
import ketai.net.bluetooth.*;
import ketai.ui.*;

KetaiSensor sensor;
KetaiBluetooth BT;
ArrayList listaDispositivos;
String nombreDispositivo;
long delayEntreMensaje = 0;

float px,py;
float AreaX, AreaY;
float sx, sy;
boolean ModoAcelerometro = false;

void setup() {
  fullScreen();
  orientation(PORTRAIT);
  px = 0;
  py = 0;
  sensor = new KetaiSensor(this);
  sensor.start();
  BT = new KetaiBluetooth(this);
  listaDispositivos = BT.getPairedDeviceNames();
  printArray(listaDispositivos);
  listaDispositivos.add("Cancelar");
}

void draw() {
  actualizar();
  comunicar();
}

void comunicar() {
  if (nombreDispositivo != null) {
    if (millis() > delayEntreMensaje + 50) {
      String Mensaje = "X/"+px+"\n";
      BT.writeToDeviceName(nombreDispositivo, Mensaje.getBytes());
      Mensaje = "Y/"+py+"\n";
      BT.writeToDeviceName(nombreDispositivo, Mensaje.getBytes());
      delayEntreMensaje = millis();
    }
  }
}

void actualizar() {
  px = map(sx, -10, 10, -100, 100);
  py = map(sy, -10, 10, -100, 100);
  px = constrain(px, -100, 100);
  py = constrain(py, -100, 100);
}

void mousePressed() {
  println("Conectar BT");
  KetaiList MenuBluetooth = new KetaiList(this, listaDispositivos);
}

void onAccelerometerEvent(float x, float y, float z) {
  sx = -x;
  sy = y;
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

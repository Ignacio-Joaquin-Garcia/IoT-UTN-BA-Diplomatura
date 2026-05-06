class SoundEvent {
  float freq;
  float amp;
  int duration; 

  SoundEvent(float f, float a, int d) {
    freq = f;
    amp = a;
    duration = d;
  }
}

class SoundProvider{
  TriOsc osc;
  PApplet app;
  
  boolean sonando = false;
  int tiempoInicio = 0;
  int delay = 50;
  
  ArrayList<SoundEvent> sonidosAEjecutar;
  SoundEvent sonidoActual;

  SoundProvider(PApplet app) {
    this.app = app;
    osc = new TriOsc(app);
    sonidosAEjecutar = new ArrayList();
  }
  
  void inicio() {
    agregar(400, 0.5, 180);
    agregar(650, 0.5, 180);
    agregar(550, 0.5, 180);
    agregar(900, 0.6, 220);
  }
  void comer(int puntaje) {
    float base = 800 + puntaje * 100;
    agregar(base, 0.7, 40);
    agregar(base + 300, 0.7, 40);
  }
  void pausa() {
    agregar(500, 0.4, 80);
    agregar(300, 0.4, 120);
  }
  void muerte(){
    agregar(600, 0.6, 100);
    agregar(400, 0.6, 120);
    agregar(250, 0.5, 150);
    agregar(120, 0.5, 300);
  }
  void resume() {
    agregar(500, 0.5, 60);
    agregar(800, 0.6, 60);
    agregar(1100, 0.7, 80);
  }
  
  void agregar(float f, float a, int d) {
    sonidosAEjecutar.add(new SoundEvent(f, a, d));
  }
  
  void update() {
    if (!sonando && sonidosAEjecutar.size() > 0) {
      sonidoActual = sonidosAEjecutar.remove(0);

      osc.freq(sonidoActual.freq);
      osc.amp(sonidoActual.amp);
      osc.play();

      tiempoInicio = millis();
      sonando = true;
    }

    if (sonando && millis() - tiempoInicio > sonidoActual.duration) {
      osc.stop();
      sonando = false;
    }
  }
}

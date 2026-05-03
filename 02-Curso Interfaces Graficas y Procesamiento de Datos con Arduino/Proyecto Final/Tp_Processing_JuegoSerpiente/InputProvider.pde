interface InputProvider{
  Direccion obtenerDireccion();
  boolean inicioSolicitado();
  Posicion obtenerClick();
  boolean mouseEnBoton(int x, int y, int ancho, int alto);
}

class KeyboardController implements InputProvider {
  private Direccion direccionPendiente = null;
  private Posicion posicionPendiente = null;
  private boolean start = false;
  
  // Se llama desde keyPressed()
  void registrarTecla(char k, int kCode) {
    if (k == 'w') direccionPendiente = ARRIBA;
    if (k == 'a') direccionPendiente = IZQUIERDA;
    if (k == 's') direccionPendiente = ABAJO;
    if (k == 'd') direccionPendiente = DERECHA;

    if (kCode == ENTER || kCode == RETURN) {
      start = true;
    }
  }
  // El juego la consume (y se limpia)
  public Direccion obtenerDireccion() {
    Direccion d = direccionPendiente;
    direccionPendiente = null; 
    return d;
  }
  
  void registrarClick(int mouseX, int mouseY){
    posicionPendiente = new Posicion(mouseX, mouseY);
  }
  public Posicion obtenerClick(){
    Posicion p = posicionPendiente;
    posicionPendiente = null;
    return p;
  }
  public boolean mouseEnBoton(int x, int y, int ancho, int alto){
    Posicion posClick = obtenerClick();
    if(posClick == null){ return false; };
    return (posClick.x >= x && posClick.x <= x + ancho && posClick.y >= y && posClick.y <= y + alto);
  }
  
  public boolean inicioSolicitado() {
    if (start) {
      start = false; // consumir evento
      return true;
    }
    return false;
  }
}

class Serpiente implements Renderable{
  //Atributos Logica
  private ArrayList<Posicion> segmentos;
  private Direccion direccionActual;
  private boolean crecerPendiente = false; //Si es true no borra cola
  
  //Atributos Render
  int tamCelda;
  PImage imgCabeza;
  
  Serpiente(Direccion direccionActual, int ancho, int alto, int tamCelda){
    //Atributos Logica
    this.direccionActual = direccionActual;
    segmentos = new ArrayList<Posicion>();
    //Cabeza siempre va a ser el ultimo elemento
    Posicion cola = new Posicion(ancho/2-1, alto/2);
    Posicion cabeza = new Posicion(ancho/2, alto/2);
    segmentos.add(0, cola);
    segmentos.add(1, cabeza);
    
    //Atributos Render
    this.tamCelda = tamCelda;
    imgCabeza = loadImage("cabeza.png");
  };
  
  Posicion obtenerCabeza(){
    return segmentos.get(segmentos.size()-1);
  }
  
  void mover(){
    Posicion cabeza = obtenerCabeza();
    Posicion nuevaCabeza = new Posicion(cabeza.x + direccionActual.dx, cabeza.y + direccionActual.dy);
    segmentos.add(nuevaCabeza);
    if(!crecerPendiente){
      segmentos.remove(0);  
    }
    crecerPendiente = false;
  };
  
  void cambiarDireccion(Direccion nuevaDireccion){
    if(nuevaDireccion == null){ return; };
    if(!nuevaDireccion.esOpuesta(direccionActual)){
      direccionActual = nuevaDireccion;
    }
  }
  
  boolean seMuerde(){
    Posicion cabeza = obtenerCabeza();
    for(int i = 0; i < segmentos.size()-1; i++){
      if(cabeza.equals(segmentos.get(i))){
        return true;  
      }
    }
    return false;
  }
  
  void crecer(){
    crecerPendiente = true;
  }
  
  boolean contiene(Posicion p){
    for(int i = 0; i < segmentos.size(); i++){
      if(segmentos.get(i).equals(p)){
        return true;  
      }  
    };
    return false;
  }
  
  ArrayList<Posicion> obtenerSegmentos(){
    return segmentos;
  }
  
  void reset(Tablero tablero){
    segmentos.clear();
    Posicion cola = new Posicion(tablero.ancho/2-1, tablero.alto/2);
    Posicion cabeza = new Posicion(tablero.ancho/2, tablero.alto/2);
    segmentos.add(0, cola);
    segmentos.add(1, cabeza);
  }
  
  int margen = 4;
  int radio = 4;
  void render(){
    for(int i = 0; i < segmentos.size(); i++){
      int pixelX =  segmentos.get(i).x * tamCelda;
      int pixelY =  segmentos.get(i).y * tamCelda;
      if(i == segmentos.size()-1){
        pushMatrix();
        translate(pixelX + tamCelda/2, pixelY + tamCelda/2);  // centro de la celda
        if(direccionActual == DERECHA){
          rotate(radians(-90));
        }
        if(direccionActual == ABAJO){
          rotate(radians(0));
        }
        if(direccionActual == IZQUIERDA){
          rotate(radians(90));
        }
        if(direccionActual == ARRIBA){
          rotate(radians(180));
        }
        image(imgCabeza, -tamCelda/2, -tamCelda/2, tamCelda, tamCelda);
        popMatrix();
        
      }else{
        fill(50, 210, 50);
        rect(pixelX+margen, pixelY+margen, tamCelda-margen*2, tamCelda-margen*2, radio);
      }
    }
  }
  
}

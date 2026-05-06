class Tablero implements Renderable{
  int ancho;
  int alto;
  int tamCelda;  
  
  Tablero(int ancho, int alto, int tamCelda){
    this.ancho = ancho;
    this.alto = alto;
    this.tamCelda = tamCelda;
  }
  
  boolean esPosicionValida(Posicion p){
    if(p.x < 0 || p.x >= ancho){
      return false;
    }
    if(p.y < 0 || p.y >= alto){
      return false; 
    }
    return true;
  }
  
  int margen = 2;
  int radio = 5;
  void render(){
    noStroke();
    fill(#65366C);
    rect(0, 0, ancho * tamCelda, alto * tamCelda, 5);
    fill(#E4CCE8);
    for(int i = 0; i < alto; i++){
      for(int j = 0; j < ancho; j++){
        int pixelX =  j * tamCelda;
        int pixelY =  i * tamCelda;
        
        rect(pixelX + margen, pixelY + margen, tamCelda - margen*2, tamCelda - margen*2, radio);
        
      }
    }
      
    
  }
}

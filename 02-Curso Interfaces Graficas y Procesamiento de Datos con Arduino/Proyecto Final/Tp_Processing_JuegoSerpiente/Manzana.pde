class Manzana implements Renderable{
  //Atributos Logica
  private Posicion posicionManzana;
  
  //Atributos Render
  int tamCelda;
  PImage imgManzana;
  
  Manzana(int ancho, int alto, Serpiente s, int tamCelda){
    //Atributos Logica
    reposicionar(ancho, alto, s);
    //Atributos Render
    this.tamCelda = tamCelda;
    imgManzana = loadImage("manzana.png");
  }
  
  Posicion obtenerPosicion(){
    return posicionManzana;
  }
  
  void reposicionar(int ancho, int alto, Serpiente s){
    do {
      int x = (int) random(ancho);
      int y = (int) random(alto);
      posicionManzana = new Posicion(x, y);
    } while (s.contiene(posicionManzana));
  }
  
  void render(){
    int pixelX =  posicionManzana.x * tamCelda;
    int pixelY =  posicionManzana.y * tamCelda;
      
    image(imgManzana, pixelX, pixelY, tamCelda, tamCelda);
  }
}

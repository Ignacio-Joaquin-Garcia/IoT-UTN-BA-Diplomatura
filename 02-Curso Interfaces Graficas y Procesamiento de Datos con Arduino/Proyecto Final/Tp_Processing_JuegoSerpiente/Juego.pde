enum EstadoJuego {
    INICIO, JUGANDO, FINALIZADO, PAUSADO 
};

class Juego implements Renderable{
  //Variables de Logica
  Tablero tablero;
  Serpiente serpiente;
  Manzana manzana;
  
  EstadoJuego estado;
  int puntaje = 0;
  int tickRate;
  int tiempoUpdate = 0;
  
  double tiempoComienzoJuego = -1;
  double tiempoFinalJuego = -1;
  double tiempoTotalJuego = -1;
  
  InputProvider input;
  
  //Render
  int tamCelda;
  int offsetX;
  int offsetY;
  
  PFont fontTitulos;
  PFont fontTexto;
  float offsetTitulos = 0;
  PGraphics fondo;
  PGraphics fondoPausa;
  PImage imgPausa;
  
  //Constructor
  Juego(int ancho, int alto, int tickRate, InputProvider input){
    tamCelda = width / ancho - 50;
    offsetX = (width - tamCelda * ancho) / 2;
    offsetY = (height - tamCelda * alto) / 2;
    this.tablero = new Tablero(ancho, alto, tamCelda);
    this.serpiente = new Serpiente(DERECHA, ancho, alto, tamCelda);
    this.manzana = new Manzana(ancho, alto, serpiente, tamCelda);
    
    this.estado = EstadoJuego.INICIO;
    this.tickRate = tickRate;
    
    this.input = input;
    
    //Render
    fontTitulos = createFont("Sofia-Regular.ttf", 48);
    fontTexto = createFont("Calibri-Light-48", 32);
    fondo = createGraphics(width, height);
    fondo.beginDraw();
    for (int y = 0; y < height; y++) {
      float t = map(y, 0, height, 0, 1);
      color c = lerpColor(color(40,0,60), color(80,0,60), t);
      fondo.stroke(c);
      fondo.line(0, y, width, y);
    }
    fondo.endDraw();
    fondoPausa = createGraphics(width, height);
    fondoPausa.beginDraw();
    for (int y = 0; y < height; y++) {
      float t = map(y, 0, height, 0, 1);
      color c = lerpColor(color(80,0,60), color(40,0,60), t);
      fondoPausa.stroke(c);
      fondoPausa.line(0, y, width, y);
    }
    fondoPausa.endDraw();
    imgPausa = loadImage("cabeza.png");
  };
  
  //Flujo Logica Juego
  void update(){
    Posicion cabeza = serpiente.obtenerCabeza();
    println("pos Serpiente" + "[x: " + cabeza.x + ", y: " + cabeza.y + "]");
    println(estado);
    if(millis() >= tiempoUpdate){
      
      switch(estado){
        case INICIO:
          inicioJuego();
          break;
        case JUGANDO:
          jugando();
          break;
        case FINALIZADO:
          gameOver();
          break;
        case PAUSADO:
          juegoPausado();
          break;
      }
      
      tiempoUpdate = millis()+tickRate;
    }
  };
  
  void inicioJuego(){
    //Esperar INPUT
    if(input.inicioSolicitado()){
      puntaje = 0;
        serpiente.reset(tablero);
        estado = EstadoJuego.JUGANDO;
        tiempoComienzoJuego = millis();
    }
    
    
  }
  void jugando(){
    //leer Input
    serpiente.cambiarDireccion(input.obtenerDireccion());
     
    //mover serpiente
    serpiente.mover();
    //obtener cabeza
    Posicion cabeza = serpiente.obtenerCabeza();
    //validar colisiones
    if(!tablero.esPosicionValida(cabeza)){
      estado = EstadoJuego.FINALIZADO;
      return;
    }
    if(serpiente.seMuerde()){
      estado = EstadoJuego.FINALIZADO;
      return;
    }
    //verificar manzana
    if(cabeza.equals(manzana.obtenerPosicion())){
      manzana.reposicionar(tablero.ancho, tablero.alto, serpiente);
      serpiente.crecer();
      //Actualizar Puntaje
      puntaje++;
    }
  }
  void gameOver(){
    if(tiempoFinalJuego != -1){ tiempoFinalJuego = millis(); };
    
  }
  void juegoPausado(){
    
  }
  
  //UI y Render Juego
  boolean bandera = false;
  void render(){
    switch (estado){
       case INICIO:
         image(fondo, 0, 0);
         textFont(fontTitulos);
         textSize(48);
         textAlign(CENTER, CENTER);
         fill(#FFFFFF);
         noStroke();
         text("Snake_Game", width/2, height/2);
         textFont(fontTexto);
         textSize(24);
         fill(#929093);
         float yTexto = height / 2 + sin(offsetTitulos) * 5 + 60;
         offsetTitulos += 0.05;
         text("Presione 'ENTER' para empezar a jugar", width/2, yTexto);
           
         
         
         break;
       case JUGANDO:
         image(fondo, 0, 0);
         int anchoBoton = 250;
         int altoBoton = anchoBoton / 6;
         int xBoton = width/2-anchoBoton/2;
         int yBoton = height*7/8;
         fill(#91579B);
         rect(xBoton, yBoton, anchoBoton, altoBoton);
         textFont(fontTexto);
         textSize(24);
         textAlign(CENTER, CENTER);
         fill(#FFFFFF);
         text("Pausar Juego", xBoton, yBoton, anchoBoton, altoBoton);
         if(input.mouseEnBoton(xBoton, yBoton, anchoBoton, altoBoton)){
             estado = EstadoJuego.PAUSADO;
         };
         
         
         pushMatrix();
           translate(offsetX, offsetY);
           tablero.render();
           serpiente.render();
           manzana.render();
         popMatrix();
         
         break;
       case FINALIZADO:
         int anchoBotonFinalizado = 250;
         int altoBotonFinalizado = anchoBotonFinalizado / 6;
         int xBotonFinalizado = width/2-anchoBotonFinalizado/2;
         int yBotonFinalizado = height/2;
         if (!bandera){
           bandera = true; 
           image(fondoPausa, 0, 0);
           
           fill(#91579B);
           rect(xBotonFinalizado, yBotonFinalizado, anchoBotonFinalizado, altoBotonFinalizado);
           fill(#FFFFFF);
           text("Volver a Jugar", xBotonFinalizado, yBotonFinalizado, anchoBotonFinalizado, altoBotonFinalizado);
           fill(#BBBDED);
           text("Puntos: " + puntaje,  width/2, height/3);
           fill(#FFFFFF);
           textFont(fontTitulos);
           textSize(48);
           textAlign(CENTER, CENTER);
           text("GAME_OVER", width/2, height/4);
         }
         if(input.mouseEnBoton(xBotonFinalizado, yBotonFinalizado, anchoBotonFinalizado, altoBotonFinalizado)){
             estado = EstadoJuego.INICIO;
             bandera = false;
         };
       
       
         break;
       case PAUSADO:
         int anchoBotonPausa = 250;
         int altoBotonPausa = anchoBotonPausa / 6;
         int xBotonPausa = width/2-anchoBotonPausa/2;
         int yBotonPausa = height/2;
         if (!bandera){
           bandera = true; 
           image(fondoPausa, 0, 0);
           
           fill(#91579B);
           rect(xBotonPausa, yBotonPausa, anchoBotonPausa, altoBotonPausa);
           fill(#FFFFFF);
           text("Despausar Juego", xBotonPausa, yBotonPausa, anchoBotonPausa, altoBotonPausa);
           text("Puntos: " + puntaje, xBotonPausa, yBotonPausa/4, anchoBotonPausa, altoBotonPausa);
         }
         if(input.mouseEnBoton(xBotonPausa, yBotonPausa, anchoBotonPausa, altoBotonPausa)){
             estado = EstadoJuego.JUGANDO;
             bandera = false;
         };
         float xR = random(0, width);
         float yR = random(0, height);
         while(xR >= xBotonPausa-30 && xR <= xBotonPausa+anchoBotonPausa+30){ xR = random(0, width); }
         image(imgPausa, xR, yR, 20, 20);
         
         break;
    };

  }
}

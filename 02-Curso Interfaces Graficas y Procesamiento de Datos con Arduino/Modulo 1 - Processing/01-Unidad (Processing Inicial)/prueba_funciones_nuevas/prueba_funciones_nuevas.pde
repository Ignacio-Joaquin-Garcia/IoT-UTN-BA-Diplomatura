void setup(){
  size(500, 500);
  background(0,45,0);
  arc(100, 100, 250, 100, 0.5, 1);
  
  textSize(16);
  PFont font = createFont("Sofia-Regular.ttf", 16); //loadFont para archivos vlw || createFont para archivos ttf
  text("Hola Mundo", 200,200,0);
  textFont(font, 16);
  text("Hola Mundo", 200,300,0);
}

//El delay no hace lo que creemos que hace en processing!
long ultimoTiempo = 0;
void draw(){
  miDelay(500);
  text("esto aparece 500 mas tarde"+" si" , 200,400,0);

}

void miDelay(int espera){
   ultimoTiempo = millis();
   while(millis() < (ultimoTiempo + espera)){};
}

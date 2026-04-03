void setup()
{
  size(1000,600);
  float angulo = 0;
  float angulof = HALF_PI;
  int ancho = 100;
  int alto = 100;
  int posx = ancho;
  int posy = alto + 50;

  for(int i = 0; i < 4; i++)
  {
    fill(255);
    ellipse(posx + posx*i, posy, ancho, alto);
    fill(0);
    arc(posx + posx*i, posy, ancho, alto, angulo, angulof);
    angulo += HALF_PI;
    angulof += HALF_PI;
  }

  fill(255);
  arc(200, 300, 100, 100, 0, PI + QUARTER_PI, OPEN);
  arc(400, 300, 100, 100, 0, PI + QUARTER_PI, CHORD);
}

void draw()
{
}

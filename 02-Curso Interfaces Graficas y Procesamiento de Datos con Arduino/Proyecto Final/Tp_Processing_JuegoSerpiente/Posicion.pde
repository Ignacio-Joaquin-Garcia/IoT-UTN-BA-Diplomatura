class Posicion{
  int x;
  int y;
  
  Posicion(int x, int y){
    this.x = x;
    this.y = y;
  }
  
  boolean equals(Posicion otra){
    if(otra.x == x && otra.y == y){
      return true;
    };
    return false;
  }
  
}


class Direccion{
  int dx;
  int dy;
  
  Direccion(int dx, int dy){
    this.dx = dx;
    this.dy = dy;
  };

  // evitar ir en direccion opuesta
  boolean esOpuesta(Direccion otra) {
    return this.dx + otra.dx == 0 && this.dy + otra.dy == 0;
  }
}

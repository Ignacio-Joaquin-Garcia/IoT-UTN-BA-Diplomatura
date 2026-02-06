int pinPulsos = 2;
int pinBinario = 3;
int pinSubir = 4;

int numDisplay(int num){
  int hexaAMostrar;
  /*
    int num0 = 0x7F;//SI
    int num1 = 0x0C;//SI
    int num2 = 0xB6;//SI
    int num3 = 0x9F;//SI
    int num4 = 0xCC;//SI
    int num5 = 0xDB;//SI
    int num6 = 0xFA;//SI
    int num7 = 0x0F;//SI
    int num8 = 0xFF;//SI
    int num9 = 0xCF;//SI
  */
  switch (num){
  	case 0: 
    	hexaAMostrar = 0x7F;
    	break;
    case 1: 
    	hexaAMostrar = 0x0C;
    	break;
    case 2: 
    	hexaAMostrar = 0xB6;
    	break;
    case 3: 
    	hexaAMostrar = 0x9F;
    	break;
    case 4: 
    	hexaAMostrar = 0xCC;
    	break;
    case 5: 
    	hexaAMostrar = 0xDB;
    	break;
    case 6: 
    	hexaAMostrar = 0xFA;
    	break;
    case 7: 
    	hexaAMostrar = 0x0F;
    	break;
    case 8: 
    	hexaAMostrar = 0xFF;
    	break;
    case 9: 
    	hexaAMostrar = 0xCF;
    	break;
  }
  return hexaAMostrar;
}
void ponerNum7Display(int num){
  digitalWrite(pinSubir, LOW);
  shiftOut(pinBinario, pinPulsos, MSBFIRST, numDisplay(num));
  digitalWrite(pinSubir, HIGH);
  delay(1000);
}

void setup()
{ 
  DDRD = 0xFF;
}

void loop()
{
  for(int i = 0; i<=9;i++){
    ponerNum7Display(i);
  }
}

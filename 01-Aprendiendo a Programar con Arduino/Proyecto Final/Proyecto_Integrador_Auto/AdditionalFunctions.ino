void carPowerOnOff(){
  if(motor1.isMotorOn() || motor2.isMotorOn()){
    putMotorsOff(motor1, motor2);
    carLeds.lightsOff();
    powerOn = false;
  }else{
    putMotorsOn(motor1, motor2);
    carLeds.lightsOn();
    powerOn = true;
  }
}
void motorsVelocityLogic(){
  if(numberOfSameComandos != 0){
      if(lastComando == comando){
        velocidadGeneral = (int) (130 * log10(numberOfSameComandos+10));
        if(velocidadGeneral > 255){
          velocidadGeneral = 255;
        }
      }else{
        numberOfSameComandos = 0;
        velocidadGeneral = 1;
      }
    }
    lastComando = comando;
    numberOfSameComandos = numberOfSameComandos +1;
    if(!powerOn && comando != 0x0){
      comando = 0xFF;
      carLeds.noMoveAllowed();
      Serial.print("Comando: ");
    }
};
void commandsLogic(){
  switch (comando){
    case 0x0: {//Prender/Apagar
      carPowerOnOff();
      break;
    }
    case 0x1: {//Adelante
      moveForward(carLeds, motor1, motor2, velocidadGeneral, manualMode, gearShiftN);
      break;
    }
    case 0x9: {//Atras
      moveBackwards(carLeds, motor1, motor2, velocidadGeneral, manualMode, gearShiftN);
      break;
    }
    case 0x6: {//Derecha
      moveRight(carLeds, motor1, motor2, velocidadGeneral);
      break;
    }
    case 0x4: {//Izquierda
      moveLeft(carLeds, motor1, motor2, velocidadGeneral);
      break;
    }
    case 0x8: {//Intermitente Izquierda
      carLeds.leftBlink(blinkNumber);
      break;
    }
    case 0xA: {//Intermitente Derecha
      carLeds.rightBlink(blinkNumber);
      break;
    }
    case 0x5: {//Bocina
      carHorn.horn();
      break; 
    }
    case 0x2: {//Pausa Motores
      moveForward(carLeds, motor1, motor2, 0, false, 0);
      break;
    }
    case 0xC: {//Activar Modo Manual
      manualMode = !manualMode;
      break;
    }
	  case 0x10: {//Primera Marcha
      moveForward(carLeds, motor1, motor2, 0, manualMode, 1);
      break;
    }
    case 0x11: {//Segunda Marcha
      moveForward(carLeds, motor1, motor2, 0, manualMode, 2);
      break;
    }
    case 0x12: {//Tercera Marcha
      moveForward(carLeds, motor1, motor2, 0, manualMode, 3);
      break;
    }
    case 0x15: {//Neutro Marcha
      moveForward(carLeds, motor1, motor2, 0, manualMode, 0);
      break;
    }
    case 0x19: {//Reversa Marcha
      moveBackwards(carLeds, motor1, motor2, 0, manualMode, -1);  
      break;
    }
    default: {
      break;
    }
  }
}
void infraredSensorRecieveCommand(){
  if(IrReceiver.decode()){
    comando = IrReceiver.decodedIRData.command; //HEX
    Serial.print("Comando: ");
    Serial.println(comando, HEX);
    motorsVelocityLogic();
    commandsLogic();
    delay(10);
    IrReceiver.resume();
  }
}
//Tiempos
void generateInterruption(){
  if(carLeds.blinkInterruptionLeft){
    logicBlinker(carLeds, false);
  }
  if(carLeds.blinkInterruptionRight){
    logicBlinker(carLeds, true);
  }
  checkObstacles(carDistance, carHorn);
}
void millisInterruption(){
  if(millis() >= interruption){
  	interruption += interruptionSpeed;
    generateInterruption();
  }
}
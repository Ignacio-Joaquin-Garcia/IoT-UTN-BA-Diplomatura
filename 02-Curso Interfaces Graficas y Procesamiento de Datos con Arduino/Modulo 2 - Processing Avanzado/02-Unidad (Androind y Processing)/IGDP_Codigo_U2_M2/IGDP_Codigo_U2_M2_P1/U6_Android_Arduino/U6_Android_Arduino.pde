import android.content.Intent;
import android.os.Bundle;

import ketai.net.bluetooth.*;
import ketai.ui.*;
import ketai.net.*;

byte[] z  ={'Z'} ;//any random byte or character
KetaiBluetooth bt;
KetaiList klist;
String BTdevice ;

//------------------ Variables/Objects for red lines ----------------------

int distance  ; // recieved distance

//-------------- Variables/Objects for serial communication ---------------


boolean init =false;
int bytesCount = 0;
byte serialArray [] = new byte[2];
int angle = 1; 

//-------------------------------------------------------------------------

//****************************************************************
// The following code is required to enable bluetooth at startup.
//****************************************************************

void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  bt = new KetaiBluetooth(this);
}

void onActivityResult(int requestCode, int resultCode, Intent data) {
  bt.onActivityResult(requestCode, resultCode, data);
}


//*****************************************************************




//================================ Setup ==================================
void setup() {  

  //Basic setup
  orientation(LANDSCAPE);
  frameRate(30);
  
  bt.start();
  
 // finds paired device and connects to it
 klist = new KetaiList(this, bt.getPairedDeviceNames());

}

//======================= Drawing Processed data ==========================

void draw() {

  if (drawState) {

    // Simulating the transition and the motion blur
    noStroke();
    fill(0, 4); 
    rect(0, 0, width, height); 


    bt.writeToDeviceName(BTdevice, z); // signal to request for new data 
    
    drawState = false ; // stop the draw loop untill new data is recieved
   
   
  }

}



//=================== Event for BT devices selection =====================


void onKetaiListSelection(KetaiList klist)
{
  String selection = klist.getSelection();
  bt.connectToDeviceByName(selection);
  BTdevice = selection ;
  //dispose of list for now
  klist = null;
}

//=========================== Receiving data ==============================

  //Call back method to manage data received
void onBluetoothDataEvent(String who, byte[] Data){

  if(Data.length == 1){
  
  serialArray[bytesCount] = Data[0] ;
  bytesCount++;
  
  if (bytesCount == 2) {
    
      angle = int(serialArray[0]);
      distance = int(serialArray[1]);
      drawState = true ;
      bytesCount = 0; 
      
   }
 }
 else {
 
      angle = int(Data[0]);
      distance = int(Data[1]);
      drawState = true ;
      bytesCount = 0;
 }
 
}

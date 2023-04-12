#include <EEPROM.h>

// Global macros
#define EEPROM_SIZE 128         //number of bytes desired for flash storage to ESP32
#define LENGTH(x) (strlen(x)+1)

// Global variables
 // EEPROM variables
int EEPROM_nextaddr = 0;               // initialized with the start address, tracks teh current next available addresses
int EEPROM_addresses[EEPROM_SIZE/2] = {EEPROM_nextaddr};   // stores a registry of all start addresses
                                                           // first address entry is the starting address used
                                       // EEPROM_SIZE/2 because smallest possible is 1 byte followed by null
int EEPROM_totaladdr = 1;              // Tracks how many address start locations have been made. set to 1 because there will always be at least 1 if in use

  // Serial variables
int incomingByte;      // a variable to read incoming serial data into

//Custom functions
/*
 * This function will take in a string variable and write the result
 * into the flash memory of the ESP32
 * 
 * adapted from https://stackoverflow.com/questions/56139657/write-string-to-permanent-flash-memory-of-arduino-esp32
 */
void writeString(const char* toStore) {
  int i = 0;
//  Serial.println("EEPROM write:\t");
  //write actual data
  for (; i < LENGTH(toStore)-1; i++) {
    EEPROM.write(EEPROM_nextaddr + i, toStore[i]);
//    uncomment for explicit address write printout
//    Serial.print("address: ");
//    Serial.print(EEPROM_nextaddr + i);
//    Serial.print(", ");
//    Serial.println(toStore[i]);
  }
  EEPROM.write(EEPROM_nextaddr + i, '\0');
  EEPROM.commit();
//    uncomment for explicit address write printout
//  Serial.print("Terminating address:\t");
//  Serial.println(EEPROM_nextaddr + i);
  
  EEPROM_totaladdr += 1;                                  // Update the start locations counter (total individual locations)
  EEPROM_nextaddr += i +1;                                // update the address for next sequential write
  EEPROM_addresses[EEPROM_totaladdr-1] = EEPROM_nextaddr; // Add the address entry to the list
}

String readStringFromFlash(int startAddr) {
  String in;
  char curIn;
  int i = 0;
  curIn = EEPROM.read(startAddr);
//  Serial.print("EEPROM read:\t");
  for (; EEPROM.read(startAddr + i) != '\0'; i++) {
    curIn = EEPROM.read(startAddr + i);
    in += curIn;
//    Serial.print(char(curIn));
  }
//  Serial.println();
  
  return String(in);
}
void setup() {
  // initialize serial communication:
  Serial.begin(115200);
  EEPROM.begin(EEPROM_SIZE);
  
  // initialize the LED pin as an output:
  pinMode(19, OUTPUT);
}

char* capture;

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    while(Serial.available()) {
      // read the oldest byte in the serial buffer:
      incomingByte = Serial.read();
      capture += incomingByte;
    }
    writeString(capture);
  }
}

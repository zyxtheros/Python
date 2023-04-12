#include <WiFi.h>
#include <WebSocketServer.h>
#include <ESP32Servo.h>
#include "definitions.h"
#define READ_PRECISION 10
//#define DIGITAL_OUT (int[]) {18, 19, 21} // define all pins used for digital output
//const int DIGITAL_OUT_LEN = sizeof(DIGITAL_OUT)/sizeof(int);

//initialize resource variables
WiFiServer server(80);
WebSocketServer webSocketServer;
Servo servo[SERVO_LEN];

const char *ssid = "ESP32 Test AP";
const char *password = "123456789";

void parsecmd(char* stream) {
  Serial.print(stream);
  Serial.print("->\t");

  const char* delim = ",";
  const char* param2 = ":";
  char* token = strtok(stream, delim); //subtrings to print
  /*
   * 
   */

  if (strcmp(token, "READ") == 0) {       // read digital state command
    Serial.print("getting state ");
    token = strtok(NULL, delim); // get the next substring
    Serial.print(token);

    int val = digitalRead(atoi(token));
    char val_ch[READ_PRECISION];
    itoa(val, val_ch, 10); // int value, char[] string, int base
    Serial.println(val);
    webSocketServer.sendData(val_ch);
  }
  else if (strcmp(token, "HIGH") == 0) {  // set digital high command
    Serial.print("setting " );
    token = strtok(NULL, delim); // get the next substring
    Serial.print(token);
    Serial.println(" HIGH");

    digitalWrite(atoi(token), HIGH);
    webSocketServer.sendData(token);
  }
  else if (strcmp(token, "LOW") == 0) {   // set digital low command
    Serial.print("setting ");
    token = strtok(NULL, delim); // get the next substring
    Serial.print(token);
    Serial.println(" LOW");

    digitalWrite(atoi(token), LOW);
    webSocketServer.sendData(token);
  }
  else if (strstr(token, param2) != NULL) { // check for secondary parameter e.g. SERVO:xxx,yy
    Serial.print("adjusting ");
    char* token2 = token;
    token = strtok(NULL, delim);          // get the next substring from "," split
    char* pin = token;                    // stores the pin name
    token2 = strtok (token2, param2);     // split 2 parameter command
    char* key = token2;                   // stores the command name
    token2 = strtok(NULL, param2);        // get the next substring from ":" split
    char* value = token2;                 // stores the parameter value
    Serial.print(key);
    Serial.print(" of ");
    
    if (strcmp(key, "SERVO") == 0) {        // set the angle of a servo
      Serial.print(pin);
      Serial.print(" to ");
      Serial.println(value);
      //do servo stuff
      int index = deref(SERVO_PIN, atoi(pin), SERVO_LEN);
      servo[index].write(atoi(value));
      Serial.println();
      Serial.print("index needed:");
      Serial.println(index);
      webSocketServer.sendData(pin);
    } 
  }
  else {                                  // error catching
    Serial.println("NaN (invalid command)");
  }
}
/* returns which index has the desired value (needle) for the array (haystack)
 * if multiple exist, the first is always returned. if none -1 is returned
 * parameters:
 *      int haystack[] (array searched)
 *      int needle     (value to find)
 *      int span       (elements in haystack to search)
 */
int deref(const unsigned int haystack[], int needle, int span) {
  int output = -1; // initially set as the error value of returned
  for (int i = 0; i < span; i++) {
    if (haystack[i] == needle){
      output = i;
      break;
    }
  }
  return output;
}

void setup() {
  pinMode(ONBOARD_LED, OUTPUT);
  for (int i = 0; i < DIGITAL_OUT_LEN; i++) { // setup output pins
    pinMode(DIGITAL_OUT[i], OUTPUT);
  }
  for (int i = 0; i < DIGITAL_OUT_LEN; i++) { // setup output pins
    pinMode(DIGITAL_IN[i], INPUT);
  }
  for (int i = 0; i < SERVO_LEN; i++) {       // setup for servo pins
    servo[i].setPeriodHertz(50);              // standard 50 hz servo        
    servo[i].attach(SERVO_PIN[i], us_min, us_max);
  }

  Serial.begin(115200);

  delay(4000);

  WiFi.softAP(ssid, password);
  Serial.println(WiFi.softAPIP());

  server.begin();
  delay(100);
}

void loop() {

  WiFiClient client = server.available();

  if (client.connected() && webSocketServer.handshake(client)) {
  Serial.println("Client disconnected");


    while (client.connected()) {
      digitalWrite(ONBOARD_LED, HIGH); // set onboard LED HIGH while client is connected
      String str = webSocketServer.getData().c_str();
      char stream[str.length() + 1];
      str.toCharArray(stream, str.length() + 1);

      if (strlen(stream) > 0) {
        parsecmd(stream);
      }

      delay(10); // Delay needed for receiving the data correctly
    }

    Serial.println("The client disconnected");
    digitalWrite(ONBOARD_LED, LOW); // set onboard LED LOW after client is disconnected
    delay(100);
  }
  else { // blink LED while waiting for client and setup is done
    digitalWrite(ONBOARD_LED, HIGH);
    delay(500);
    digitalWrite(ONBOARD_LED, LOW);
    delay(500);
  }

  delay(100);
}

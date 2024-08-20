#include <WiFi.h>
#include <WebSocketServer.h>
#define READ_PRECISION 10
#define DIGITAL_OUT (int[]) {18, 19, 21} // define all pins used for digital output
const int DIGITAL_OUT_LEN = sizeof(DIGITAL_OUT)/sizeof(int);


WiFiServer server(80);
WebSocketServer webSocketServer;

const char *ssid = "ESP32 Test AP";
const char *password = "123456789";

void parsecmd(char* stream) {
  Serial.print(stream);
  Serial.print("->\t");

  const char* delim = ",";
  char* token = strtok(stream, delim); //subtrings to print

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
  else {                                  // error catching
    Serial.println("NaN (invalid command)");
  }
}

void setup() {
  for (int i = 0; i < DIGITAL_OUT_LEN; i++) { // setup output pins
    pinMode(DIGITAL_OUT[i], OUTPUT);
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



    while (client.connected()) {

      String str = webSocketServer.getData().c_str();
      char stream[str.length() + 1];
      str.toCharArray(stream, str.length() + 1);

      if (strlen(stream) > 0) {
        parsecmd(stream);
      }

      delay(10); // Delay needed for receiving the data correctly
    }

    Serial.println("The client disconnected");
    delay(100);
  }

  delay(100);
}

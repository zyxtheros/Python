int x = 1;
int y = 2;
int z = 3;
int dl = 1000; // in ms

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(x);
  Serial.print(", ");
  Serial.print(y);
  Serial.print(", ");
  Serial.println(z);
  x+=2;
  y+=5;
  z+=4;
  delay(dl);
}

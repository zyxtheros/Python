//digital pin definitions
#define ONBOARD_LED 2
#define DIGITAL_OUT (int[]) {18, 19, 21} // define all pins used for digital output
#define DIGITAL_IN (int[]) {} // define all pins used for digital input
const unsigned int DIGITAL_OUT_LEN = sizeof(DIGITAL_OUT)/sizeof(int);  // elements in array
const unsigned int DIGITAL_IN_LEN = sizeof(DIGITAL_IN)/sizeof(int);  // elements in array

// PWM pins
// Recommended PWM GPIO pins on the ESP32 include 2,4,12-19,21-23,25-27,32-33 
const unsigned int SERVO_PIN[] = {22, 23};                   // define all pins used for digital input
const unsigned int SERVO_LEN = sizeof(SERVO_PIN)/sizeof(int);  // elements in array
const unsigned int us_min = 500, us_max = 2400;                // min/max positions in microseconds

/*
Program: Receive Integers From Raspberry Pi
File: receive_ints_from_raspberrypi.ino
Description: Receive integers from a Raspberry Pi
Author: Addison Sears-Collins, Cuong Nguyen
Website: https://automaticaddison.com
Date: October 4, 2022
*/
#include <Servo.h>

#define NUM_SERVO 3

Servo myservo[NUM_SERVO];

// Initialize the integer variables
int servo_angle[NUM_SERVO];

int servo_state[NUM_SERVO];

int servo_pin[NUM_SERVO] = {2,3,4};
 
void setup(){
  // Set the baud rate  
  Serial.begin(115200);

  for (int i=0; i<NUM_SERVO; i++) {
    servo_angle[i]=90;
    myservo[i].attach(servo_pin[i]);
    servo_state[i] = 90;
  }
  
  Serial.println("ready");
}
 
void loop(){
 
  if(Serial.available() > 1) {
    for (int i=0; i<NUM_SERVO; i++) {
      servo_angle[i] = Serial.parseInt();
    }   

    while (!checkServoArrival()) {
      for (int i=0; i<NUM_SERVO; i++) {
        if (servo_state[i] < servo_angle[i]) {
          servo_state[i]++;
        } else if (servo_state[i] > servo_angle[i]) {
          servo_state[i]--;
        }
        myservo[i].write(servo_state[i]);
      }
      delay(20);
    }
     
 
    // We do println to add a new line character '\n' at the end
    // of the comma-separated stream of integers
    for (int i=0; i<NUM_SERVO-1; i++) {
      Serial.print(servo_angle[i]);Serial.print(",");
    }
    Serial.println(servo_angle[NUM_SERVO-1]);
  }
}

bool checkServoArrival() {
  for (int i=0; i<NUM_SERVO; i++) {
    if (servo_state[i] != servo_angle[i]) {
      return false;
    }
  }
  return true;
}

#!/usr/bin/env python3
 
###############################################################################
# Program: Send Integers to an Arduino From a Raspberry Pi
# File: send_ints_to_arduino.py
# Description: This program runs on a Raspberry Pi. It sends integers
#   to Arduino in comma-separated format. It also receives the integers it sent
#   and prints them to the screen. This provides bi-directional (2-way) communication
#   between Arduino and Raspberry Pi.
# Author: Addison Sears-Collins
# Website: https://automaticaddison.com
# Date: July 5, 2020
###############################################################################
 
import serial # Module needed for serial communication
import time # Module needed to add delays in the code
 
# Set the port name and the baud rate. This baud rate should match the
# baud rate set on the Arduino.
# Timeout parameter makes sure that program doesn't get stuck if data isn't
# being received. After 1 second, the function will return with whatever data
# it has. The readline() function will only wait 1 second for a complete line 
# of input.
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
 
# Intialize the integer values we'll send to Arduino
servo_0_angle = 90
servo_1_angle = 7
servo_2_angle = 63
servo_3_angle = 85
servo_4_angle = 162
servo_5_angle = 45
 
# Get rid of garbage/incomplete data
ser.flush()
 
# Infinite loop
while (1):
 
  # Convert the integers to a comma-separated string
  servo_0_angle = (servo_0_angle+1) % 180
  angle_value_list = [str(servo_0_angle),str(servo_1_angle),str(
    servo_2_angle),str(servo_3_angle),str(servo_4_angle),str(servo_5_angle)]    
  send_string = ','.join(angle_value_list)
  send_string += "\n"
 
  # Send the string. Make sure you encode it before you send it to the Arduino
  ser.write(send_string.encode('utf-8'))
  
  # Receive data from the Arduino
  #if ser.in_waiting > 0:    
  receive_string = ser.readline().decode('utf-8', 'replace').rstrip()

  # Print the data received from Arduino to the terminal
  print("Regurgitated by Arduino:")
  print(receive_string + "\n")
  time.sleep(1)

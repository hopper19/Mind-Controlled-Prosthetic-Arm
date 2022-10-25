###############################################################################
# Program: Control Servo from Raspberry Pi
# File: 
# Description: This program runs on a Raspberry Pi. 
# Author: Cuong Nguyen
# Date: October 4, 2022
###############################################################################
 
import serial # Module needed for serial communication
import time # Module needed to add delays in the code
 
NUM_SERVO = 3 # Number of servos

# Set the port name and the baud rate. This baud rate should match the
# baud rate set on the Arduino.
# Timeout parameter makes sure that program doesn't get stuck if data isn't
# being received. After 1 second, the function will return with whatever data
# it has. The readline() function will only wait 1 second for a complete line 
# of input.
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5, write_timeout=5)
 
# Intialize the integer values we'll send to Arduino
servo_angle = [[130,115,180],[55,40,105]]

print("Waiting for Arduino to reset...")
ser.readline().decode('utf-8', 'replace').rstrip()
print("Python program starting...\n")

# Infinite loop
while (1):
  command = input("Enter a command: ")
  if command == "sweep":
    for i in range(10):
      for i in range(2):
        # Convert the integers to a comma-separated string   
        send_string = ','.join(map(str,servo_angle[i]))
        send_string += "\n"
      
        # Send the string. Make sure you encode it before you send it to the Arduino
        ser.write(send_string.encode('utf-8'))
        print("Sent to Arduino: " + send_string,end='')
        
        # Receive data from the Arduino
        receive_string = ser.readline().decode('utf-8', 'replace').rstrip()

        # Print the data received from Arduino to the terminal
        print("Arduino reported servos moved to angles:")
        print(receive_string + "\n")
  elif command == "quit":
    break
  else:
    command += "\n"
    ser.write(command.encode('utf-8'))
    print("Sent to Arduino: " + command, end='')

    # Receive data from the Arduino
    receive_string = ser.readline().decode('utf-8', 'replace').rstrip()

    # Print the data received from Arduino to the terminal
    print("Arduino reported servos moved to angles:")
    print(receive_string + "\n")

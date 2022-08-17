# HCR_Servo_IMU
Upload the IMU code into either an arduino or ESP32. First Microcontroller 
Uplaod the StandardFrimata code into the other Mircocontroller

Running the python file will allow first to read serially the acceleration data 
Then freqeuncy decompostion will be done
following that incase the absolute values of the one sided DFT exceed a certain threshold 
the servo motor will move 180 degrees

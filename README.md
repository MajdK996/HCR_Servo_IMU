# HCR_Servo_IMU
In this project the concept was to actuate the servo motor with the case when a tremor was detected.

First, upload the IMU code into either an arduino or ESP32 which ever serves to be the first Microcontroller.
Second, uplaod the StandardFrimata code into the other Mircocontroller.
Third, run the python file will allow first to read serially the acceleration data.
Then freqeuncy decompostion will be done.
Following that incase the absolute values of the one sided DFT exceed a certain threshold the servo motor will move 180 degrees.

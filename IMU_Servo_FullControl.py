from os import sep
from socket import timeout
import serial 
from scipy.fft import fft, fftfreq
import time 
import pandas 
import numpy as np
import matplotlib.pyplot as plt 
import sensormotion as sm

sr= 140

def IMU(data):
    #Settting the port 
    data = serial.Serial('COM10', baudrate=512000, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
    t_end = time.time() + 5

    acc_t = []
    ax_t = []
    ay_t= []
    az_t= []

    
    print('Started Collecting data')
    while time.time()<t_end:
        while(data.inWaiting()==0):
            pass
        data_t = data.readline()
        data_t = str(data_t, 'utf-8')
        split_t = data_t.split(',')
        acc_t.append(float(split_t[0]))
        ax_t.append(float(split_t[1]))
        ay_t.append(float(split_t[2]))
        az_t.append(float(split_t[3]))
    return acc_t

#Plotting the total Acc in time 
def Acc_mo(x):
    s = 5/ len(x)
    t = np.arange(0,5,s)
    plt.figure(figsize = (8,6))
    plt.plot(t,x)
    plt.ylabel('Amplitude')
    plt.show()

#Freqeuncy decompostion 
def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = np.reshape((N,1))
    e = np.exp(-2j *np.pi* k* n/N)
    X = np.dot(e,x)
    N = len(x)
    n = np.arange(N)
    T = N/sr
    freq = n/T
    n_oneside = N//2
    # get the one side frequency
    f_oneside = freq[:n_oneside]
    # normalize the amplitude
    X_oneside =X[:n_oneside]/n_oneside
    return abs(X_oneside)

from pyfirmata import Arduino, SERVO
from time import sleep



def main():
    port = 'COM3'
    pin = 3 
    board = Arduino(port)
    board.digital[pin].mode = SERVO
    counter = 0

    def rotateServo(pin, angle):
        board.digital[pin].write(angle)
        sleep(0.015)

    while True:
        acc_t = IMU()
        Acc_mo(acc_t)
        acc_freq_content = DFT(acc_t) 
        if np.all(acc_freq_content[1:]>0.1):
            if counter == 0:
                for i in range(0,180):
                    rotateServo(pin, i)
                    counter = counter +1
            else:
                pass 
        if  np.all(acc_freq_content[1:]<0.1):
            if counter == 1:
                for i in range(180, 1, -1):
                    rotateServo(pin,i)
                    counter =0
            else:
                pass 
        sleep(15)



if __name__ == '__main__':
    main() 
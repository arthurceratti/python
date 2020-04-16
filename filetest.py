#!/bin/python3

import math
import os
import random
import re
import sys
import serial
import matplotlib.pyplot as plt

def humidityShowFunction(): 
    plt.plot(xAxysList, humidity_list)
    plt.show() 
def temperatureShowFunction():
    plt.plot(xAxysList, temperatureList)
    plt.show() 
t = 0
humidity_list = []
temperatureList = []
xAxysList = []
port = serial.Serial("COM4", baudrate=115200, timeout=3.0)
rcv = [0]
while t<10:
    #port.write("\r\nSay something:")
    # buffer de x tamanho
    rcv = port.read(100)
    #decodificando de byte para ASCII
    rcv=rcv.decode('ASCII')
    humidity = int(rcv[0:2])
    temperature = int(rcv[5:7])
    #print(rcv[5:7])
    print(t)
    humidity_list.append(humidity)
    temperatureList.append(temperature)
    xAxysList.append(t)
    t = t+1
#humidityShowFunction()    
temperatureShowFunction()
#print(humidity_list)
    #port.write("\r\nYou sent:" + repr(rcv))
#f= open("guru99.txt","w+")
#fh = open("welcome.txt","r")
#print (f.read())

#!/bin/python3
import math
import os
import random
import re
import sys
import serial
import matplotlib.pyplot as plt

#f= open("guru99.txt","w+")
#fh = open("welcome.txt","r")
#print (f.read())

def plotFunctionList(x,y): 
    plt.plot(x, y)
    #plt.pause(0.05)
    plt.show() 

#Variable declarations
humidity_list = []
temperatureList = []
xAxysList = []
rcv = [0]

#Setup Serial Port
port = serial.Serial("COM4", baudrate=115200, timeout=3.0)
rcv = port.read(100)
rcv = rcv.decode('ASCII')
port.write(79)
 
t=0 #numero de amostras de temperatura e umidade antes de plotar
while t<10:
    # buffer de x tamanho
    port.write(75)
    rcv = port.read(100)
    rcv = rcv.decode('ASCII')
    #decodificando de byte para ASCII
    temperature = int(rcv[0:2])
    print(t)
    #humidity_list.append(humidity)
    temperatureList.append(temperature)
    xAxysList.append(t)
    t = t+1
plotFunctionList(xAxysList,temperatureList)


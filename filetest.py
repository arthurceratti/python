#!/bin/python3
import math
import os
import random
import re
import sys
import serial
import matplotlib.pyplot as plt
import time

#f= open("guru99.txt","w+")
#fh = open("welcome.txt","r")
#print (f.read())

def plotFunctionList(dataToBePlotted):
    """ função que serve para plotar"""
    plt.plot(dataToBePlotted) 
    plt.show()
    time.sleep(3)
    plt.cla()
    plt.clf()
    plt.close()

#Variable declarations
humidity_list = []
temperatureList = []
xAxysList = []
rcv = [0]

#Setup Serial Port
port = serial.Serial("COM4", baudrate=115200, timeout=3.0)
rcv = port.read(100)
rcv = rcv.decode('ASCII')
port.close

t=0 #numero de amostras de temperatura e umidade antes de plotar
while t<100:
    # buffer de x tamanho
    port.write(b'O')
    port.close
    rcv = port.read(100)
    #decodificando de byte para ASCII
    rcv = rcv.decode('ASCII') 
    port.close 
    print(rcv)
    temperature = int(rcv[0:2])
    print(t)
    #humidity_list.append(humidity)
    temperatureList.append(temperature)
    xAxysList.append(t)
    t = t+1
    time.sleep(5)
    plotFunctionList(temperatureList)
    

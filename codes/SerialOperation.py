# -*- coding: utf-8 -*- 
'''
Created on 2013-8-3

@author: Administrator
'''
import serial
import time

class MySerial(object):
    
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.timeout = 10
    
    def reinit(self):
        self.ser = serial.Serial()
        self.ser.timeout = 10
      
    def getSupportedInfo(self):
        info = {}
        info['baudrate'] = dict(self.ser.getSupportedBaudrates())
        info['bytesize'] = dict(self.ser.getSupportedByteSizes())
        info['parity'] = dict(self.ser.getSupportedParities())
        info['stopbit'] = dict(self.ser.getSupportedStopbits())
        return info
    
    def sendData(self,data):
        count = 0
        tempstr = ''
        for each in data:
            count += self.ser.write(each)
            tempstr+=each
            time.sleep(0.006)
        return (count,tempstr)
    
    
        
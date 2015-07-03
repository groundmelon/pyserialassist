# -*- coding: utf-8 -*-
import threading
import wx

class SerialListener(threading.Thread): #The timer class is derived from the class threading.Thread
    def __init__(self, ser):
        threading.Thread.__init__(self)
        self.ser = ser
        
        self.thread_stop = False
        self.listening = False
 
    def regiterWindow(self, window):
        self.window = window
    
        
    def run(self): #Overwrite run() method, put what you want the thread do here
        while not self.thread_stop:
            rcvchr = self.ser.read(1)
            if rcvchr:
                wx.CallAfter(self.window.onReceiveSerial,rcvchr)
        print(self.getName()+" will stop")
            
    def stop(self):
        self.thread_stop = True
       
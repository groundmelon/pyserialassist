# -*- coding: utf-8 -*- 
'''
Created on 2013-8-3

@author: Administrator
'''
import os
import wx
import serial.tools.list_ports as lstprt
import serial
import MainFrameBase
import SerialOperation
import SerialListenerThread
import PickleFileIO
import binascii
import time

if os.name == "nt":
    import win32api
import string




class MainFrame(MainFrameBase.MainFrameBase):
    '''
    classdocs
    '''
    TYPE_HEX = 0
    TYPE_ASC = 1
    def __init__(self,dev):
        '''
        Constructor
        '''
        MainFrameBase.MainFrameBase.__init__(self,None)
        
        exeName = ""
        if os.name == "nt":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            #print ('exeName:[%s]'%exeName)
            if exeName.find('python.exe') == -1:
                    self.SetIcon(wx.Icon(exeName+';0', wx.BITMAP_TYPE_ICO))
            else:
                self.SetIcon(wx.Icon(r'sa.ico', wx.BITMAP_TYPE_ICO))
        else:
            self.SetIcon(wx.Icon(r'sa.ico', wx.BITMAP_TYPE_ICO))
    
        self.rcvbuf = []
        self.newrcvbuf=[]
        self.bufsize = 10240
        self.rcvbuflenlast = -1
        self.rcvbuflenthis = 0
        
        self.dev = dev
        
        self.settingComponents=[self.m_choice_com,
                                self.m_choice_baudrate,
                                self.m_choice_databits,
                                self.m_choice_parity,
                                self.m_choice_stopbits,
                                self.m_checkBox_hardFlowCtrl,
                                self.m_checkBox_softFlowCtrl,
                                self.m_menu_load,
                                ]
        self.sndComponents = [self.m_textCtrl_send,
                              self.m_button_send,
                              self.m_radioBtn_sASCII,
                              self.m_radioBtn_sHEX,
                              self.m_staticTextHistoryPrompt,
                              ]
        
        self.m_statusBar.SetStatusWidths([-3,-2])
        
        self.applySerialToggleUI(False)
        
        self.Bind(wx.EVT_CLOSE, self.onQuit)
        
        #init options
        devinfo = self.dev.getSupportedInfo()
        print devinfo

        btl = sorted(devinfo['baudrate'], lambda a,b:cmp(int(a),int(b)))
        self.m_choice_com.SetItems([each[0] for each in lstprt.comports()])    
        self.m_choice_baudrate.SetItems([str(x) for x in devinfo['baudrate']])
        self.m_choice_databits.SetItems([str(x) for x in devinfo['bytesize']])
        self.m_choice_parity.SetItems([str(x) for x in devinfo['parity']])
        self.m_choice_stopbits.SetItems([str(x) for x in devinfo['stopbit']])
                        
        
        self.m_choice_com.SetSelection(0)
        self.m_choice_baudrate.SetStringSelection('9600')              
        self.m_choice_databits.SetStringSelection('8')
        self.m_choice_parity.SetStringSelection('None')
        self.m_choice_stopbits.SetStringSelection('1')
        self.m_checkBox_hardFlowCtrl.SetValue(False)
        self.m_checkBox_softFlowCtrl.SetValue(False)
        
        port_str = "null"
        if isinstance(lstprt.comports(), list):
            if lstprt.comports():
                port_str = lstprt.comports()[0]
        else:
            port_str = lstprt.comports().next
        self.sSettings={'port':port_str,
                        'baudrate':9600,
                        'bytesize':8,
                        'parity':'N',
                        'stopbits':1,
                        'rtscts':False,
                        'xonxoff':False,
                        }
        
        
        
        self.sendType = self.TYPE_ASC
        self.rcvType = self.TYPE_ASC
        
        self.SetStatusText("应用已经就绪")
        
        # load default settings
        filepath = 'sasetting.sas'
        try:
            pfio = PickleFileIO.PickleFileIO(filepath)
            self.sSettings = pfio.load()
            self.applySettings()
            self.m_statusBar.SetStatusText(u'设置"%s"已经应用。'%filepath)
            #wx.MessageBox('设置"%s"已经应用。'%filepath, u"设置成功",wx.OK | wx.ICON_INFORMATION)
        except (EOFError,IOError),e:
            #wx.MessageBox(u'设置"%s"应用失败。\n%s'%(filepath,str(e)), u"设置失败",wx.OK | wx.ICON_ERROR)
            self.m_statusBar.SetStatusText(u'默认设置"%s"未找到'%filepath)
        
        self.timer = wx.Timer(self)#创建定时器
        self.Bind(wx.EVT_TIMER, self.onUpdateUITimer, self.timer)#绑定一个定时器事件
        
        
    
    def onQuit(self,evt):
        print("onQuit")
        try:
            self.listenerThread.stop()
        except AttributeError:
            pass
        self.Destroy()
        
    
    def onSeeComInfo(self, event):
        MainFrameBase.MainFrameBase.onSeeComInfo(self, event)
        msg = ''
        coms = lstprt.comports()
        for each in coms:
            msg += "%s \t %s\n"%(each[0],each[1])
        wx.MessageBox(msg, u"串口信息",wx.OK | wx.ICON_INFORMATION)
        self.m_choice_com.SetItems([each[0] for each in lstprt.comports()])
        self.m_choice_com.SetSelection(0)
        
    def onSerialToggle(self, event):
        MainFrameBase.MainFrameBase.onSerialToggle(self, event)
        if self.serialToggle == True:
            self.closeDevice()
        else:
            self.openDevice()
        
    def applySerialToggleUI(self,switch):
        self.serialToggle = switch
        self.enableSettingUI(not self.serialToggle)
        self.enableSndUI(self.serialToggle)
    
    def openDevice(self):
        try:
            self.dev.reinit()
            self.setByChoice()
            self.dev.ser.open()
            
            self.listenerThread = SerialListenerThread.SerialListener(self.dev.ser)
            self.listenerThread.regiterWindow(self)
            self.listenerThread.start()
            
            print self.dev.ser
            self.applySerialToggleUI(True)
            self.SetStatusText(self.dev.ser.portstr+u"已经打开")
            self.tc = TrnsConter(self)
            self.history = InputHistory(self)
            self.m_toggleBtn_serial.SetLabel(u"断开连接")
            self.timer.Start(50)#设定时间间隔
        
        except serial.SerialException,e:
            wx.MessageBox(u"串口可能已经被占用！\n%s"%str(e), u"串口开启错误",wx.OK | wx.ICON_ERROR)
            self.SetStatusText(str(e),0)
            try:
                self.closeDevice()
            except AttributeError,e:
                pass
            except Exception,e:
                print(e)
        
        except Exception,e:
            wx.MessageBox(str(e), u"出现错误",wx.OK | wx.ICON_ERROR)
            self.SetStatusText(str(e),0)
            try:
                self.closeDevice()
            except AttributeError,e:
                pass
            except Exception,e:
                print(e)
        
            
    
    def closeDevice(self):
        
        self.timer.Stop()
        self.listenerThread.stop()
        self.dev.ser.close()
        self.applySerialToggleUI(False)
        self.m_toggleBtn_serial.SetLabel(u"建立连接")
        self.SetStatusText(self.dev.ser.portstr+u"已经关闭")
        
        
    def applySettings(self):
        self.dev.ser.apply_settings(self.sSettings)
        self.dev.ser.port = self.sSettings['port']
        # self.dev.ser.setBaudrate(self.sSettings['baudrate'])
        # self.dev.ser.setByteSize(self.sSettings['bytesize'])
        # self.dev.ser.setParity(self.sSettings['parity'])
        # self.dev.ser.setStopbits(self.sSettings['stopbits'])
        # self.dev.ser.setXonXoff(self.sSettings['xonxoff'])
        # self.dev.ser.setRtsCts(self.sSettings['rtscts'])
        # self.dev.ser.setPort(self.sSettings['port'])
        
        self.updateSettingUI()
        print(self.dev.ser.get_settings());
        
    
    def setByChoice(self):
        self.sSettings={#'baudrate':int(self.m_choice_baudrate.GetStringSelection()),
                        'baudrate':int(self.m_choice_baudrate.GetValue()),
                        'bytesize':int(self.m_choice_databits.GetStringSelection()),
                        'parity':self.m_choice_parity.GetStringSelection()[0],
                        'stopbits':int(self.m_choice_stopbits.GetStringSelection()),
                        'rtscts':self.m_checkBox_hardFlowCtrl.IsChecked(),
                        'xonxoff':self.m_checkBox_softFlowCtrl.IsChecked(),
                        'port':self.m_choice_com.GetStringSelection(),
                        }
        self.applySettings()
        return
    
    def updateSettingUI(self):
        self.m_choice_com.SetStringSelection(self.sSettings['port'])
        self.m_choice_baudrate.SetStringSelection(str(self.sSettings['baudrate']))              
        self.m_choice_databits.SetStringSelection(str(self.sSettings['bytesize']))
        self.m_choice_parity.SetStringSelection(str(self.sSettings['parity']))
        self.m_choice_stopbits.SetStringSelection(str(self.sSettings['stopbits']))
        self.m_checkBox_hardFlowCtrl.SetValue(self.sSettings['rtscts'])
        self.m_checkBox_softFlowCtrl.SetValue(self.sSettings['xonxoff'])
    
    def enableSettingUI(self,switch):
        for each in self.settingComponents:
            each.Enable(switch)
            
    def enableSndUI(self,switch):
        for each in self.sndComponents:
            each.Enable(switch)
            
    def onReceiveSerial(self,rcvchr):
        for each in rcvchr:
#             self.m_recvarea.AppendText(self.rawToDisplay(each, 'rcv'))
            self.newrcvbuf.append(each)
            self.rcvbuf.append(each)
        self.tc.updateData(len(rcvchr), 0)
    
    def onUpdateUITimer(self, evt):
        if self.newrcvbuf:
            self.m_recvarea.AppendText( self.rawToDisplay(''.join(self.newrcvbuf), 'rcv') )
        self.tc.updateDisplay()
        self.newrcvbuf=[]
            
        
    def rawToDisplay(self, src, texttype):        
        if texttype == "send" and self.sendType == self.TYPE_HEX:
            des = self.stringToHexString(src)
        elif texttype == "rcv" and self.rcvType == self.TYPE_HEX:
            des = self.stringToHexString(src)
        else:
            des = ''.join([c if c in string.printable else '[0x%s]'%binascii.b2a_hex(c) for c in src])
        return des
                
            
    def onRcvHEX(self, event):
        MainFrameBase.MainFrameBase.onRcvHEX(self, event)
        self.rcvType = self.TYPE_HEX
        self.m_statusBar.SetStatusText(u'接收区HEX显示')    
    
    def onRcvASC(self, event):
        MainFrameBase.MainFrameBase.onRcvASC(self, event)
        self.rcvType = self.TYPE_ASC
        self.m_statusBar.SetStatusText(u'接收区ASCII显示')
    
    def onSndHEX(self, event):
        MainFrameBase.MainFrameBase.onSndHEX(self, event)
        self.sendType = self.TYPE_HEX
        self.m_statusBar.SetStatusText(u'发送区HEX显示')
    
    def onSndASC(self, event):
        MainFrameBase.MainFrameBase.onSndASC(self, event)
        self.sendType = self.TYPE_ASC
        self.m_statusBar.SetStatusText(u'发送区ASCII显示')
        
    def onRcvClear(self, event):
        self.rcvbuf = []
        self.newrcvbuf = []
        self.m_recvarea.SetValue('')
        self.m_statusBar.SetStatusText(u'接收区已经清空')
        
    def onRcvSave(self, event):
        MainFrameBase.MainFrameBase.onRcvSave(self, event)
        choice = wx.GetSingleChoiceIndex(u"选择保存形式", "保存形式", ['原始数据','字符','十六进制字符'], parent=None)
        print choice
        data = ''.join(self.rcvbuf)

        if self.rcvType == self.TYPE_HEX:
            try:
                data = bytearray.fromhex(data)
            except ValueError,e:
                wx.MessageBox(u'不可识别的十六进制字符串！请检查输入内容！\n%s'%str(e), u"非法内容",wx.OK | wx.ICON_ERROR)
                return 
            

        if choice == -1:
            return
        elif choice == 0:
            wildcard = u"二进制文件(*.*)|*.*"
            outputdata = data
            opentype = 'wb'
        elif choice == 1:
            wildcard = u"文本文件 (*.txt)|*.txt"
            outputdata = data
            opentype = 'w'
        elif choice == 2:
            wildcard = u"文本文件 (*.txt)|*.txt"
            outputdata = self.stringToHexString(str(data))
            opentype = 'w'
        print r'%s'%outputdata
        dialog = wx.FileDialog(None, u"保存内容到...", os.getcwd(),
                "", wildcard, wx.SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            filepath = dialog.GetPath()
            try:
                f = open(filepath,opentype)
                f.write(outputdata)
                f.close()
                self.m_statusBar.SetStatusText(u'文件"%s"已经保存。'%filepath)
                wx.MessageBox(u'文件"%s"已经保存。'%filepath, u"保存成功",wx.OK | wx.ICON_INFORMATION)
            except Exception,e:
                wx.MessageBox(u'文件"%s"保存失败。'%filepath, u"保存失败",wx.OK | wx.ICON_ERROR)
                self.m_statusBar.SetStatusText(u'文件"%s"保存发生错误'%filepath)    
        dialog.Destroy()
        
        


        
    def onBINEnter(self, event):
        #MainFrameBase.MainFrameBase.onBINEnter(self, event)
        try:
            x = int(self.m_textCtrl_calcBIN.GetValue(),2)
            self.m_textCtrl_calcDEC.SetValue(str(x))
            self.m_textCtrl_calcHEX.SetValue("%X"%x)           
        except ValueError,e:
            wx.MessageBox(u'非法输入！ \n请检查输入内容。\n%s'%e, u"非法输入",wx.OK | wx.ICON_ERROR)
            self.m_statusBar.SetStatusText(u'非法输入！')    
    
    def onHEXEnter( self, event ):
        try:
            x = int(self.m_textCtrl_calcHEX.GetValue(),16)
            self.m_textCtrl_calcDEC.SetValue(str(x))
            self.m_textCtrl_calcBIN.SetValue(bin(x).replace('0b',''))           
        except ValueError,e:
            wx.MessageBox(u'非法输入！ \n请检查输入内容。\n%s'%e, u"非法输入",wx.OK | wx.ICON_ERROR)
            self.m_statusBar.SetStatusText(u'非法输入！')
    
    def onDECEnter( self, event ):
        try:
            x = int(self.m_textCtrl_calcDEC.GetValue(),10)
            self.m_textCtrl_calcHEX.SetValue('%X'%x)
            self.m_textCtrl_calcBIN.SetValue(bin(x).replace('0b',''))           
        except ValueError,e:
            wx.MessageBox(u'非法输入！ \n请检查输入内容。\n%s'%e, u"非法输入",wx.OK | wx.ICON_ERROR)
            self.m_statusBar.SetStatusText(u'非法输入！')
        
    def onDClkStatusBar(self, event):
        MainFrameBase.MainFrameBase.onDClkStatusBar(self, event)
        self.tc.clear()
    
    def onSendEnter(self, event):
        MainFrameBase.MainFrameBase.onSendEnter(self, event)
        if len(self.m_textCtrl_send.GetValue()):
            self.sendInputtedData()
    
    def onSendChar(self, event):
        
        keycode = event.GetKeyCode()
        
        if keycode == wx.WXK_UP:
            self.m_textCtrl_send.SetValue(self.history.getByRel(-1))
            self.m_textCtrl_send.SetInsertionPoint(len(self.m_textCtrl_send.GetValue()))
        elif keycode == wx.WXK_DOWN:
            self.m_textCtrl_send.SetValue(self.history.getByRel(1))
            self.m_textCtrl_send.SetInsertionPoint(len(self.m_textCtrl_send.GetValue()))
        else:
            MainFrameBase.MainFrameBase.onSendChar(self, event)
            
    
    def onSndBtn(self, event):
        if len(self.m_textCtrl_send.GetValue()):
            MainFrameBase.MainFrameBase.onSndBtn(self, event)
            self.sendInputtedData()
        
    
    def sendInputtedData(self):
        
        self.history.add(self.m_textCtrl_send.GetValue())
        data=''
        
        if self.sendType == self.TYPE_HEX:          
            for each in self.m_textCtrl_send.GetValue().encode('ascii','ignore').split():
                data+=chr(int(each,16))

        elif self.sendType == self.TYPE_ASC:
            data = self.m_textCtrl_send.GetValue().encode('ascii','ignore')
        
        (count,tempstr) = self.dev.sendData(data)
        
        tempstr="Send(%d):%s"%(count,self.stringToHexString(tempstr))
        self.SetStatusText(tempstr,0)
        self.tc.updateData(0, count)
        if self.m_checkBox_clear_on_sent.GetValue():
            self.m_textCtrl_send.SetValue("")
                
        
        
    def stringToHexString(self, src):
        des = ""
        for i in range(0,len(src)):
            des += "%s "%binascii.b2a_hex(src[i]).upper()
        return des
    
    def onSaveSettings(self, event):
        #MainFrameBase.MainFrameBase.onSaveSettings(self, event)
        dialog = wx.FileDialog(None, u"保存设置到...", os.getcwd(),
                "sasetting", u"设置文件 (*.sas)|*.sas", wx.SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            filepath = dialog.GetPath()
            try:
                pfio = PickleFileIO.PickleFileIO(filepath)
                pfio.save(self.sSettings)
                self.m_statusBar.SetStatusText(u'设置"%s"已经保存。'%filepath)
                wx.MessageBox(u'设置"%s"已经保存。'%filepath, u"保存成功",wx.OK | wx.ICON_INFORMATION)
            except Exception,e:
                wx.MessageBox(u'设置"%s"保存失败。\n%s'%(filepath,str(e)), u"保存失败",wx.OK | wx.ICON_ERROR)
                self.m_statusBar.SetStatusText(u'设置"%s"保存发生错误'%filepath)    
        dialog.Destroy()
        
    def onLoadSettings(self, event):
        #MainFrameBase.MainFrameBase.onSaveSettings(self, event)
        dialog = wx.FileDialog(None, u"读取设置", os.getcwd(),
                "", u"设置文件 (*.sas)|*.sas", wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            filepath = dialog.GetPath()
            try:
                pfio = PickleFileIO.PickleFileIO(filepath)
                self.sSettings = pfio.load()
                self.applySettings()
                self.m_statusBar.SetStatusText(u'设置"%s"已经应用。'%filepath)
                wx.MessageBox(u'设置"%s"已经应用。'%filepath, u"设置成功",wx.OK | wx.ICON_INFORMATION)
            except (EOFError,IOError),e:
                wx.MessageBox(u'设置"%s"应用失败。\n%s'%(filepath,str(e)), u"设置失败",wx.OK | wx.ICON_ERROR)
                self.m_statusBar.SetStatusText(u'设置"%s"应用发生错误'%filepath)    
        dialog.Destroy()
     
    def onAbout(self, event):
        #MainFrameBase.MainFrameBase.onAbout(self, event)
        wx.MessageBox(u'串口助手 V2014.03.21\nGroundMelon@gmail.com', u"关于",wx.OK | wx.ICON_INFORMATION)
        
    def OnXorEnter(self, event ):
        event.Skip()
        s = self.m_textCtrl_xor.GetValue()
        self.m_textCtrl_xor.SetValue(self.check_xor(s))
    
    def check_xor(self, s):
        lst = s.split()
        print("lst=",lst)
        x=0
        for each in lst:
            x=x^int(each,16)
        return hex(x)
        
    
class InputHistory(object):
    def __init__(self,window):
        self.window = window
        self.history=[]
        self.cursor = -1
    
    def add(self,s):
        self.history.append(s)
        self.cursor = len(self.history)    
    
    def getByRel(self,rel):
        ret = ""
        try:
            
            if self.cursor+rel == -1:
                ret = self.history[0]
                raise IndexError
            if self.cursor+rel == len(self.history):
                ret = self.history[self.cursor]
                raise IndexError                        
            ret = self.history[self.cursor+rel]
            self.cursor = self.cursor+rel
            self.window.SetStatusText(u"历史记录[%d]:%s"%(self.cursor+1,ret),0)
        except IndexError:
            self.window.SetStatusText(u"没有更多历史记录",0)
        return ret
    
    def getByAbs(self,cur):
        try:
            if cur == -1:
                raise IndexError
            ret = self.history[cur]
            self.window.SetStatusText(u"历史记录:%s"%ret,0)
        except IndexError:
            self.window.setStatusText(u"没有更多历史记录",0)
            ret = ""
        return ret
        

class TrnsConter(object):
    ''' 计数器类'''
    def __init__(self,window):
        self.window = window
        self.rx = 0
        self.tx = 0
        self.updateDisplay()
        
    def updateData(self,rx,tx):
        self.rx += rx
        self.tx += tx
        #self.updateDisplay()
    
    def updateDisplay(self):
        self.window.SetStatusText(u"RX:%d  TX:%d  双击此处清零"%(self.rx,self.tx),1)
    
    def clear(self):
        self.rx = 0
        self.tx = 0
        self.updateDisplay()


class App(wx.App):
    
    def OnInit(self):
        self.dev = SerialOperation.MySerial()
        
        self.frame = MainFrame(self.dev)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        
        return True
    
    def OnExit(self):
        if self.dev.ser.isOpen():
            print("Closing dev")
            self.dev.ser.close()
        
        print('Exit APP...')
        
        
if __name__ == '__main__':
    app = App(redirect=False)
    app.MainLoop()

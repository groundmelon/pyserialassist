# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SerialAssist by Groundmelon@gmail.com", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menu_save = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"保存设置(&S)", u"保存串口设置到文件", wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menu_save )
		
		self.m_menu_load = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"读取设置(&L)", u"从文件读取串口设置", wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menu_load )
		
		self.m_menu_file.AppendSeparator()
		
		self.exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"退出(&E)", u"退出程序", wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.exit )
		
		self.m_menubar.Append( self.m_menu_file, u"文件(&F)" ) 
		
		self.m_menu_edit = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu_edit, wx.ID_ANY, u"复制", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_edit.AppendItem( self.m_menuItem5 )
		self.m_menuItem5.Enable( False )
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu_edit, wx.ID_ANY, u"粘贴", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_edit.AppendItem( self.m_menuItem6 )
		self.m_menuItem6.Enable( False )
		
		self.m_menubar.Append( self.m_menu_edit, u"编辑(&E)" ) 
		
		self.m_menu_help = wx.Menu()
		self.m_menu_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"关于(&A)", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_menu_about )
		
		self.m_menubar.Append( self.m_menu_help, u"帮助(&H)" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		self.m_statusBar = self.CreateStatusBar( 2, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer0 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		fgSizer1 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizerSerialOption = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"串口设置" ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText33 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"串口信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gbSizer2.Add( self.m_staticText33, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button_checkCOM = wx.Button( self.m_panel1, wx.ID_ANY, u"查看", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		gbSizer2.Add( self.m_button_checkCOM, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"选择COM口", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gbSizer2.Add( self.m_staticText34, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice_comChoices = []
		self.m_choice_com = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_comChoices, 0 )
		self.m_choice_com.SetSelection( 0 )
		gbSizer2.Add( self.m_choice_com, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"波特率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gbSizer2.Add( self.m_staticText35, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice_baudrateChoices = []
		self.m_choice_baudrate = wx.ComboBox( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_baudrateChoices, 0 )
		gbSizer2.Add( self.m_choice_baudrate, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText351 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"校验方式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText351.Wrap( -1 )
		gbSizer2.Add( self.m_staticText351, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice_parityChoices = [ u"None", u"Even", u"Odd", u"Mask", u"Space" ]
		self.m_choice_parity = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_parityChoices, 0 )
		self.m_choice_parity.SetSelection( 0 )
		gbSizer2.Add( self.m_choice_parity, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText3511 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"数据位", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3511.Wrap( -1 )
		gbSizer2.Add( self.m_staticText3511, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice_databitsChoices = [ u"5", u"6", u"7", u"8" ]
		self.m_choice_databits = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_databitsChoices, 0 )
		self.m_choice_databits.SetSelection( 0 )
		gbSizer2.Add( self.m_choice_databits, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText35111 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"停止位", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35111.Wrap( -1 )
		gbSizer2.Add( self.m_staticText35111, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice_stopbitsChoices = [ u"1", u"1.5", u"2" ]
		self.m_choice_stopbits = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_stopbitsChoices, 0 )
		self.m_choice_stopbits.SetSelection( 0 )
		gbSizer2.Add( self.m_choice_stopbits, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox_hardFlowCtrl = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"硬件流控", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_checkBox_hardFlowCtrl, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_checkBox_softFlowCtrl = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"软件流控", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_checkBox_softFlowCtrl, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_toggleBtn_serial = wx.ToggleButton( self.m_panel1, wx.ID_ANY, u"建立连接", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_toggleBtn_serial, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		sbSizerSerialOption.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( sbSizerSerialOption, 1, 0, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"接收区" ), wx.VERTICAL )
		
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_recvarea = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_WORDWRAP )
		self.m_recvarea.SetMaxLength( 0 ) 
		self.m_recvarea.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Consolas" ) )
		self.m_recvarea.SetMinSize( wx.Size( 400,200 ) )
		
		gbSizer4.Add( self.m_recvarea, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_radioBtn_rHEX = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"HEX", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		gbSizer4.Add( self.m_radioBtn_rHEX, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_radioBtn_rASCII = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"ASCII", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn_rASCII.SetValue( True ) 
		gbSizer4.Add( self.m_radioBtn_rASCII, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button_save_recv = wx.Button( self.m_panel1, wx.ID_ANY, u"保存接收区", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_button_save_recv, wx.GBPosition( 1, 3 ), wx.GBSpan( 2, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button_clear_recv = wx.Button( self.m_panel1, wx.ID_ANY, u"清除接收区", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_button_clear_recv, wx.GBPosition( 1, 4 ), wx.GBSpan( 2, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		gbSizer4.AddGrowableCol( 0 )
		gbSizer4.AddGrowableRow( 0 )
		
		sbSizer2.Add( gbSizer4, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"进制转换" ), wx.HORIZONTAL )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText9 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"BIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gbSizer3.Add( self.m_staticText9, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl_calcBIN = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_textCtrl_calcBIN.SetMaxLength( 0 ) 
		gbSizer3.Add( self.m_textCtrl_calcBIN, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"HEX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gbSizer3.Add( self.m_staticText10, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl_calcHEX = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_textCtrl_calcHEX.SetMaxLength( 0 ) 
		gbSizer3.Add( self.m_textCtrl_calcHEX, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"DEC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gbSizer3.Add( self.m_staticText12, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl_calcDEC = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_textCtrl_calcDEC.SetMaxLength( 0 ) 
		gbSizer3.Add( self.m_textCtrl_calcDEC, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		sbSizer3.Add( gbSizer3, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"发送区" ), wx.VERTICAL )
		
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_textCtrl_send = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_textCtrl_send.SetMaxLength( 0 ) 
		gbSizer5.Add( self.m_textCtrl_send, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_button_send = wx.Button( self.m_panel1, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.m_button_send, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticTextHistoryPrompt = wx.StaticText( self.m_panel1, wx.ID_ANY, u"按上下键可调出历史记录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextHistoryPrompt.Wrap( -1 )
		gbSizer5.Add( self.m_staticTextHistoryPrompt, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox_clear_on_sent = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"发送后清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_clear_on_sent.SetValue(True) 
		gbSizer5.Add( self.m_checkBox_clear_on_sent, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"异或运算", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gbSizer5.Add( self.m_staticText11, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_textCtrl_xor = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PROCESS_ENTER )
		self.m_textCtrl_xor.SetMaxLength( 0 ) 
		gbSizer5.Add( self.m_textCtrl_xor, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.m_radioBtn_sHEX = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"HEX", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		gbSizer5.Add( self.m_radioBtn_sHEX, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_radioBtn_sASCII = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"ASCII", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn_sASCII.SetValue( True ) 
		gbSizer5.Add( self.m_radioBtn_sASCII, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		gbSizer5.AddGrowableCol( 0 )
		
		sbSizer4.Add( gbSizer5, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer0.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer0 )
		self.Layout()
		bSizer0.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.onSaveSettings, id = self.m_menu_save.GetId() )
		self.Bind( wx.EVT_MENU, self.onLoadSettings, id = self.m_menu_load.GetId() )
		self.Bind( wx.EVT_MENU, self.onQuit, id = self.exit.GetId() )
		self.Bind( wx.EVT_MENU, self.onAbout, id = self.m_menu_about.GetId() )
		self.m_statusBar.Bind( wx.EVT_LEFT_DCLICK, self.onDClkStatusBar )
		self.m_button_checkCOM.Bind( wx.EVT_BUTTON, self.onSeeComInfo )
		self.m_toggleBtn_serial.Bind( wx.EVT_TOGGLEBUTTON, self.onSerialToggle )
		self.m_radioBtn_rHEX.Bind( wx.EVT_RADIOBUTTON, self.onRcvHEX )
		self.m_radioBtn_rASCII.Bind( wx.EVT_RADIOBUTTON, self.onRcvASC )
		self.m_button_save_recv.Bind( wx.EVT_BUTTON, self.onRcvSave )
		self.m_button_clear_recv.Bind( wx.EVT_BUTTON, self.onRcvClear )
		self.m_textCtrl_calcBIN.Bind( wx.EVT_TEXT_ENTER, self.onBINEnter )
		self.m_textCtrl_calcHEX.Bind( wx.EVT_TEXT_ENTER, self.onHEXEnter )
		self.m_textCtrl_calcDEC.Bind( wx.EVT_TEXT_ENTER, self.onDECEnter )
		self.m_textCtrl_send.Bind( wx.EVT_CHAR, self.onSendChar )
		self.m_textCtrl_send.Bind( wx.EVT_TEXT_ENTER, self.onSendEnter )
		self.m_button_send.Bind( wx.EVT_BUTTON, self.onSndBtn )
		self.m_checkBox_clear_on_sent.Bind( wx.EVT_CHECKBOX, self.On_CHKBOX_clear_on_send )
		self.m_textCtrl_xor.Bind( wx.EVT_TEXT_ENTER, self.OnXorEnter )
		self.m_radioBtn_sHEX.Bind( wx.EVT_RADIOBUTTON, self.onSndHEX )
		self.m_radioBtn_sASCII.Bind( wx.EVT_RADIOBUTTON, self.onSndASC )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSaveSettings( self, event ):
		event.Skip()
	
	def onLoadSettings( self, event ):
		event.Skip()
	
	def onQuit( self, event ):
		event.Skip()
	
	def onAbout( self, event ):
		event.Skip()
	
	def onDClkStatusBar( self, event ):
		event.Skip()
	
	def onSeeComInfo( self, event ):
		event.Skip()
	
	def onSerialToggle( self, event ):
		event.Skip()
	
	def onRcvHEX( self, event ):
		event.Skip()
	
	def onRcvASC( self, event ):
		event.Skip()
	
	def onRcvSave( self, event ):
		event.Skip()
	
	def onRcvClear( self, event ):
		event.Skip()
	
	def onBINEnter( self, event ):
		event.Skip()
	
	def onHEXEnter( self, event ):
		event.Skip()
	
	def onDECEnter( self, event ):
		event.Skip()
	
	def onSendChar( self, event ):
		event.Skip()
	
	def onSendEnter( self, event ):
		event.Skip()
	
	def onSndBtn( self, event ):
		event.Skip()
	
	def On_CHKBOX_clear_on_send( self, event ):
		event.Skip()
	
	def OnXorEnter( self, event ):
		event.Skip()
	
	def onSndHEX( self, event ):
		event.Skip()
	
	def onSndASC( self, event ):
		event.Skip()
	

###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer47 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_htmlWin_about = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,173 ), wx.html.HW_SCROLLBAR_AUTO )
		bSizer47.Add( self.m_htmlWin_about, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer47 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	


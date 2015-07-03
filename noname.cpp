///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Feb 26 2014)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MainFrameBase::MainFrameBase( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	m_menubar = new wxMenuBar( 0 );
	m_menu_file = new wxMenu();
	wxMenuItem* m_menu_save;
	m_menu_save = new wxMenuItem( m_menu_file, wxID_ANY, wxString( wxT("保存设置(&S)") ) , wxT("保存串口设置到文件"), wxITEM_NORMAL );
	m_menu_file->Append( m_menu_save );
	
	wxMenuItem* m_menu_load;
	m_menu_load = new wxMenuItem( m_menu_file, wxID_ANY, wxString( wxT("读取设置(&L)") ) , wxT("从文件读取串口设置"), wxITEM_NORMAL );
	m_menu_file->Append( m_menu_load );
	
	m_menu_file->AppendSeparator();
	
	wxMenuItem* exit;
	exit = new wxMenuItem( m_menu_file, wxID_ANY, wxString( wxT("退出(&E)") ) , wxT("退出程序"), wxITEM_NORMAL );
	m_menu_file->Append( exit );
	
	m_menubar->Append( m_menu_file, wxT("文件(&F)") ); 
	
	m_menu_edit = new wxMenu();
	wxMenuItem* m_menuItem5;
	m_menuItem5 = new wxMenuItem( m_menu_edit, wxID_ANY, wxString( wxT("复制") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu_edit->Append( m_menuItem5 );
	m_menuItem5->Enable( false );
	
	wxMenuItem* m_menuItem6;
	m_menuItem6 = new wxMenuItem( m_menu_edit, wxID_ANY, wxString( wxT("粘贴") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu_edit->Append( m_menuItem6 );
	m_menuItem6->Enable( false );
	
	m_menubar->Append( m_menu_edit, wxT("编辑(&E)") ); 
	
	m_menu_help = new wxMenu();
	wxMenuItem* m_menu_about;
	m_menu_about = new wxMenuItem( m_menu_help, wxID_ANY, wxString( wxT("关于(&A)") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu_help->Append( m_menu_about );
	
	m_menubar->Append( m_menu_help, wxT("帮助(&H)") ); 
	
	this->SetMenuBar( m_menubar );
	
	m_statusBar = this->CreateStatusBar( 2, wxST_SIZEGRIP, wxID_ANY );
	wxBoxSizer* bSizer0;
	bSizer0 = new wxBoxSizer( wxVERTICAL );
	
	m_panel1 = new wxPanel( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	m_panel1->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_MENU ) );
	
	wxGridBagSizer* gbSizer1;
	gbSizer1 = new wxGridBagSizer( 0, 0 );
	gbSizer1->SetFlexibleDirection( wxBOTH );
	gbSizer1->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	wxStaticBoxSizer* sbSizerSerialOption;
	sbSizerSerialOption = new wxStaticBoxSizer( new wxStaticBox( m_panel1, wxID_ANY, wxT("串口设置") ), wxVERTICAL );
	
	wxGridBagSizer* gbSizer2;
	gbSizer2 = new wxGridBagSizer( 0, 0 );
	gbSizer2->SetFlexibleDirection( wxBOTH );
	gbSizer2->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_staticText33 = new wxStaticText( m_panel1, wxID_ANY, wxT("串口信息"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText33->Wrap( -1 );
	gbSizer2->Add( m_staticText33, wxGBPosition( 0, 0 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	m_button_checkCOM = new wxButton( m_panel1, wxID_ANY, wxT("查看"), wxDefaultPosition, wxSize( 80,-1 ), 0 );
	gbSizer2->Add( m_button_checkCOM, wxGBPosition( 0, 1 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	m_staticText34 = new wxStaticText( m_panel1, wxID_ANY, wxT("选择COM口"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText34->Wrap( -1 );
	gbSizer2->Add( m_staticText34, wxGBPosition( 1, 0 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	wxArrayString m_choice_comChoices;
	m_choice_com = new wxChoice( m_panel1, wxID_ANY, wxDefaultPosition, wxSize( 80,-1 ), m_choice_comChoices, 0 );
	m_choice_com->SetSelection( 0 );
	gbSizer2->Add( m_choice_com, wxGBPosition( 1, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText35 = new wxStaticText( m_panel1, wxID_ANY, wxT("波特率"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText35->Wrap( -1 );
	gbSizer2->Add( m_staticText35, wxGBPosition( 2, 0 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	wxArrayString m_choice_baudrateChoices;
	m_choice_baudrate = new wxChoice( m_panel1, wxID_ANY, wxDefaultPosition, wxSize( 80,-1 ), m_choice_baudrateChoices, 0 );
	m_choice_baudrate->SetSelection( 0 );
	gbSizer2->Add( m_choice_baudrate, wxGBPosition( 2, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText351 = new wxStaticText( m_panel1, wxID_ANY, wxT("校验方式"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText351->Wrap( -1 );
	gbSizer2->Add( m_staticText351, wxGBPosition( 3, 0 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	wxString m_choice_parityChoices[] = { wxT("None"), wxT("Even"), wxT("Odd"), wxT("Mask"), wxT("Space") };
	int m_choice_parityNChoices = sizeof( m_choice_parityChoices ) / sizeof( wxString );
	m_choice_parity = new wxChoice( m_panel1, wxID_ANY, wxDefaultPosition, wxSize( 80,-1 ), m_choice_parityNChoices, m_choice_parityChoices, 0 );
	m_choice_parity->SetSelection( 0 );
	gbSizer2->Add( m_choice_parity, wxGBPosition( 3, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText3511 = new wxStaticText( m_panel1, wxID_ANY, wxT("数据位"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3511->Wrap( -1 );
	gbSizer2->Add( m_staticText3511, wxGBPosition( 4, 0 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	wxString m_choice_databitsChoices[] = { wxT("5"), wxT("6"), wxT("7"), wxT("8") };
	int m_choice_databitsNChoices = sizeof( m_choice_databitsChoices ) / sizeof( wxString );
	m_choice_databits = new wxChoice( m_panel1, wxID_ANY, wxDefaultPosition, wxSize( 80,-1 ), m_choice_databitsNChoices, m_choice_databitsChoices, 0 );
	m_choice_databits->SetSelection( 0 );
	gbSizer2->Add( m_choice_databits, wxGBPosition( 4, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText35111 = new wxStaticText( m_panel1, wxID_ANY, wxT("停止位"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText35111->Wrap( -1 );
	gbSizer2->Add( m_staticText35111, wxGBPosition( 5, 0 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	wxString m_choice_stopbitsChoices[] = { wxT("1"), wxT("1.5"), wxT("2") };
	int m_choice_stopbitsNChoices = sizeof( m_choice_stopbitsChoices ) / sizeof( wxString );
	m_choice_stopbits = new wxChoice( m_panel1, wxID_ANY, wxDefaultPosition, wxSize( 80,-1 ), m_choice_stopbitsNChoices, m_choice_stopbitsChoices, 0 );
	m_choice_stopbits->SetSelection( 0 );
	gbSizer2->Add( m_choice_stopbits, wxGBPosition( 5, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_checkBox_hardFlowCtrl = new wxCheckBox( m_panel1, wxID_ANY, wxT("硬件流控"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer2->Add( m_checkBox_hardFlowCtrl, wxGBPosition( 6, 0 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	m_checkBox_softFlowCtrl = new wxCheckBox( m_panel1, wxID_ANY, wxT("软件流控"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer2->Add( m_checkBox_softFlowCtrl, wxGBPosition( 6, 1 ), wxGBSpan( 1, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	m_toggleBtn_serial = new wxToggleButton( m_panel1, wxID_ANY, wxT("建立连接"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer2->Add( m_toggleBtn_serial, wxGBPosition( 7, 0 ), wxGBSpan( 1, 2 ), wxALIGN_CENTER|wxALL, 5 );
	
	
	sbSizerSerialOption->Add( gbSizer2, 1, wxEXPAND, 5 );
	
	
	gbSizer1->Add( sbSizerSerialOption, wxGBPosition( 0, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );
	
	wxStaticBoxSizer* sbSizer2;
	sbSizer2 = new wxStaticBoxSizer( new wxStaticBox( m_panel1, wxID_ANY, wxT("接收区") ), wxVERTICAL );
	
	wxGridBagSizer* gbSizer4;
	gbSizer4 = new wxGridBagSizer( 0, 0 );
	gbSizer4->SetFlexibleDirection( wxBOTH );
	gbSizer4->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_recvarea = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( -1,-1 ), wxTE_MULTILINE|wxTE_WORDWRAP );
	m_recvarea->SetMaxLength( 0 ); 
	gbSizer4->Add( m_recvarea, wxGBPosition( 0, 0 ), wxGBSpan( 1, 5 ), wxALL|wxEXPAND, 5 );
	
	m_radioBtn_rHEX = new wxRadioButton( m_panel1, wxID_ANY, wxT("HEX"), wxDefaultPosition, wxDefaultSize, wxRB_GROUP );
	m_radioBtn_rHEX->SetValue( true ); 
	gbSizer4->Add( m_radioBtn_rHEX, wxGBPosition( 1, 2 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_radioBtn_rASCII = new wxRadioButton( m_panel1, wxID_ANY, wxT("ASCII"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer4->Add( m_radioBtn_rASCII, wxGBPosition( 2, 2 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_button_save_recv = new wxButton( m_panel1, wxID_ANY, wxT("保存接收区"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer4->Add( m_button_save_recv, wxGBPosition( 1, 3 ), wxGBSpan( 2, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	m_button_clear_recv = new wxButton( m_panel1, wxID_ANY, wxT("清除接收区"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer4->Add( m_button_clear_recv, wxGBPosition( 1, 4 ), wxGBSpan( 2, 1 ), wxALIGN_CENTER|wxALL, 5 );
	
	
	sbSizer2->Add( gbSizer4, 1, wxEXPAND, 5 );
	
	
	gbSizer1->Add( sbSizer2, wxGBPosition( 0, 1 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );
	
	wxStaticBoxSizer* sbSizer3;
	sbSizer3 = new wxStaticBoxSizer( new wxStaticBox( m_panel1, wxID_ANY, wxT("进制转换") ), wxHORIZONTAL );
	
	wxGridBagSizer* gbSizer3;
	gbSizer3 = new wxGridBagSizer( 0, 0 );
	gbSizer3->SetFlexibleDirection( wxBOTH );
	gbSizer3->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_staticText9 = new wxStaticText( m_panel1, wxID_ANY, wxT("BIN"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText9->Wrap( -1 );
	gbSizer3->Add( m_staticText9, wxGBPosition( 0, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textCtrl_calcBIN = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_PROCESS_ENTER );
	m_textCtrl_calcBIN->SetMaxLength( 0 ); 
	gbSizer3->Add( m_textCtrl_calcBIN, wxGBPosition( 0, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText10 = new wxStaticText( m_panel1, wxID_ANY, wxT("HEX"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText10->Wrap( -1 );
	gbSizer3->Add( m_staticText10, wxGBPosition( 1, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textCtrl_calcHEX = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_PROCESS_ENTER );
	m_textCtrl_calcHEX->SetMaxLength( 0 ); 
	gbSizer3->Add( m_textCtrl_calcHEX, wxGBPosition( 1, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText12 = new wxStaticText( m_panel1, wxID_ANY, wxT("DEC"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText12->Wrap( -1 );
	gbSizer3->Add( m_staticText12, wxGBPosition( 2, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textCtrl_calcDEC = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_PROCESS_ENTER );
	m_textCtrl_calcDEC->SetMaxLength( 0 ); 
	gbSizer3->Add( m_textCtrl_calcDEC, wxGBPosition( 2, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	
	sbSizer3->Add( gbSizer3, 1, wxEXPAND, 5 );
	
	
	gbSizer1->Add( sbSizer3, wxGBPosition( 1, 0 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );
	
	wxStaticBoxSizer* sbSizer4;
	sbSizer4 = new wxStaticBoxSizer( new wxStaticBox( m_panel1, wxID_ANY, wxT("发送区") ), wxVERTICAL );
	
	wxGridBagSizer* gbSizer5;
	gbSizer5 = new wxGridBagSizer( 0, 0 );
	gbSizer5->SetFlexibleDirection( wxBOTH );
	gbSizer5->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_textCtrl_send = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_PROCESS_ENTER );
	m_textCtrl_send->SetMaxLength( 0 ); 
	gbSizer5->Add( m_textCtrl_send, wxGBPosition( 0, 0 ), wxGBSpan( 1, 3 ), wxALIGN_CENTER|wxALL|wxEXPAND, 5 );
	
	m_button_send = new wxButton( m_panel1, wxID_ANY, wxT("发送"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer5->Add( m_button_send, wxGBPosition( 0, 4 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticTextHistoryPrompt = new wxStaticText( m_panel1, wxID_ANY, wxT("按上下键可调出历史记录"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextHistoryPrompt->Wrap( -1 );
	gbSizer5->Add( m_staticTextHistoryPrompt, wxGBPosition( 1, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_checkBox_clear_on_sent = new wxCheckBox( m_panel1, wxID_ANY, wxT("发送后清空"), wxDefaultPosition, wxDefaultSize, 0 );
	m_checkBox_clear_on_sent->SetValue(true); 
	gbSizer5->Add( m_checkBox_clear_on_sent, wxGBPosition( 1, 2 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText11 = new wxStaticText( m_panel1, wxID_ANY, wxT("异或运算"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText11->Wrap( -1 );
	gbSizer5->Add( m_staticText11, wxGBPosition( 2, 0 ), wxGBSpan( 1, 1 ), wxALIGN_RIGHT|wxALL, 5 );
	
	m_textCtrl_xor = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 150,-1 ), wxTE_PROCESS_ENTER );
	m_textCtrl_xor->SetMaxLength( 0 ); 
	gbSizer5->Add( m_textCtrl_xor, wxGBPosition( 2, 1 ), wxGBSpan( 1, 2 ), wxALL, 5 );
	
	m_radioBtn_sHEX = new wxRadioButton( m_panel1, wxID_ANY, wxT("HEX"), wxDefaultPosition, wxDefaultSize, wxRB_GROUP );
	m_radioBtn_sHEX->SetValue( true ); 
	gbSizer5->Add( m_radioBtn_sHEX, wxGBPosition( 1, 4 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_radioBtn_sASCII = new wxRadioButton( m_panel1, wxID_ANY, wxT("ASCII"), wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer5->Add( m_radioBtn_sASCII, wxGBPosition( 2, 4 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	
	sbSizer4->Add( gbSizer5, 1, wxEXPAND, 5 );
	
	
	gbSizer1->Add( sbSizer4, wxGBPosition( 1, 1 ), wxGBSpan( 1, 1 ), wxEXPAND, 5 );
	
	
	m_panel1->SetSizer( gbSizer1 );
	m_panel1->Layout();
	gbSizer1->Fit( m_panel1 );
	bSizer0->Add( m_panel1, 1, wxEXPAND | wxALL, 0 );
	
	
	this->SetSizer( bSizer0 );
	this->Layout();
	bSizer0->Fit( this );
	
	this->Centre( wxBOTH );
	
	// Connect Events
	this->Connect( m_menu_save->GetId(), wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrameBase::onSaveSettings ) );
	this->Connect( m_menu_load->GetId(), wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrameBase::onLoadSettings ) );
	this->Connect( exit->GetId(), wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrameBase::onQuit ) );
	this->Connect( m_menu_about->GetId(), wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrameBase::onAbout ) );
	m_statusBar->Connect( wxEVT_LEFT_DCLICK, wxMouseEventHandler( MainFrameBase::onDClkStatusBar ), NULL, this );
	m_button_checkCOM->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onSeeComInfo ), NULL, this );
	m_toggleBtn_serial->Connect( wxEVT_COMMAND_TOGGLEBUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onSerialToggle ), NULL, this );
	m_radioBtn_rHEX->Connect( wxEVT_COMMAND_RADIOBUTTON_SELECTED, wxCommandEventHandler( MainFrameBase::onRcvHEX ), NULL, this );
	m_radioBtn_rASCII->Connect( wxEVT_COMMAND_RADIOBUTTON_SELECTED, wxCommandEventHandler( MainFrameBase::onRcvASC ), NULL, this );
	m_button_save_recv->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onRcvSave ), NULL, this );
	m_button_clear_recv->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onRcvClear ), NULL, this );
	m_textCtrl_calcBIN->Connect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::onBINEnter ), NULL, this );
	m_textCtrl_calcHEX->Connect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::onHEXEnter ), NULL, this );
	m_textCtrl_calcDEC->Connect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::onDECEnter ), NULL, this );
	m_textCtrl_send->Connect( wxEVT_CHAR, wxKeyEventHandler( MainFrameBase::onSendChar ), NULL, this );
	m_textCtrl_send->Connect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::onSendEnter ), NULL, this );
	m_button_send->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onSndBtn ), NULL, this );
	m_checkBox_clear_on_sent->Connect( wxEVT_COMMAND_CHECKBOX_CLICKED, wxCommandEventHandler( MainFrameBase::On_CHKBOX_clear_on_send ), NULL, this );
	m_textCtrl_xor->Connect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::OnXorEnter ), NULL, this );
	m_radioBtn_sHEX->Connect( wxEVT_COMMAND_RADIOBUTTON_SELECTED, wxCommandEventHandler( MainFrameBase::onSndHEX ), NULL, this );
	m_radioBtn_sASCII->Connect( wxEVT_COMMAND_RADIOBUTTON_SELECTED, wxCommandEventHandler( MainFrameBase::onSndASC ), NULL, this );
}

MainFrameBase::~MainFrameBase()
{
	// Disconnect Events
	this->Disconnect( wxID_ANY, wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrameBase::onSaveSettings ) );
	this->Disconnect( wxID_ANY, wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrameBase::onLoadSettings ) );
	this->Disconnect( wxID_ANY, wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrameBase::onQuit ) );
	this->Disconnect( wxID_ANY, wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrameBase::onAbout ) );
	m_statusBar->Disconnect( wxEVT_LEFT_DCLICK, wxMouseEventHandler( MainFrameBase::onDClkStatusBar ), NULL, this );
	m_button_checkCOM->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onSeeComInfo ), NULL, this );
	m_toggleBtn_serial->Disconnect( wxEVT_COMMAND_TOGGLEBUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onSerialToggle ), NULL, this );
	m_radioBtn_rHEX->Disconnect( wxEVT_COMMAND_RADIOBUTTON_SELECTED, wxCommandEventHandler( MainFrameBase::onRcvHEX ), NULL, this );
	m_radioBtn_rASCII->Disconnect( wxEVT_COMMAND_RADIOBUTTON_SELECTED, wxCommandEventHandler( MainFrameBase::onRcvASC ), NULL, this );
	m_button_save_recv->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onRcvSave ), NULL, this );
	m_button_clear_recv->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onRcvClear ), NULL, this );
	m_textCtrl_calcBIN->Disconnect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::onBINEnter ), NULL, this );
	m_textCtrl_calcHEX->Disconnect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::onHEXEnter ), NULL, this );
	m_textCtrl_calcDEC->Disconnect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::onDECEnter ), NULL, this );
	m_textCtrl_send->Disconnect( wxEVT_CHAR, wxKeyEventHandler( MainFrameBase::onSendChar ), NULL, this );
	m_textCtrl_send->Disconnect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::onSendEnter ), NULL, this );
	m_button_send->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrameBase::onSndBtn ), NULL, this );
	m_checkBox_clear_on_sent->Disconnect( wxEVT_COMMAND_CHECKBOX_CLICKED, wxCommandEventHandler( MainFrameBase::On_CHKBOX_clear_on_send ), NULL, this );
	m_textCtrl_xor->Disconnect( wxEVT_COMMAND_TEXT_ENTER, wxCommandEventHandler( MainFrameBase::OnXorEnter ), NULL, this );
	m_radioBtn_sHEX->Disconnect( wxEVT_COMMAND_RADIOBUTTON_SELECTED, wxCommandEventHandler( MainFrameBase::onSndHEX ), NULL, this );
	m_radioBtn_sASCII->Disconnect( wxEVT_COMMAND_RADIOBUTTON_SELECTED, wxCommandEventHandler( MainFrameBase::onSndASC ), NULL, this );
	
}

AboutDialog::AboutDialog( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxDialog( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer47;
	bSizer47 = new wxBoxSizer( wxVERTICAL );
	
	m_htmlWin_about = new wxHtmlWindow( this, wxID_ANY, wxDefaultPosition, wxSize( 300,173 ), wxHW_SCROLLBAR_AUTO );
	bSizer47->Add( m_htmlWin_about, 0, wxEXPAND, 5 );
	
	
	this->SetSizer( bSizer47 );
	this->Layout();
	
	this->Centre( wxBOTH );
}

AboutDialog::~AboutDialog()
{
}

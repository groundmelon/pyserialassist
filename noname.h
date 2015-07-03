///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Feb 26 2014)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/menu.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/statusbr.h>
#include <wx/stattext.h>
#include <wx/button.h>
#include <wx/choice.h>
#include <wx/checkbox.h>
#include <wx/tglbtn.h>
#include <wx/gbsizer.h>
#include <wx/sizer.h>
#include <wx/statbox.h>
#include <wx/textctrl.h>
#include <wx/radiobut.h>
#include <wx/panel.h>
#include <wx/frame.h>
#include <wx/html/htmlwin.h>
#include <wx/dialog.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MainFrameBase
///////////////////////////////////////////////////////////////////////////////
class MainFrameBase : public wxFrame 
{
	private:
	
	protected:
		wxMenuBar* m_menubar;
		wxMenu* m_menu_file;
		wxMenu* m_menu_edit;
		wxMenu* m_menu_help;
		wxStatusBar* m_statusBar;
		wxPanel* m_panel1;
		wxStaticText* m_staticText33;
		wxButton* m_button_checkCOM;
		wxStaticText* m_staticText34;
		wxChoice* m_choice_com;
		wxStaticText* m_staticText35;
		wxChoice* m_choice_baudrate;
		wxStaticText* m_staticText351;
		wxChoice* m_choice_parity;
		wxStaticText* m_staticText3511;
		wxChoice* m_choice_databits;
		wxStaticText* m_staticText35111;
		wxChoice* m_choice_stopbits;
		wxCheckBox* m_checkBox_hardFlowCtrl;
		wxCheckBox* m_checkBox_softFlowCtrl;
		wxToggleButton* m_toggleBtn_serial;
		wxTextCtrl* m_recvarea;
		wxRadioButton* m_radioBtn_rHEX;
		wxRadioButton* m_radioBtn_rASCII;
		wxButton* m_button_save_recv;
		wxButton* m_button_clear_recv;
		wxStaticText* m_staticText9;
		wxTextCtrl* m_textCtrl_calcBIN;
		wxStaticText* m_staticText10;
		wxTextCtrl* m_textCtrl_calcHEX;
		wxStaticText* m_staticText12;
		wxTextCtrl* m_textCtrl_calcDEC;
		wxTextCtrl* m_textCtrl_send;
		wxButton* m_button_send;
		wxStaticText* m_staticTextHistoryPrompt;
		wxCheckBox* m_checkBox_clear_on_sent;
		wxStaticText* m_staticText11;
		wxTextCtrl* m_textCtrl_xor;
		wxRadioButton* m_radioBtn_sHEX;
		wxRadioButton* m_radioBtn_sASCII;
		
		// Virtual event handlers, overide them in your derived class
		virtual void onSaveSettings( wxCommandEvent& event ) { event.Skip(); }
		virtual void onLoadSettings( wxCommandEvent& event ) { event.Skip(); }
		virtual void onQuit( wxCommandEvent& event ) { event.Skip(); }
		virtual void onAbout( wxCommandEvent& event ) { event.Skip(); }
		virtual void onDClkStatusBar( wxMouseEvent& event ) { event.Skip(); }
		virtual void onSeeComInfo( wxCommandEvent& event ) { event.Skip(); }
		virtual void onSerialToggle( wxCommandEvent& event ) { event.Skip(); }
		virtual void onRcvHEX( wxCommandEvent& event ) { event.Skip(); }
		virtual void onRcvASC( wxCommandEvent& event ) { event.Skip(); }
		virtual void onRcvSave( wxCommandEvent& event ) { event.Skip(); }
		virtual void onRcvClear( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBINEnter( wxCommandEvent& event ) { event.Skip(); }
		virtual void onHEXEnter( wxCommandEvent& event ) { event.Skip(); }
		virtual void onDECEnter( wxCommandEvent& event ) { event.Skip(); }
		virtual void onSendChar( wxKeyEvent& event ) { event.Skip(); }
		virtual void onSendEnter( wxCommandEvent& event ) { event.Skip(); }
		virtual void onSndBtn( wxCommandEvent& event ) { event.Skip(); }
		virtual void On_CHKBOX_clear_on_send( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnXorEnter( wxCommandEvent& event ) { event.Skip(); }
		virtual void onSndHEX( wxCommandEvent& event ) { event.Skip(); }
		virtual void onSndASC( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		MainFrameBase( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Serial Assist @ Groundmelon@gmail.com"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( -1,-1 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~MainFrameBase();
	
};

///////////////////////////////////////////////////////////////////////////////
/// Class AboutDialog
///////////////////////////////////////////////////////////////////////////////
class AboutDialog : public wxDialog 
{
	private:
	
	protected:
		wxHtmlWindow* m_htmlWin_about;
	
	public:
		
		AboutDialog( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 300,200 ), long style = wxDEFAULT_DIALOG_STYLE ); 
		~AboutDialog();
	
};

#endif //__NONAME_H__

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MainFrameTemplate
###########################################################################

class MainFrameTemplate ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GIF Viewer", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.BORDER_THEME|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 600,400 ), wx.DefaultSize )

        mainFrameSizer = wx.BoxSizer( wx.VERTICAL )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        mainPanelSizer = wx.BoxSizer( wx.VERTICAL )

        dirPickerSizer = wx.StaticBoxSizer( wx.StaticBox( self.mainPanel, wx.ID_ANY, u"Folder with GIFs" ), wx.VERTICAL )

        self.dirPicker = wx.DirPickerCtrl( dirPickerSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder with GIFs", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_USE_TEXTCTRL )
        dirPickerSizer.Add( self.dirPicker, 0, wx.ALL|wx.EXPAND, 5 )


        mainPanelSizer.Add( dirPickerSizer, 0, wx.ALL|wx.EXPAND, 5 )

        chosenDirAreaSizer = wx.BoxSizer( wx.HORIZONTAL )

        fileListSizer = wx.StaticBoxSizer( wx.StaticBox( self.mainPanel, wx.ID_ANY, u"Files in folder" ), wx.VERTICAL )

        fileListBoxChoices = []
        self.fileListBox = wx.ListBox( fileListSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, fileListBoxChoices, wx.LB_SINGLE )
        self.fileListBox.SetMinSize( wx.Size( 180,-1 ) )
        self.fileListBox.SetMaxSize( wx.Size( 230,-1 ) )

        fileListSizer.Add( self.fileListBox, 1, wx.ALL|wx.EXPAND, 0 )


        chosenDirAreaSizer.Add( fileListSizer, 0, wx.ALL|wx.EXPAND, 5 )

        imageAreaSizer = wx.StaticBoxSizer( wx.StaticBox( self.mainPanel, wx.ID_ANY, u"GIF" ), wx.VERTICAL )

        self.animationArea = wx.adv.AnimationCtrl( imageAreaSizer.GetStaticBox(), wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
        imageAreaSizer.Add( self.animationArea, 1, wx.ALL|wx.EXPAND, 5 )


        chosenDirAreaSizer.Add( imageAreaSizer, 1, wx.ALL|wx.EXPAND, 5 )


        mainPanelSizer.Add( chosenDirAreaSizer, 1, wx.EXPAND, 0 )


        self.mainPanel.SetSizer( mainPanelSizer )
        self.mainPanel.Layout()
        mainPanelSizer.Fit( self.mainPanel )
        mainFrameSizer.Add( self.mainPanel, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( mainFrameSizer )
        self.Layout()
        self.statusBar = self.CreateStatusBar( 1, wx.STB_ELLIPSIZE_END|wx.STB_SIZEGRIP, wx.ID_ANY )
        self.statusBar.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.statusBar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        self.statusBar.SetToolTip( u"status bar" )


        self.Centre( wx.BOTH )

        # Connect Events
        self.dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.onDirChangeHandler )
        self.fileListBox.Bind( wx.EVT_LISTBOX, self.onListItemSelect )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onDirChangeHandler( self, event ):
        event.Skip()

    def onListItemSelect( self, event ):
        event.Skip()



import os

from datetime import datetime
from threading import Timer

import wx
from gui import generated_gui as gui


class MainFrame(gui.MainFrameTemplate):

    def onDirChangeHandler( self, event ):
        self.dir_path = event.GetPath()
        self.populateFileList()

    def populateFileList(self):
        self.fileListBox.Clear()
        files_list = os.listdir(self.dir_path)
        for cur_file in files_list:
            if cur_file.endswith(".gif"):
                self.fileListBox.Append(cur_file)

    def onListItemSelect( self, event ):
        try:
            cur_gif = event.GetString()
            cur_filepath = os.path.join(self.dir_path, cur_gif)
            self.animationArea.LoadFile(cur_filepath)
            # print(self.animationArea.GetAnimation())
            self.animationArea.Play()
        except Exception as e:
            self.onExceptionOccur(e)
        
    def onExceptionOccur(self, err):
        '''
        Show error message in status bar and log error to file.
        '''
        def resetStatusBar():
            self.statusBar.SetBackgroundColour(wx.NullColour)
            self.statusBar.PopStatusText()

        self.statusBar.SetBackgroundColour(wx.RED)
        self.statusBar.PushStatusText(f"Error: {str(err)}")
        print(repr(err))
        print(str(err))
        with open("fails.log", "a") as log_f:
            log_f.write(str(datetime.now()))
            log_f.write('\t')
            log_f.write(repr(err))
            log_f.write('\n')
        # clean statusbar
        statusResetTimer = Timer(2.0, resetStatusBar)
        statusResetTimer.start()

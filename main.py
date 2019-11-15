import wx
from gui import main_frame


class MainApp(wx.App):
	def OnInit(self):
		mainFrame = main_frame.MainFrame(parent=None)
		mainFrame.Show()
		return True


if __name__ == "__main__":
    app = MainApp()
    # main_frame = viewer_ui.FrameMain(None)
    app.MainLoop()

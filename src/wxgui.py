import wx


class GeneralFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


def show_window():
    app = wx.App(redirect=True)
    # Redirect in the standard console, and not stdout/stderr
    general_window = GeneralFrame(None)  # Create an object [Instance] forms
    # (In the terminology wxwidgets this window)

    general_window.Show(True)
    app.MainLoop()

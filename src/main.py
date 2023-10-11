"""
Main wxStlViewer module

@copyright: 2023 Pavel Pertsev
@license: GNU GPL-3.0  (see LICENSE file) - provided as is, no warranty
"""

# import general python modules
import logging
import sys

# third party modules
import wx

# import project modules
from wxgui import GeneralFrame

if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET, filename="wxStlViewer.log", filemode="w")
    logging.info(f"Using Python {sys.version.split()[0]}")
    logging.info(f"Using wxPython {wx.version()}")

    app = wx.App()
    # Redirect in the standard console, and not stdout/stderr
    general_window = GeneralFrame(None)  # Create an object [Instance] forms
    # (In the terminology wxwidgets this window)

    general_window.Show(True)
    app.MainLoop()

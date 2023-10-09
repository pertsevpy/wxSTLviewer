"""
Main wxSTL viewer module
"""

# import general python modules
import logging, sys

# import project modules
# TODO: understand scopes and multiple imports after creating event handlers
from wxgui import *

if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET, filename="wxSTLviewer.log", filemode="w")
    logging.info(f"Using Python {sys.version.split()[0]}")
    logging.info(f"Using wxPython {wx.version()}")
    app = wx.App()
    # Redirect in the standard console, and not stdout/stderr
    general_window = GeneralFrame(None)  # Create an object [Instance] forms
    # (In the terminology wxwidgets this window)

    general_window.Show(True)
    app.MainLoop()

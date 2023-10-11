import numpy as np

import wx
import wx.glcanvas as wxgl
import OpenGL.GL as OGL


class GeneralFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,  title="Malevich's Black Square",
                          pos=wx.DefaultPosition, size=wx.Size(800, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.Centre(wx.BOTH)

        # OpenGL
        canvas_attrs = wxgl.GLAttributes()
        canvas_attrs.PlatformDefaults().MinRGBA(1, 1, 1, 0).DoubleBuffer().Depth(1).EndList()
        self.glcv = wxgl.GLCanvas(self, canvas_attrs)
        contextAttrs = wxgl.GLContextAttrs()
        self.glctx = wxgl.GLContext(self.glcv, ctxAttrs=contextAttrs)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self._must_init = True

    def on_paint(self, event):
        self.glcv.SetCurrent(self.glctx)
        size = self.glcv.GetClientSize()
        OGL.glViewport(0, 0, size[0], size[1])
        OGL.glClearColor(1.0, 1.0, 1.0, 1.0)
        # Clear the screen to dark green
        OGL.glClear(OGL.GL_COLOR_BUFFER_BIT)

        OGL.glMatrixMode(OGL.GL_PROJECTION)
        OGL.glLoadIdentity()
        OGL.glOrtho(size[0]/-200, size[0]/200, size[1]/-200, size[1]/200, -2, 2)

        OGL.glMatrixMode(OGL.GL_MODELVIEW)
        OGL.glColor3f(0.0, 0.0, 0.0)  # White
        OGL.glBegin(OGL.GL_QUADS)
        OGL.glVertex2f(-1, 1)
        OGL.glVertex2f(1, 1)
        OGL.glVertex2f(1, -1)
        OGL.glVertex2f(-1, -1)
        OGL.glEnd()

        self.glcv.SwapBuffers()
        event.Skip()

    def __del__(self):
        pass

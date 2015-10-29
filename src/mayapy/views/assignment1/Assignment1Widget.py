# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget


# ___________________________________________________________________________________________________ Assignment1Widget
class Assignment1Widget(PyGlassWidget):
    """A class for Assignment 1"""

    # ===================================================================================================
    #                                                                                       C L A S S

    # ___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment1Widget, self).__init__(parent, **kwargs)
        self.kickBtn.clicked.connect(self.on_click_kick)
        self.makeLegoManBtn.clicked.connect(self.on_click_make_lego_man)
        self.raiseArmBtn.clicked.connect(self.on_click_raise_arm)
        self.homeBtn.clicked.connect(self._handleReturnHome)


    def on_click_kick(self):
        """
        """
        r = 50
        a = 2.0 * r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)


    def on_click_make_lego_man(self):
        """
        """
        r = 50
        a = 2.0 * r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)


    def on_click_raise_arm(self):
        """
        """
        r = 50
        a = 2.0 * r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)


    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

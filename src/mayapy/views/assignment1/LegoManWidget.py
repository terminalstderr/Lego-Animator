# Assignment1Widget.py
# (C)2013
# Scott Ernst

# DEFAULT IMPORTS
import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

# Ryan's Imports
import random
import re


# ___________________________________________________________________________________________________ LegoManWidget
class LegoManWidget(PyGlassWidget):
    """A class for Assignment 1"""

    def __init__(self, parent, **kwargs):
        """Creates a new instance of LegoManWidget."""
        super(LegoManWidget, self).__init__(parent, **kwargs)
        self.kickBtn.clicked.connect(self.on_click_kick)
        self.makeLegoManBtn.clicked.connect(self.on_click_make_lego_man)
        self.raiseArmBtn.clicked.connect(self.on_click_raise_arm)
        self.homeBtn.clicked.connect(self.on_click_return_home)


    def on_click_return_home(self):
        self.mainWindow.setActiveWidget('home')


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


    def get_ball_from_current_selection(self):
        selection = cmds.ls(selection=True)
        ball = ''
        for item in selection:
            match = re.search("(ball.*)\|*?", item)
            if match:
                ball = match.group(1)
        return ball


    def on_click_object_flight(self, height=30):
        ball = get_ball_from_current_selection()
        if ball is '':
            return """Was unable to find a "ball" in the current selection!"""
        starting_ball_height = cmds.getAttr(ball + ".translateY")
        final_slide = height/10
        ball_rotation = 360*random.randint(height/20, height/10)
        final_slide_time = height/10

        # Set initial key frame
        current_time = cmds.currentTime(query=True)
        cmds.setKeyframe(ball, at="translateZ", t=current_time, ott="linear")
        cmds.setKeyframe(ball, at="translateY", t=current_time, ott="linear")
        cmds.setKeyframe(ball, at="rotate", t=current_time)

        # Set all remaining key frames programatically in the below loop
        bounce_height = height
        bounce_time = bounce_height
        bounce_distance = 0
        while bounce_height > 1:
            # peak of flight
            current_time += bounce_time/2
            cmds.setKeyframe(ball, v=bounce_height, at="translateY", t=current_time, itt="spline", ott="spline")

            # touch down to earth
            current_time += bounce_time/2
            cmds.setKeyframe(ball, v=starting_ball_height, at="translateY", t=current_time, itt="linear", ott="linear")

            bounce_distance += bounce_height*3
            bounce_time *= 0.5
            bounce_height *= 0.5

        # Set final key frame
        current_time += final_slide_time
        cmds.setKeyframe(ball, v=bounce_distance + final_slide, at="translateZ", t=current_time, itt="spline")
        cmds.setKeyframe(ball, v=ball_rotation, at="rotate", t=current_time)
        cmds.currentTime(current_time)

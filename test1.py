from psychopy import visual, core, event, clock
from psychopy.hardware import keyboard
import numpy as np

mywin = visual.Window ([600, 600], monitor = "testMonitor", units = "deg", color = [-1, -1, -1])
## Begin experiment
mouse = event.Mouse(win=mywin)
clicked = False
trialClock = core.Clock()
t = 0
trialClock.reset()
frameN = 120

## Begin routine
mouse.tStart = None
mouse.tStop = None
mouse.tStartRefresh = None
mouse.tStopRefresh = None
#mouse.status = NOT_STARTED

text_msg = visual.TextStim(win = mywin, text='Welcome to the experiment. Choose the triangle in the following images. Press the space bar to begin.')
text_msg.draw()
mywin.update()
instruction_msg_time = event.waitKeys (keyList = ['space'])

xvalues_range = [0, 3, 4, 3, 0, -3, -4, -3]
yvalues_range = [4, 3, 0, -3, -4, -3, 0, 3]
for ii in range (8):
    for jj in range (8):
        if xvalues_range [ii] == xvalues_range [jj] and yvalues_range [ii] == yvalues_range [jj]:
            triangle1 = visual.Polygon(win = mywin, edges=3, radius=1.25, fillColor=[0, 255, 0], lineColor = [0, 255, 0], colorSpace = 'rgb', pos=(xvalues_range [jj], yvalues_range [jj]))
            triangle1.draw()
        else:
            circle1 = visual.Circle (win = mywin, radius= 1, edges='circle', fillColor= [0, 255, 0], colorSpace = 'rgb', pos=(xvalues_range [jj], yvalues_range [jj]))
            circle1.draw()
    myphoto = mywin.update()
    #while clicked == False:
        #if mouse.isPressedIn (triangle1):
            #clicked = True
        #else:
            #core.wait (5)
    for frames in range (frameN):
        if mouse.isPressedIn (triangle1):
            core.wait (0.5)
            core.quit()
        else:
            core.wait (3)
        
    

for ii in range (8):
    for jj in range (8):
        if xvalues_range [ii] == xvalues_range [jj] and yvalues_range [ii] == yvalues_range [jj]:
            triangle1 = visual.Polygon(win = mywin, edges=3, radius=1.25, fillColor=[255, 0, 0], lineColor = [255, 0, 0], colorSpace = 'rgb', pos=(xvalues_range [jj], yvalues_range [jj]))
            triangle1.draw()
        else:
            circle1 = visual.Circle (win = mywin, radius= 1, edges='circle', fillColor= [0, 255, 0], colorSpace = 'rgb', pos=(xvalues_range [jj], yvalues_range [jj]))
            circle1.draw()
    mywin.update()
    #core.wait (1.0)
    
scrambled_x_range = [-3, 0, 0, 4, -3, -4, 3, 3]
scrambled_y_range = [-3, -4, 4, 0, 3, 0, -3, 3]

for ii in range (8):
    for jj in range (8):
        if xvalues_range [ii] == xvalues_range [jj] and yvalues_range [ii] == yvalues_range [jj]:
            triangle1 = visual.Polygon(win = mywin, edges=3, radius=1.25, fillColor=[0, 255, 0], lineColor = [0, 255, 0], colorSpace = 'rgb', pos=(xvalues_range [jj], yvalues_range [jj]))
            triangle1.draw()
        elif xvalues_range [jj] == scrambled_x_range [ii] and yvalues_range [jj] == scrambled_y_range [ii]:
            circle2 = visual.Circle (win = mywin, radius= 1, edges='circle', fillColor= [255, 0, 0], colorSpace = 'rgb', pos=(xvalues_range [jj], yvalues_range [jj]))
            circle2.draw()
        else:
            circle1 = visual.Circle (win = mywin, radius= 1, edges='circle', fillColor= [0, 255, 0], colorSpace = 'rgb', pos=(xvalues_range [jj], yvalues_range [jj]))
            circle1.draw()
    mywin.update()
    #core.wait (2.0)

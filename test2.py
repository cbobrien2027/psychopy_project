from psychopy import visual, core, event, clock
from psychopy.hardware import keyboard

mywin = visual.Window ([600, 600], monitor = "testMonitor", units = "deg", color = [-1, -1, -1])

text_msg = visual.TextStim(win = mywin, text='Welcome to the experiment. Choose the triangle in the following images. Press the space bar to begin.')
text_msg.draw()
mywin.update()
instruction_msg_time = event.waitKeys (keyList = ['space'])

xvalues_range = [0, 3, 4, 3, 0, -3, -4, -3]
yvalues_range = [4, 3, 0, -3, -4, -3, 0, 3]

possible_positions = [(0, 4), (3, 3), (4, 0), (3, -3), (0, -4), (-3, -3), (-4, 0), (-3, 3)]

for ii in possible_positions:
    if ii == triangle_pos:
        triangle1 = visual.Polygon(win = mywin, edges=3, radius=1.25, colorSpace = 'rgb', pos=ii)
        if triangle_color == 'g':
            triangle1.color = (0, 255, 0)
        else:
            triangle1.color = (255, 0, 0)
        triangle1.draw()
    else:
        circle1 = visual.Circle (win = mywin, radius= 1, edges='circle', colorSpace = 'rgb', pos=ii)
        if ii == pink_circle_pos:
            circle1.color (255, 0, 0)
        else:
            circle1.color (0, 255, 0)
        circle1.draw()
    mywin.update()
        

    #while clicked == False:
        #if mouse.isPressedIn (triangle1):
            #clicked = True
        #else:
            #core.wait (5)
    #for frames in range (frameN):
        #if mouse.isPressedIn (triangle1):
            #core.wait (0.5)
            #core.quit()
        #else:
            #core.wait (3)

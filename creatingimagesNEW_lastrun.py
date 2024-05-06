#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on Sun May  5 23:46:59 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'creatingimagesNEW'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1536, 864]
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/carolineobrien/Documents/GitHub/psychopy_project/creatingimagesNEW_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1,-1,-1]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = True
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome_Page" ---
    textWelcomePage = visual.TextStim(win=win, name='textWelcomePage',
        text='Hello!\n\nThank you for participating in this experiment. Please read the instructions before beginning. \n\nInstructions:\nYou will be presented with a variety of shapes. Your task is to choose the triangle. You will not be able to move on to the next slide unless you correctly choose the triangle with your mouse. Once you begin the experiment you will not be able to leave until you have successfully completed all tasks. This experiment will take approximately 5 minutes. \n\nPLEASE PRESS THE SPACE BAR TO BEGIN THE EXPERIMENT',
        font='Open Sans',
        pos=(0, -0.05), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "code_attempt" ---
    
    # --- Initialize components for Routine "builder_attempt" ---
    circle1 = visual.ShapeStim(
        win=win, name='circle1',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    circle2 = visual.ShapeStim(
        win=win, name='circle2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    circle3 = visual.ShapeStim(
        win=win, name='circle3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    circle4 = visual.ShapeStim(
        win=win, name='circle4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    circle5 = visual.ShapeStim(
        win=win, name='circle5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    circle6 = visual.ShapeStim(
        win=win, name='circle6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    circle7 = visual.ShapeStim(
        win=win, name='circle7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    triangle1 = visual.ShapeStim(
        win=win, name='triangle1',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-8.0, interpolate=True)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "End_Routine" ---
    End_Text = visual.TextStim(win=win, name='End_Text',
        text='Thank you for completing the experiment! Please press the SPACE BAR to exit the program. ',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome_Page" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Welcome_Page.started', globalClock.getTime(format='float'))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    Welcome_PageComponents = [textWelcomePage, key_resp]
    for thisComponent in Welcome_PageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome_Page" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcomePage* updates
        
        # if textWelcomePage is starting this frame...
        if textWelcomePage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcomePage.frameNStart = frameN  # exact frame index
            textWelcomePage.tStart = t  # local t and not account for scr refresh
            textWelcomePage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcomePage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcomePage.started')
            # update status
            textWelcomePage.status = STARTED
            textWelcomePage.setAutoDraw(True)
        
        # if textWelcomePage is active this frame...
        if textWelcomePage.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome_PageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome_Page" ---
    for thisComponent in Welcome_PageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Welcome_Page.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Welcome_Page" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Conditions Spreadsheet-2.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "code_attempt" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('code_attempt.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_2
        #Caroline coded.
        fixation_square = visual.Polygon (win = win, edges = 4, radius = 0.1, pos = (0,0), size = 0.3, fillColor = [1, 1, 1], fillColorSpace = 'rgb', ori=90.0)
        fixation_square.draw()
        win.update()
        core.wait (0.2)
        
        #Garv coded.
        mouse.setPos(0)
        
        
        #Caroline Coded
        mouse = event.Mouse(win = win)
        mouse.mouseClock = core.Clock()
        #Sets circle1 position.
        if triangle_pos != (0, 0.25):
            circle1_pos = (0, 0.25)
        else:
            circle1_pos = (0.1875, 0.1875)
           
        #Sets circle2 position.
        if triangle_pos != (0.1875, 0.1875) and triangle_pos != (0, 0.25):
            circle2_pos = (0.1875, 0.1875)
        else:
            circle2_pos = (0.25, 0)
        
        #Sets circle3 position.
        if triangle_pos != (0.25, 0) and triangle_pos != (0.1875, 0.1875) and triangle_pos != (0, 0.25):
            circle3_pos = (0.25, 0)
        else:
            circle3_pos = (0.1875, -0.1875)
        
        #Sets circle4 position.
        if triangle_pos == (0, -0.25) or triangle_pos == (-0.1875, -0.1875) or triangle_pos == (-0.25, 0) or triangle_pos == (-0.1875, 0.1875):
            circle4_pos = (0.1875, -0.1875)
        else:
            circle4_pos = (0, -0.25)
            
        #Sets circle5 position.
        if triangle_pos== (-0.1875, -0.1875) or triangle_pos == (-0.25, 0) or triangle_pos == (-0.1875, 0.1875):
            circle5_pos = (0, -0.25)
        else:
            circle5_pos = (-0.1875, -0.1875)
            
        #Sets circle6 position.
        if triangle_pos == (-0.25, 0) or triangle_pos == (-0.1875, 0.1875):
            circle6_pos = (-0.1875, -0.1875)
        else:
            circle6_pos = (-0.25, 0)
            
        #Sets circle7 position.
        if triangle_pos == (-0.1875, 0.1875):
            circle7_pos = (-0.25, 0)
        else:
            circle7_pos = (-0.1875, 0.1875)
        
        #Sets the triangle color.
        if triangle_color == 'g':
            triangle1_color = [-0.6078, 0.6708, -0.6708]
        else:
            triangle1_color = [1.0000, -1.0000, 1.0000]
            
        #Sets the circle colors - all green except if the position matches pink_circle_pos.
        #Then it is set to pink.
        
        circle1_color = []
        circle2_color = []
        circle3_color = []
        circle4_color = []
        circle5_color = []
        circle6_color = []
        circle7_color = []
        
        circle_positions = [circle1_pos, circle2_pos, circle3_pos, circle4_pos, circle5_pos, circle6_pos, circle7_pos]
        circle_colors = [circle1_color, circle2_color, circle3_color, circle4_color, circle5_color, circle6_color, circle7_color]
        
        for ii in range (len (circle_colors)):
            if circle_positions [ii] == pink_circle_pos:
                circle_colors[ii] = [1.0000, -1.0000, 1.0000]
            else:
                circle_colors[ii] = [-0.6708, 0.6708, -0.6708]
        
        for ii in range (len(circle_colors)):
            circles = visual.Circle (win = win, edges = 'circle', pos = circle_positions[ii], size = 0.1, fillColor = circle_colors[ii], fillColorSpace = 'rgb')
            circles.draw()
        triangle1 = visual.Polygon (win = win, edges = 3, pos = triangle_pos, size = 0.125, fillColor = triangle1_color, lineColor = triangle1_color, fillColorSpace = 'rgb', lineColorSpace = 'rgb')
        triangle1.draw()
        fixation_square.draw()
        win.update()
        
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
                    
        while triangle1.contains(mouse) == False:
            core.wait (1)
            
        if triangle1.contains(mouse) == True:
            continueRoutine = False
        
        # keep track of which components have finished
        code_attemptComponents = []
        for thisComponent in code_attemptComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "code_attempt" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in code_attemptComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "code_attempt" ---
        for thisComponent in code_attemptComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('code_attempt.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code_2
        
        
        # the Routine "code_attempt" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "builder_attempt" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('builder_attempt.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from code
    #Caroline coded lines 6-90.
    #Sets circle1 position.
    if triangle_pos != (0, 0.25):
        circle1_pos = (0, 0.25)
    else:
        circle1_pos = (0.1875, 0.1875)
       
    #Sets circle2 position.
    if triangle_pos != (0.1875, 0.1875) and triangle_pos != (0, 0.25):
        circle2_pos = (0.1875, 0.1875)
    else:
        circle2_pos = (0.25, 0)
    
    #Sets circle3 position.
    if triangle_pos != (0.25, 0) and triangle_pos != (0.1875, 0.1875) and triangle_pos != (0, 0.25):
        circle3_pos = (0.25, 0)
    else:
        circle3_pos = (0.1875, -0.1875)
    
    #Sets circle4 position.
    if triangle_pos == (0, -0.25) or triangle_pos == (-0.1875, -0.1875) or triangle_pos == (-0.25, 0) or triangle_pos == (-0.1875, 0.1875):
        circle4_pos = (0.1875, -0.1875)
    else:
        circle4_pos = (0, -0.25)
        
    #Sets circle5 position.
    if triangle_pos== (-0.1875, -0.1875) or triangle_pos == (-0.25, 0) or triangle_pos == (-0.1875, 0.1875):
        circle5_pos = (0, -0.25)
    else:
        circle5_pos = (-0.1875, -0.1875)
        
    #Sets circle6 position.
    if triangle_pos == (-0.25, 0) or triangle_pos == (-0.1875, 0.1875):
        circle6_pos = (-0.1875, -0.1875)
    else:
        circle6_pos = (-0.25, 0)
        
    #Sets circle7 position.
    if triangle_pos == (-0.1875, 0.1875):
        circle7_pos = (-0.25, 0)
    else:
        circle7_pos = (-0.1875, 0.1875)
    
    #Sets the triangle color.
    if triangle_color == 'g':
        triangle1_color = [-0.6078, 0.6708, -0.6708]
    else:
        triangle1_color = [1.0000, -1.0000, 1.0000]
        
    #Sets the circle colors - all green except if the position matches pink_circle_pos.
    #Then it is set to pink.
    if circle1_pos == pink_circle_pos:
        circle1_color = [1.0000, -1.0000, 1.0000]
    else:
        circle1_color = [-0.6078, 0.6708, -0.6708]
        
    if circle2_pos == pink_circle_pos:
        circle2_color = [1.0000, -1.0000, 1.0000]
    else:
        circle2_color = [-0.6078, 0.6708, -0.6708]
        
    if circle3_pos == pink_circle_pos:
        circle3_color = [1.0000, -1.0000, 1.0000]
    else:
        circle3_color = [-0.6078, 0.6708, -0.6708]
        
    if circle4_pos == pink_circle_pos:
        circle4_color = [1.0000, -1.0000, 1.0000]
    else:
        circle4_color = [-0.6078, 0.6708, -0.6708]
        
    if circle5_pos == pink_circle_pos:
        circle5_color = [1.0000, -1.0000, 1.0000]
    else:
        circle5_color = [-0.6078, 0.6708, -0.6708]
        
    if circle6_pos == pink_circle_pos:
        circle6_color = [1.0000, -1.0000, 1.0000]
    else:
        circle6_color = [-0.6078, 0.6708, -0.6708]
        
    if circle7_pos == pink_circle_pos:
        circle7_color = [1.0000, -1.0000, 1.0000]
    else:
        circle7_color = [-0.6078, 0.6708, -0.6708]
    
    #Garv coded.
    mouse.setPos(0)
    circle1.setFillColor(circle1_color)
    circle1.setPos(circle1_pos)
    circle1.setLineColor(circle1_color)
    circle2.setFillColor(circle2_color)
    circle2.setPos(circle2_pos)
    circle2.setLineColor(circle2_color)
    circle3.setFillColor(circle3_color)
    circle3.setPos(circle3_pos)
    circle3.setLineColor(circle3_color)
    circle4.setFillColor(circle4_color)
    circle4.setPos(circle4_pos)
    circle4.setLineColor(circle4_color)
    circle5.setFillColor(circle5_color)
    circle5.setPos(circle5_pos)
    circle5.setLineColor(circle5_color)
    circle6.setFillColor(circle6_color)
    circle6.setPos(circle6_pos)
    circle6.setLineColor(circle6_color)
    circle7.setFillColor(circle7_color)
    circle7.setPos(circle7_pos)
    circle7.setLineColor(circle7_color)
    triangle1.setFillColor(triangle1_color)
    triangle1.setPos(triangle_pos)
    triangle1.setLineColor(triangle1_color)
    # setup some python lists for storing info about the mouse
    mouse.corr = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    builder_attemptComponents = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, triangle1, mouse]
    for thisComponent in builder_attemptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "builder_attempt" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circle1* updates
        
        # if circle1 is starting this frame...
        if circle1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            circle1.frameNStart = frameN  # exact frame index
            circle1.tStart = t  # local t and not account for scr refresh
            circle1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle1.started')
            # update status
            circle1.status = STARTED
            circle1.setAutoDraw(True)
        
        # if circle1 is active this frame...
        if circle1.status == STARTED:
            # update params
            pass
        
        # *circle2* updates
        
        # if circle2 is starting this frame...
        if circle2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            circle2.frameNStart = frameN  # exact frame index
            circle2.tStart = t  # local t and not account for scr refresh
            circle2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle2.started')
            # update status
            circle2.status = STARTED
            circle2.setAutoDraw(True)
        
        # if circle2 is active this frame...
        if circle2.status == STARTED:
            # update params
            pass
        
        # *circle3* updates
        
        # if circle3 is starting this frame...
        if circle3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            circle3.frameNStart = frameN  # exact frame index
            circle3.tStart = t  # local t and not account for scr refresh
            circle3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle3.started')
            # update status
            circle3.status = STARTED
            circle3.setAutoDraw(True)
        
        # if circle3 is active this frame...
        if circle3.status == STARTED:
            # update params
            pass
        
        # *circle4* updates
        
        # if circle4 is starting this frame...
        if circle4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            circle4.frameNStart = frameN  # exact frame index
            circle4.tStart = t  # local t and not account for scr refresh
            circle4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle4.started')
            # update status
            circle4.status = STARTED
            circle4.setAutoDraw(True)
        
        # if circle4 is active this frame...
        if circle4.status == STARTED:
            # update params
            pass
        
        # *circle5* updates
        
        # if circle5 is starting this frame...
        if circle5.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            circle5.frameNStart = frameN  # exact frame index
            circle5.tStart = t  # local t and not account for scr refresh
            circle5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle5.started')
            # update status
            circle5.status = STARTED
            circle5.setAutoDraw(True)
        
        # if circle5 is active this frame...
        if circle5.status == STARTED:
            # update params
            pass
        
        # *circle6* updates
        
        # if circle6 is starting this frame...
        if circle6.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            circle6.frameNStart = frameN  # exact frame index
            circle6.tStart = t  # local t and not account for scr refresh
            circle6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle6.started')
            # update status
            circle6.status = STARTED
            circle6.setAutoDraw(True)
        
        # if circle6 is active this frame...
        if circle6.status == STARTED:
            # update params
            pass
        
        # *circle7* updates
        
        # if circle7 is starting this frame...
        if circle7.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            circle7.frameNStart = frameN  # exact frame index
            circle7.tStart = t  # local t and not account for scr refresh
            circle7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle7.started')
            # update status
            circle7.status = STARTED
            circle7.setAutoDraw(True)
        
        # if circle7 is active this frame...
        if circle7.status == STARTED:
            # update params
            pass
        
        # *triangle1* updates
        
        # if triangle1 is starting this frame...
        if triangle1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            triangle1.frameNStart = frameN  # exact frame index
            triangle1.tStart = t  # local t and not account for scr refresh
            triangle1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triangle1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'triangle1.started')
            # update status
            triangle1.status = STARTED
            triangle1.setAutoDraw(True)
        
        # if triangle1 is active this frame...
        if triangle1.status == STARTED:
            # update params
            pass
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([triangle1], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    # check whether click was in correct object
                    if gotValidClick:
                        _corr = 0
                        _corrAns = environmenttools.getFromNames(triangle1, namespace=locals())
                        for obj in _corrAns:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                _corr = 1
                        mouse.corr.append(_corr)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in builder_attemptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "builder_attempt" ---
    for thisComponent in builder_attemptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('builder_attempt.stopped', globalClock.getTime(format='float'))
    # store data for thisExp (ExperimentHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames([triangle1], namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    thisExp.addData('mouse.x', x)
    thisExp.addData('mouse.y', y)
    thisExp.addData('mouse.leftButton', buttons[0])
    thisExp.addData('mouse.midButton', buttons[1])
    thisExp.addData('mouse.rightButton', buttons[2])
    thisExp.addData('mouse.corr', mouse.corr)
    if len(mouse.clicked_name):
        thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "builder_attempt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "End_Routine" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('End_Routine.started', globalClock.getTime(format='float'))
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    End_RoutineComponents = [End_Text, key_resp_2]
    for thisComponent in End_RoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End_Routine" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *End_Text* updates
        
        # if End_Text is starting this frame...
        if End_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            End_Text.frameNStart = frameN  # exact frame index
            End_Text.tStart = t  # local t and not account for scr refresh
            End_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(End_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'End_Text.started')
            # update status
            End_Text.status = STARTED
            End_Text.setAutoDraw(True)
        
        # if End_Text is active this frame...
        if End_Text.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_RoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_Routine" ---
    for thisComponent in End_RoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('End_Routine.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "End_Routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

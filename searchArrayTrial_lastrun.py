#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.1),
    on Mon Apr 29 14:16:26 2024
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
psychopyVersion = '2024.1.1'
expName = 'searchArrayTrial'  # from the Builder filename that created this script
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
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
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
        originPath='/Users/carolineobrien/Documents/GitHub/psychopy_project/searchArrayTrial_lastrun.py',
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
            size=[1000, 800], fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1, -1, -1], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1, -1, -1]
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
    
    # --- Initialize components for Routine "WelcomePage" ---
    textWelcomeMessage = visual.TextStim(win=win, name='textWelcomeMessage',
        text='Welcome to the Experiment\n\nPress the SpaceBar to begin!',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "Instructions" ---
    textInstructions = visual.TextStim(win=win, name='textInstructions',
        text='There will be 15 images. \n\nUsing your mouse, select the rhombus in each image.\n\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "image1_1" ---
    greencircle1 = visual.ShapeStim(
        win=win, name='greencircle1',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2 = visual.ShapeStim(
        win=win, name='greencircle2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3 = visual.ShapeStim(
        win=win, name='greencircle3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4 = visual.ShapeStim(
        win=win, name='greencircle4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5 = visual.ShapeStim(
        win=win, name='greencircle5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6 = visual.ShapeStim(
        win=win, name='greencircle6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7 = visual.ShapeStim(
        win=win, name='greencircle7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle = visual.ShapeStim(
        win=win, name='greentriangle',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image1_2" ---
    greencircle1_2 = visual.ShapeStim(
        win=win, name='greencircle1_2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_2 = visual.ShapeStim(
        win=win, name='greencircle2_2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_2 = visual.ShapeStim(
        win=win, name='greencircle3_2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_2 = visual.ShapeStim(
        win=win, name='greencircle4_2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_2 = visual.ShapeStim(
        win=win, name='greencircle5_2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_2 = visual.ShapeStim(
        win=win, name='greencircle6_2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_2 = visual.ShapeStim(
        win=win, name='greencircle7_2',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_2 = visual.ShapeStim(
        win=win, name='greentriangle_2',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image1_3" ---
    greencircle1_3 = visual.ShapeStim(
        win=win, name='greencircle1_3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_3 = visual.ShapeStim(
        win=win, name='greencircle2_3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_3 = visual.ShapeStim(
        win=win, name='greencircle3_3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_3 = visual.ShapeStim(
        win=win, name='greencircle4_3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_3 = visual.ShapeStim(
        win=win, name='greencircle5_3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_3 = visual.ShapeStim(
        win=win, name='greencircle6_3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_3 = visual.ShapeStim(
        win=win, name='greencircle7_3',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_3 = visual.ShapeStim(
        win=win, name='greentriangle_3',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image1_4" ---
    greencircle1_4 = visual.ShapeStim(
        win=win, name='greencircle1_4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_4 = visual.ShapeStim(
        win=win, name='greencircle2_4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_4 = visual.ShapeStim(
        win=win, name='greencircle3_4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_4 = visual.ShapeStim(
        win=win, name='greencircle4_4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_4 = visual.ShapeStim(
        win=win, name='greencircle5_4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_4 = visual.ShapeStim(
        win=win, name='greencircle6_4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_4 = visual.ShapeStim(
        win=win, name='greencircle7_4',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_4 = visual.ShapeStim(
        win=win, name='greentriangle_4',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image1_5" ---
    greencircle1_5 = visual.ShapeStim(
        win=win, name='greencircle1_5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_5 = visual.ShapeStim(
        win=win, name='greencircle2_5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_5 = visual.ShapeStim(
        win=win, name='greencircle3_5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_5 = visual.ShapeStim(
        win=win, name='greencircle4_5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_5 = visual.ShapeStim(
        win=win, name='greencircle5_5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_5 = visual.ShapeStim(
        win=win, name='greencircle6_5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_5 = visual.ShapeStim(
        win=win, name='greencircle7_5',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_5 = visual.ShapeStim(
        win=win, name='greentriangle_5',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0, -0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image1_6" ---
    greencircle1_6 = visual.ShapeStim(
        win=win, name='greencircle1_6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_6 = visual.ShapeStim(
        win=win, name='greencircle2_6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_6 = visual.ShapeStim(
        win=win, name='greencircle3_6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_6 = visual.ShapeStim(
        win=win, name='greencircle4_6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_6 = visual.ShapeStim(
        win=win, name='greencircle5_6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_6 = visual.ShapeStim(
        win=win, name='greencircle6_6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_6 = visual.ShapeStim(
        win=win, name='greencircle7_6',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_6 = visual.ShapeStim(
        win=win, name='greentriangle_6',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(-.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image1_7" ---
    greencircle1_7 = visual.ShapeStim(
        win=win, name='greencircle1_7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_7 = visual.ShapeStim(
        win=win, name='greencircle2_7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_7 = visual.ShapeStim(
        win=win, name='greencircle3_7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_7 = visual.ShapeStim(
        win=win, name='greencircle4_7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_7 = visual.ShapeStim(
        win=win, name='greencircle5_7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_7 = visual.ShapeStim(
        win=win, name='greencircle6_7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_7 = visual.ShapeStim(
        win=win, name='greencircle7_7',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_7 = visual.ShapeStim(
        win=win, name='greentriangle_7',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(-.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image1_8" ---
    greencircle1_8 = visual.ShapeStim(
        win=win, name='greencircle1_8',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_8 = visual.ShapeStim(
        win=win, name='greencircle2_8',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_8 = visual.ShapeStim(
        win=win, name='greencircle3_8',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_8 = visual.ShapeStim(
        win=win, name='greencircle4_8',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_8 = visual.ShapeStim(
        win=win, name='greencircle5_8',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_8 = visual.ShapeStim(
        win=win, name='greencircle6_8',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_8 = visual.ShapeStim(
        win=win, name='greencircle7_8',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_8 = visual.ShapeStim(
        win=win, name='greentriangle_8',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(-.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image3_1" ---
    greencircle1_9 = visual.ShapeStim(
        win=win, name='greencircle1_9',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_9 = visual.ShapeStim(
        win=win, name='greencircle2_9',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_9 = visual.ShapeStim(
        win=win, name='greencircle3_9',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_9 = visual.ShapeStim(
        win=win, name='greencircle4_9',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_9 = visual.ShapeStim(
        win=win, name='greencircle5_9',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_9 = visual.ShapeStim(
        win=win, name='greencircle6_9',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_9 = visual.ShapeStim(
        win=win, name='greencircle7_9',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    pinktriangle = visual.ShapeStim(
        win=win, name='pinktriangle',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, 1.0000], fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image3_2" ---
    greencircle1_10 = visual.ShapeStim(
        win=win, name='greencircle1_10',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_10 = visual.ShapeStim(
        win=win, name='greencircle2_10',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_10 = visual.ShapeStim(
        win=win, name='greencircle3_10',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_10 = visual.ShapeStim(
        win=win, name='greencircle4_10',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_10 = visual.ShapeStim(
        win=win, name='greencircle5_10',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_10 = visual.ShapeStim(
        win=win, name='greencircle6_10',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_10 = visual.ShapeStim(
        win=win, name='greencircle7_10',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_9 = visual.ShapeStim(
        win=win, name='greentriangle_9',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, 1.0000], fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image3_3" ---
    greencircle1_11 = visual.ShapeStim(
        win=win, name='greencircle1_11',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_11 = visual.ShapeStim(
        win=win, name='greencircle2_11',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_11 = visual.ShapeStim(
        win=win, name='greencircle3_11',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_11 = visual.ShapeStim(
        win=win, name='greencircle4_11',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_11 = visual.ShapeStim(
        win=win, name='greencircle5_11',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_11 = visual.ShapeStim(
        win=win, name='greencircle6_11',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_11 = visual.ShapeStim(
        win=win, name='greencircle7_11',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_10 = visual.ShapeStim(
        win=win, name='greentriangle_10',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, 1.0000], fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image3_4" ---
    greencircle1_12 = visual.ShapeStim(
        win=win, name='greencircle1_12',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_12 = visual.ShapeStim(
        win=win, name='greencircle2_12',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_12 = visual.ShapeStim(
        win=win, name='greencircle3_12',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_12 = visual.ShapeStim(
        win=win, name='greencircle4_12',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_12 = visual.ShapeStim(
        win=win, name='greencircle5_12',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_12 = visual.ShapeStim(
        win=win, name='greencircle6_12',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_12 = visual.ShapeStim(
        win=win, name='greencircle7_12',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_11 = visual.ShapeStim(
        win=win, name='greentriangle_11',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, 1.0000], fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image3_5" ---
    greencircle1_13 = visual.ShapeStim(
        win=win, name='greencircle1_13',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_13 = visual.ShapeStim(
        win=win, name='greencircle2_13',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_13 = visual.ShapeStim(
        win=win, name='greencircle3_13',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_13 = visual.ShapeStim(
        win=win, name='greencircle4_13',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_13 = visual.ShapeStim(
        win=win, name='greencircle5_13',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_13 = visual.ShapeStim(
        win=win, name='greencircle6_13',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_13 = visual.ShapeStim(
        win=win, name='greencircle7_13',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_12 = visual.ShapeStim(
        win=win, name='greentriangle_12',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(0, -0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, 1.0000], fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image3_6" ---
    greencircle1_14 = visual.ShapeStim(
        win=win, name='greencircle1_14',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_14 = visual.ShapeStim(
        win=win, name='greencircle2_14',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_14 = visual.ShapeStim(
        win=win, name='greencircle3_14',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_14 = visual.ShapeStim(
        win=win, name='greencircle4_14',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_14 = visual.ShapeStim(
        win=win, name='greencircle5_14',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_14 = visual.ShapeStim(
        win=win, name='greencircle6_14',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_14 = visual.ShapeStim(
        win=win, name='greencircle7_14',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_13 = visual.ShapeStim(
        win=win, name='greentriangle_13',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(-.1875, -0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, 1.0000], fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image3_7" ---
    greencircle1_15 = visual.ShapeStim(
        win=win, name='greencircle1_15',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_15 = visual.ShapeStim(
        win=win, name='greencircle2_15',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_15 = visual.ShapeStim(
        win=win, name='greencircle3_15',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_15 = visual.ShapeStim(
        win=win, name='greencircle4_15',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_15 = visual.ShapeStim(
        win=win, name='greencircle5_15',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_15 = visual.ShapeStim(
        win=win, name='greencircle6_15',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_15 = visual.ShapeStim(
        win=win, name='greencircle7_15',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_14 = visual.ShapeStim(
        win=win, name='greentriangle_14',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(-.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, 1.0000], fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "image3_8" ---
    greencircle1_16 = visual.ShapeStim(
        win=win, name='greencircle1_16',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=0.0, interpolate=True)
    greencircle2_16 = visual.ShapeStim(
        win=win, name='greencircle2_16',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-1.0, interpolate=True)
    greencircle3_16 = visual.ShapeStim(
        win=win, name='greencircle3_16',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-2.0, interpolate=True)
    greencircle4_16 = visual.ShapeStim(
        win=win, name='greencircle4_16',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-3.0, interpolate=True)
    greencircle5_16 = visual.ShapeStim(
        win=win, name='greencircle5_16',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, -0.25), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-4.0, interpolate=True)
    greencircle6_16 = visual.ShapeStim(
        win=win, name='greencircle6_16',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.1875, -.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-5.0, interpolate=True)
    greencircle7_16 = visual.ShapeStim(
        win=win, name='greencircle7_16',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.1608, 0.1137, -0.7255], fillColor=[-0.1608, 0.1137, -0.7255],
        opacity=None, depth=-6.0, interpolate=True)
    greentriangle_15 = visual.ShapeStim(
        win=win, name='greentriangle_15',
        size=(0.1, 0.1), vertices='triangle',
        ori=0.0, pos=(-.1875, 0.1875), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, 1.0000], fillColor=[1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    
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
    
    # --- Prepare to start Routine "WelcomePage" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('WelcomePage.started', globalClock.getTime(format='float'))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    WelcomePageComponents = [textWelcomeMessage, key_resp]
    for thisComponent in WelcomePageComponents:
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
    
    # --- Run Routine "WelcomePage" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcomeMessage* updates
        
        # if textWelcomeMessage is starting this frame...
        if textWelcomeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcomeMessage.frameNStart = frameN  # exact frame index
            textWelcomeMessage.tStart = t  # local t and not account for scr refresh
            textWelcomeMessage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcomeMessage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcomeMessage.started')
            # update status
            textWelcomeMessage.status = STARTED
            textWelcomeMessage.setAutoDraw(True)
        
        # if textWelcomeMessage is active this frame...
        if textWelcomeMessage.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        for thisComponent in WelcomePageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomePage" ---
    for thisComponent in WelcomePageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('WelcomePage.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "WelcomePage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions.started', globalClock.getTime(format='float'))
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [textInstructions, key_resp_2]
    for thisComponent in InstructionsComponents:
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
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstructions* updates
        
        # if textInstructions is starting this frame...
        if textInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstructions.frameNStart = frameN  # exact frame index
            textInstructions.tStart = t  # local t and not account for scr refresh
            textInstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstructions.started')
            # update status
            textInstructions.status = STARTED
            textInstructions.setAutoDraw(True)
        
        # if textInstructions is active this frame...
        if textInstructions.status == STARTED:
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
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image1_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image1_1.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image1_1Components = [greencircle1, greencircle2, greencircle3, greencircle4, greencircle5, greencircle6, greencircle7, greentriangle]
    for thisComponent in image1_1Components:
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
    
    # --- Run Routine "image1_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1* updates
        
        # if greencircle1 is starting this frame...
        if greencircle1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1.frameNStart = frameN  # exact frame index
            greencircle1.tStart = t  # local t and not account for scr refresh
            greencircle1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1.started')
            # update status
            greencircle1.status = STARTED
            greencircle1.setAutoDraw(True)
        
        # if greencircle1 is active this frame...
        if greencircle1.status == STARTED:
            # update params
            pass
        
        # *greencircle2* updates
        
        # if greencircle2 is starting this frame...
        if greencircle2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2.frameNStart = frameN  # exact frame index
            greencircle2.tStart = t  # local t and not account for scr refresh
            greencircle2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2.started')
            # update status
            greencircle2.status = STARTED
            greencircle2.setAutoDraw(True)
        
        # if greencircle2 is active this frame...
        if greencircle2.status == STARTED:
            # update params
            pass
        
        # *greencircle3* updates
        
        # if greencircle3 is starting this frame...
        if greencircle3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3.frameNStart = frameN  # exact frame index
            greencircle3.tStart = t  # local t and not account for scr refresh
            greencircle3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3.started')
            # update status
            greencircle3.status = STARTED
            greencircle3.setAutoDraw(True)
        
        # if greencircle3 is active this frame...
        if greencircle3.status == STARTED:
            # update params
            pass
        
        # *greencircle4* updates
        
        # if greencircle4 is starting this frame...
        if greencircle4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4.frameNStart = frameN  # exact frame index
            greencircle4.tStart = t  # local t and not account for scr refresh
            greencircle4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4.started')
            # update status
            greencircle4.status = STARTED
            greencircle4.setAutoDraw(True)
        
        # if greencircle4 is active this frame...
        if greencircle4.status == STARTED:
            # update params
            pass
        
        # *greencircle5* updates
        
        # if greencircle5 is starting this frame...
        if greencircle5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5.frameNStart = frameN  # exact frame index
            greencircle5.tStart = t  # local t and not account for scr refresh
            greencircle5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5.started')
            # update status
            greencircle5.status = STARTED
            greencircle5.setAutoDraw(True)
        
        # if greencircle5 is active this frame...
        if greencircle5.status == STARTED:
            # update params
            pass
        
        # *greencircle6* updates
        
        # if greencircle6 is starting this frame...
        if greencircle6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6.frameNStart = frameN  # exact frame index
            greencircle6.tStart = t  # local t and not account for scr refresh
            greencircle6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6.started')
            # update status
            greencircle6.status = STARTED
            greencircle6.setAutoDraw(True)
        
        # if greencircle6 is active this frame...
        if greencircle6.status == STARTED:
            # update params
            pass
        
        # *greencircle7* updates
        
        # if greencircle7 is starting this frame...
        if greencircle7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7.frameNStart = frameN  # exact frame index
            greencircle7.tStart = t  # local t and not account for scr refresh
            greencircle7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7.started')
            # update status
            greencircle7.status = STARTED
            greencircle7.setAutoDraw(True)
        
        # if greencircle7 is active this frame...
        if greencircle7.status == STARTED:
            # update params
            pass
        
        # *greentriangle* updates
        
        # if greentriangle is starting this frame...
        if greentriangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle.frameNStart = frameN  # exact frame index
            greentriangle.tStart = t  # local t and not account for scr refresh
            greentriangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle.started')
            # update status
            greentriangle.status = STARTED
            greentriangle.setAutoDraw(True)
        
        # if greentriangle is active this frame...
        if greentriangle.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image1_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image1_1" ---
    for thisComponent in image1_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image1_1.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image1_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image1_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image1_2.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image1_2Components = [greencircle1_2, greencircle2_2, greencircle3_2, greencircle4_2, greencircle5_2, greencircle6_2, greencircle7_2, greentriangle_2]
    for thisComponent in image1_2Components:
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
    
    # --- Run Routine "image1_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_2* updates
        
        # if greencircle1_2 is starting this frame...
        if greencircle1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_2.frameNStart = frameN  # exact frame index
            greencircle1_2.tStart = t  # local t and not account for scr refresh
            greencircle1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_2.started')
            # update status
            greencircle1_2.status = STARTED
            greencircle1_2.setAutoDraw(True)
        
        # if greencircle1_2 is active this frame...
        if greencircle1_2.status == STARTED:
            # update params
            pass
        
        # *greencircle2_2* updates
        
        # if greencircle2_2 is starting this frame...
        if greencircle2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_2.frameNStart = frameN  # exact frame index
            greencircle2_2.tStart = t  # local t and not account for scr refresh
            greencircle2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_2.started')
            # update status
            greencircle2_2.status = STARTED
            greencircle2_2.setAutoDraw(True)
        
        # if greencircle2_2 is active this frame...
        if greencircle2_2.status == STARTED:
            # update params
            pass
        
        # *greencircle3_2* updates
        
        # if greencircle3_2 is starting this frame...
        if greencircle3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_2.frameNStart = frameN  # exact frame index
            greencircle3_2.tStart = t  # local t and not account for scr refresh
            greencircle3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_2.started')
            # update status
            greencircle3_2.status = STARTED
            greencircle3_2.setAutoDraw(True)
        
        # if greencircle3_2 is active this frame...
        if greencircle3_2.status == STARTED:
            # update params
            pass
        
        # *greencircle4_2* updates
        
        # if greencircle4_2 is starting this frame...
        if greencircle4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_2.frameNStart = frameN  # exact frame index
            greencircle4_2.tStart = t  # local t and not account for scr refresh
            greencircle4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_2.started')
            # update status
            greencircle4_2.status = STARTED
            greencircle4_2.setAutoDraw(True)
        
        # if greencircle4_2 is active this frame...
        if greencircle4_2.status == STARTED:
            # update params
            pass
        
        # *greencircle5_2* updates
        
        # if greencircle5_2 is starting this frame...
        if greencircle5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_2.frameNStart = frameN  # exact frame index
            greencircle5_2.tStart = t  # local t and not account for scr refresh
            greencircle5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_2.started')
            # update status
            greencircle5_2.status = STARTED
            greencircle5_2.setAutoDraw(True)
        
        # if greencircle5_2 is active this frame...
        if greencircle5_2.status == STARTED:
            # update params
            pass
        
        # *greencircle6_2* updates
        
        # if greencircle6_2 is starting this frame...
        if greencircle6_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_2.frameNStart = frameN  # exact frame index
            greencircle6_2.tStart = t  # local t and not account for scr refresh
            greencircle6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_2.started')
            # update status
            greencircle6_2.status = STARTED
            greencircle6_2.setAutoDraw(True)
        
        # if greencircle6_2 is active this frame...
        if greencircle6_2.status == STARTED:
            # update params
            pass
        
        # *greencircle7_2* updates
        
        # if greencircle7_2 is starting this frame...
        if greencircle7_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_2.frameNStart = frameN  # exact frame index
            greencircle7_2.tStart = t  # local t and not account for scr refresh
            greencircle7_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_2.started')
            # update status
            greencircle7_2.status = STARTED
            greencircle7_2.setAutoDraw(True)
        
        # if greencircle7_2 is active this frame...
        if greencircle7_2.status == STARTED:
            # update params
            pass
        
        # *greentriangle_2* updates
        
        # if greentriangle_2 is starting this frame...
        if greentriangle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_2.frameNStart = frameN  # exact frame index
            greentriangle_2.tStart = t  # local t and not account for scr refresh
            greentriangle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_2.started')
            # update status
            greentriangle_2.status = STARTED
            greentriangle_2.setAutoDraw(True)
        
        # if greentriangle_2 is active this frame...
        if greentriangle_2.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image1_2" ---
    for thisComponent in image1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image1_2.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image1_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image1_3.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image1_3Components = [greencircle1_3, greencircle2_3, greencircle3_3, greencircle4_3, greencircle5_3, greencircle6_3, greencircle7_3, greentriangle_3]
    for thisComponent in image1_3Components:
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
    
    # --- Run Routine "image1_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_3* updates
        
        # if greencircle1_3 is starting this frame...
        if greencircle1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_3.frameNStart = frameN  # exact frame index
            greencircle1_3.tStart = t  # local t and not account for scr refresh
            greencircle1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_3.started')
            # update status
            greencircle1_3.status = STARTED
            greencircle1_3.setAutoDraw(True)
        
        # if greencircle1_3 is active this frame...
        if greencircle1_3.status == STARTED:
            # update params
            pass
        
        # *greencircle2_3* updates
        
        # if greencircle2_3 is starting this frame...
        if greencircle2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_3.frameNStart = frameN  # exact frame index
            greencircle2_3.tStart = t  # local t and not account for scr refresh
            greencircle2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_3.started')
            # update status
            greencircle2_3.status = STARTED
            greencircle2_3.setAutoDraw(True)
        
        # if greencircle2_3 is active this frame...
        if greencircle2_3.status == STARTED:
            # update params
            pass
        
        # *greencircle3_3* updates
        
        # if greencircle3_3 is starting this frame...
        if greencircle3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_3.frameNStart = frameN  # exact frame index
            greencircle3_3.tStart = t  # local t and not account for scr refresh
            greencircle3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_3.started')
            # update status
            greencircle3_3.status = STARTED
            greencircle3_3.setAutoDraw(True)
        
        # if greencircle3_3 is active this frame...
        if greencircle3_3.status == STARTED:
            # update params
            pass
        
        # *greencircle4_3* updates
        
        # if greencircle4_3 is starting this frame...
        if greencircle4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_3.frameNStart = frameN  # exact frame index
            greencircle4_3.tStart = t  # local t and not account for scr refresh
            greencircle4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_3.started')
            # update status
            greencircle4_3.status = STARTED
            greencircle4_3.setAutoDraw(True)
        
        # if greencircle4_3 is active this frame...
        if greencircle4_3.status == STARTED:
            # update params
            pass
        
        # *greencircle5_3* updates
        
        # if greencircle5_3 is starting this frame...
        if greencircle5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_3.frameNStart = frameN  # exact frame index
            greencircle5_3.tStart = t  # local t and not account for scr refresh
            greencircle5_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_3.started')
            # update status
            greencircle5_3.status = STARTED
            greencircle5_3.setAutoDraw(True)
        
        # if greencircle5_3 is active this frame...
        if greencircle5_3.status == STARTED:
            # update params
            pass
        
        # *greencircle6_3* updates
        
        # if greencircle6_3 is starting this frame...
        if greencircle6_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_3.frameNStart = frameN  # exact frame index
            greencircle6_3.tStart = t  # local t and not account for scr refresh
            greencircle6_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_3.started')
            # update status
            greencircle6_3.status = STARTED
            greencircle6_3.setAutoDraw(True)
        
        # if greencircle6_3 is active this frame...
        if greencircle6_3.status == STARTED:
            # update params
            pass
        
        # *greencircle7_3* updates
        
        # if greencircle7_3 is starting this frame...
        if greencircle7_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_3.frameNStart = frameN  # exact frame index
            greencircle7_3.tStart = t  # local t and not account for scr refresh
            greencircle7_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_3.started')
            # update status
            greencircle7_3.status = STARTED
            greencircle7_3.setAutoDraw(True)
        
        # if greencircle7_3 is active this frame...
        if greencircle7_3.status == STARTED:
            # update params
            pass
        
        # *greentriangle_3* updates
        
        # if greentriangle_3 is starting this frame...
        if greentriangle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_3.frameNStart = frameN  # exact frame index
            greentriangle_3.tStart = t  # local t and not account for scr refresh
            greentriangle_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_3.started')
            # update status
            greentriangle_3.status = STARTED
            greentriangle_3.setAutoDraw(True)
        
        # if greentriangle_3 is active this frame...
        if greentriangle_3.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image1_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image1_3" ---
    for thisComponent in image1_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image1_3.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image1_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image1_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image1_4.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image1_4Components = [greencircle1_4, greencircle2_4, greencircle3_4, greencircle4_4, greencircle5_4, greencircle6_4, greencircle7_4, greentriangle_4]
    for thisComponent in image1_4Components:
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
    
    # --- Run Routine "image1_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_4* updates
        
        # if greencircle1_4 is starting this frame...
        if greencircle1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_4.frameNStart = frameN  # exact frame index
            greencircle1_4.tStart = t  # local t and not account for scr refresh
            greencircle1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_4.started')
            # update status
            greencircle1_4.status = STARTED
            greencircle1_4.setAutoDraw(True)
        
        # if greencircle1_4 is active this frame...
        if greencircle1_4.status == STARTED:
            # update params
            pass
        
        # *greencircle2_4* updates
        
        # if greencircle2_4 is starting this frame...
        if greencircle2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_4.frameNStart = frameN  # exact frame index
            greencircle2_4.tStart = t  # local t and not account for scr refresh
            greencircle2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_4.started')
            # update status
            greencircle2_4.status = STARTED
            greencircle2_4.setAutoDraw(True)
        
        # if greencircle2_4 is active this frame...
        if greencircle2_4.status == STARTED:
            # update params
            pass
        
        # *greencircle3_4* updates
        
        # if greencircle3_4 is starting this frame...
        if greencircle3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_4.frameNStart = frameN  # exact frame index
            greencircle3_4.tStart = t  # local t and not account for scr refresh
            greencircle3_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_4.started')
            # update status
            greencircle3_4.status = STARTED
            greencircle3_4.setAutoDraw(True)
        
        # if greencircle3_4 is active this frame...
        if greencircle3_4.status == STARTED:
            # update params
            pass
        
        # *greencircle4_4* updates
        
        # if greencircle4_4 is starting this frame...
        if greencircle4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_4.frameNStart = frameN  # exact frame index
            greencircle4_4.tStart = t  # local t and not account for scr refresh
            greencircle4_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_4.started')
            # update status
            greencircle4_4.status = STARTED
            greencircle4_4.setAutoDraw(True)
        
        # if greencircle4_4 is active this frame...
        if greencircle4_4.status == STARTED:
            # update params
            pass
        
        # *greencircle5_4* updates
        
        # if greencircle5_4 is starting this frame...
        if greencircle5_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_4.frameNStart = frameN  # exact frame index
            greencircle5_4.tStart = t  # local t and not account for scr refresh
            greencircle5_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_4.started')
            # update status
            greencircle5_4.status = STARTED
            greencircle5_4.setAutoDraw(True)
        
        # if greencircle5_4 is active this frame...
        if greencircle5_4.status == STARTED:
            # update params
            pass
        
        # *greencircle6_4* updates
        
        # if greencircle6_4 is starting this frame...
        if greencircle6_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_4.frameNStart = frameN  # exact frame index
            greencircle6_4.tStart = t  # local t and not account for scr refresh
            greencircle6_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_4.started')
            # update status
            greencircle6_4.status = STARTED
            greencircle6_4.setAutoDraw(True)
        
        # if greencircle6_4 is active this frame...
        if greencircle6_4.status == STARTED:
            # update params
            pass
        
        # *greencircle7_4* updates
        
        # if greencircle7_4 is starting this frame...
        if greencircle7_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_4.frameNStart = frameN  # exact frame index
            greencircle7_4.tStart = t  # local t and not account for scr refresh
            greencircle7_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_4.started')
            # update status
            greencircle7_4.status = STARTED
            greencircle7_4.setAutoDraw(True)
        
        # if greencircle7_4 is active this frame...
        if greencircle7_4.status == STARTED:
            # update params
            pass
        
        # *greentriangle_4* updates
        
        # if greentriangle_4 is starting this frame...
        if greentriangle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_4.frameNStart = frameN  # exact frame index
            greentriangle_4.tStart = t  # local t and not account for scr refresh
            greentriangle_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_4.started')
            # update status
            greentriangle_4.status = STARTED
            greentriangle_4.setAutoDraw(True)
        
        # if greentriangle_4 is active this frame...
        if greentriangle_4.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image1_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image1_4" ---
    for thisComponent in image1_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image1_4.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image1_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image1_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image1_5.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image1_5Components = [greencircle1_5, greencircle2_5, greencircle3_5, greencircle4_5, greencircle5_5, greencircle6_5, greencircle7_5, greentriangle_5]
    for thisComponent in image1_5Components:
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
    
    # --- Run Routine "image1_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_5* updates
        
        # if greencircle1_5 is starting this frame...
        if greencircle1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_5.frameNStart = frameN  # exact frame index
            greencircle1_5.tStart = t  # local t and not account for scr refresh
            greencircle1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_5.started')
            # update status
            greencircle1_5.status = STARTED
            greencircle1_5.setAutoDraw(True)
        
        # if greencircle1_5 is active this frame...
        if greencircle1_5.status == STARTED:
            # update params
            pass
        
        # *greencircle2_5* updates
        
        # if greencircle2_5 is starting this frame...
        if greencircle2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_5.frameNStart = frameN  # exact frame index
            greencircle2_5.tStart = t  # local t and not account for scr refresh
            greencircle2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_5.started')
            # update status
            greencircle2_5.status = STARTED
            greencircle2_5.setAutoDraw(True)
        
        # if greencircle2_5 is active this frame...
        if greencircle2_5.status == STARTED:
            # update params
            pass
        
        # *greencircle3_5* updates
        
        # if greencircle3_5 is starting this frame...
        if greencircle3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_5.frameNStart = frameN  # exact frame index
            greencircle3_5.tStart = t  # local t and not account for scr refresh
            greencircle3_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_5.started')
            # update status
            greencircle3_5.status = STARTED
            greencircle3_5.setAutoDraw(True)
        
        # if greencircle3_5 is active this frame...
        if greencircle3_5.status == STARTED:
            # update params
            pass
        
        # *greencircle4_5* updates
        
        # if greencircle4_5 is starting this frame...
        if greencircle4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_5.frameNStart = frameN  # exact frame index
            greencircle4_5.tStart = t  # local t and not account for scr refresh
            greencircle4_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_5.started')
            # update status
            greencircle4_5.status = STARTED
            greencircle4_5.setAutoDraw(True)
        
        # if greencircle4_5 is active this frame...
        if greencircle4_5.status == STARTED:
            # update params
            pass
        
        # *greencircle5_5* updates
        
        # if greencircle5_5 is starting this frame...
        if greencircle5_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_5.frameNStart = frameN  # exact frame index
            greencircle5_5.tStart = t  # local t and not account for scr refresh
            greencircle5_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_5.started')
            # update status
            greencircle5_5.status = STARTED
            greencircle5_5.setAutoDraw(True)
        
        # if greencircle5_5 is active this frame...
        if greencircle5_5.status == STARTED:
            # update params
            pass
        
        # *greencircle6_5* updates
        
        # if greencircle6_5 is starting this frame...
        if greencircle6_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_5.frameNStart = frameN  # exact frame index
            greencircle6_5.tStart = t  # local t and not account for scr refresh
            greencircle6_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_5.started')
            # update status
            greencircle6_5.status = STARTED
            greencircle6_5.setAutoDraw(True)
        
        # if greencircle6_5 is active this frame...
        if greencircle6_5.status == STARTED:
            # update params
            pass
        
        # *greencircle7_5* updates
        
        # if greencircle7_5 is starting this frame...
        if greencircle7_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_5.frameNStart = frameN  # exact frame index
            greencircle7_5.tStart = t  # local t and not account for scr refresh
            greencircle7_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_5.started')
            # update status
            greencircle7_5.status = STARTED
            greencircle7_5.setAutoDraw(True)
        
        # if greencircle7_5 is active this frame...
        if greencircle7_5.status == STARTED:
            # update params
            pass
        
        # *greentriangle_5* updates
        
        # if greentriangle_5 is starting this frame...
        if greentriangle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_5.frameNStart = frameN  # exact frame index
            greentriangle_5.tStart = t  # local t and not account for scr refresh
            greentriangle_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_5.started')
            # update status
            greentriangle_5.status = STARTED
            greentriangle_5.setAutoDraw(True)
        
        # if greentriangle_5 is active this frame...
        if greentriangle_5.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image1_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image1_5" ---
    for thisComponent in image1_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image1_5.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image1_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image1_6" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image1_6.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image1_6Components = [greencircle1_6, greencircle2_6, greencircle3_6, greencircle4_6, greencircle5_6, greencircle6_6, greencircle7_6, greentriangle_6]
    for thisComponent in image1_6Components:
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
    
    # --- Run Routine "image1_6" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_6* updates
        
        # if greencircle1_6 is starting this frame...
        if greencircle1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_6.frameNStart = frameN  # exact frame index
            greencircle1_6.tStart = t  # local t and not account for scr refresh
            greencircle1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_6.started')
            # update status
            greencircle1_6.status = STARTED
            greencircle1_6.setAutoDraw(True)
        
        # if greencircle1_6 is active this frame...
        if greencircle1_6.status == STARTED:
            # update params
            pass
        
        # *greencircle2_6* updates
        
        # if greencircle2_6 is starting this frame...
        if greencircle2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_6.frameNStart = frameN  # exact frame index
            greencircle2_6.tStart = t  # local t and not account for scr refresh
            greencircle2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_6.started')
            # update status
            greencircle2_6.status = STARTED
            greencircle2_6.setAutoDraw(True)
        
        # if greencircle2_6 is active this frame...
        if greencircle2_6.status == STARTED:
            # update params
            pass
        
        # *greencircle3_6* updates
        
        # if greencircle3_6 is starting this frame...
        if greencircle3_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_6.frameNStart = frameN  # exact frame index
            greencircle3_6.tStart = t  # local t and not account for scr refresh
            greencircle3_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_6.started')
            # update status
            greencircle3_6.status = STARTED
            greencircle3_6.setAutoDraw(True)
        
        # if greencircle3_6 is active this frame...
        if greencircle3_6.status == STARTED:
            # update params
            pass
        
        # *greencircle4_6* updates
        
        # if greencircle4_6 is starting this frame...
        if greencircle4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_6.frameNStart = frameN  # exact frame index
            greencircle4_6.tStart = t  # local t and not account for scr refresh
            greencircle4_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_6.started')
            # update status
            greencircle4_6.status = STARTED
            greencircle4_6.setAutoDraw(True)
        
        # if greencircle4_6 is active this frame...
        if greencircle4_6.status == STARTED:
            # update params
            pass
        
        # *greencircle5_6* updates
        
        # if greencircle5_6 is starting this frame...
        if greencircle5_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_6.frameNStart = frameN  # exact frame index
            greencircle5_6.tStart = t  # local t and not account for scr refresh
            greencircle5_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_6.started')
            # update status
            greencircle5_6.status = STARTED
            greencircle5_6.setAutoDraw(True)
        
        # if greencircle5_6 is active this frame...
        if greencircle5_6.status == STARTED:
            # update params
            pass
        
        # *greencircle6_6* updates
        
        # if greencircle6_6 is starting this frame...
        if greencircle6_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_6.frameNStart = frameN  # exact frame index
            greencircle6_6.tStart = t  # local t and not account for scr refresh
            greencircle6_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_6.started')
            # update status
            greencircle6_6.status = STARTED
            greencircle6_6.setAutoDraw(True)
        
        # if greencircle6_6 is active this frame...
        if greencircle6_6.status == STARTED:
            # update params
            pass
        
        # *greencircle7_6* updates
        
        # if greencircle7_6 is starting this frame...
        if greencircle7_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_6.frameNStart = frameN  # exact frame index
            greencircle7_6.tStart = t  # local t and not account for scr refresh
            greencircle7_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_6.started')
            # update status
            greencircle7_6.status = STARTED
            greencircle7_6.setAutoDraw(True)
        
        # if greencircle7_6 is active this frame...
        if greencircle7_6.status == STARTED:
            # update params
            pass
        
        # *greentriangle_6* updates
        
        # if greentriangle_6 is starting this frame...
        if greentriangle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_6.frameNStart = frameN  # exact frame index
            greentriangle_6.tStart = t  # local t and not account for scr refresh
            greentriangle_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_6.started')
            # update status
            greentriangle_6.status = STARTED
            greentriangle_6.setAutoDraw(True)
        
        # if greentriangle_6 is active this frame...
        if greentriangle_6.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image1_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image1_6" ---
    for thisComponent in image1_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image1_6.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image1_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image1_7" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image1_7.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image1_7Components = [greencircle1_7, greencircle2_7, greencircle3_7, greencircle4_7, greencircle5_7, greencircle6_7, greencircle7_7, greentriangle_7]
    for thisComponent in image1_7Components:
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
    
    # --- Run Routine "image1_7" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_7* updates
        
        # if greencircle1_7 is starting this frame...
        if greencircle1_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_7.frameNStart = frameN  # exact frame index
            greencircle1_7.tStart = t  # local t and not account for scr refresh
            greencircle1_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_7.started')
            # update status
            greencircle1_7.status = STARTED
            greencircle1_7.setAutoDraw(True)
        
        # if greencircle1_7 is active this frame...
        if greencircle1_7.status == STARTED:
            # update params
            pass
        
        # *greencircle2_7* updates
        
        # if greencircle2_7 is starting this frame...
        if greencircle2_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_7.frameNStart = frameN  # exact frame index
            greencircle2_7.tStart = t  # local t and not account for scr refresh
            greencircle2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_7.started')
            # update status
            greencircle2_7.status = STARTED
            greencircle2_7.setAutoDraw(True)
        
        # if greencircle2_7 is active this frame...
        if greencircle2_7.status == STARTED:
            # update params
            pass
        
        # *greencircle3_7* updates
        
        # if greencircle3_7 is starting this frame...
        if greencircle3_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_7.frameNStart = frameN  # exact frame index
            greencircle3_7.tStart = t  # local t and not account for scr refresh
            greencircle3_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_7.started')
            # update status
            greencircle3_7.status = STARTED
            greencircle3_7.setAutoDraw(True)
        
        # if greencircle3_7 is active this frame...
        if greencircle3_7.status == STARTED:
            # update params
            pass
        
        # *greencircle4_7* updates
        
        # if greencircle4_7 is starting this frame...
        if greencircle4_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_7.frameNStart = frameN  # exact frame index
            greencircle4_7.tStart = t  # local t and not account for scr refresh
            greencircle4_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_7.started')
            # update status
            greencircle4_7.status = STARTED
            greencircle4_7.setAutoDraw(True)
        
        # if greencircle4_7 is active this frame...
        if greencircle4_7.status == STARTED:
            # update params
            pass
        
        # *greencircle5_7* updates
        
        # if greencircle5_7 is starting this frame...
        if greencircle5_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_7.frameNStart = frameN  # exact frame index
            greencircle5_7.tStart = t  # local t and not account for scr refresh
            greencircle5_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_7.started')
            # update status
            greencircle5_7.status = STARTED
            greencircle5_7.setAutoDraw(True)
        
        # if greencircle5_7 is active this frame...
        if greencircle5_7.status == STARTED:
            # update params
            pass
        
        # *greencircle6_7* updates
        
        # if greencircle6_7 is starting this frame...
        if greencircle6_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_7.frameNStart = frameN  # exact frame index
            greencircle6_7.tStart = t  # local t and not account for scr refresh
            greencircle6_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_7.started')
            # update status
            greencircle6_7.status = STARTED
            greencircle6_7.setAutoDraw(True)
        
        # if greencircle6_7 is active this frame...
        if greencircle6_7.status == STARTED:
            # update params
            pass
        
        # *greencircle7_7* updates
        
        # if greencircle7_7 is starting this frame...
        if greencircle7_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_7.frameNStart = frameN  # exact frame index
            greencircle7_7.tStart = t  # local t and not account for scr refresh
            greencircle7_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_7.started')
            # update status
            greencircle7_7.status = STARTED
            greencircle7_7.setAutoDraw(True)
        
        # if greencircle7_7 is active this frame...
        if greencircle7_7.status == STARTED:
            # update params
            pass
        
        # *greentriangle_7* updates
        
        # if greentriangle_7 is starting this frame...
        if greentriangle_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_7.frameNStart = frameN  # exact frame index
            greentriangle_7.tStart = t  # local t and not account for scr refresh
            greentriangle_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_7.started')
            # update status
            greentriangle_7.status = STARTED
            greentriangle_7.setAutoDraw(True)
        
        # if greentriangle_7 is active this frame...
        if greentriangle_7.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image1_7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image1_7" ---
    for thisComponent in image1_7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image1_7.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image1_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image1_8" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image1_8.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image1_8Components = [greencircle1_8, greencircle2_8, greencircle3_8, greencircle4_8, greencircle5_8, greencircle6_8, greencircle7_8, greentriangle_8]
    for thisComponent in image1_8Components:
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
    
    # --- Run Routine "image1_8" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_8* updates
        
        # if greencircle1_8 is starting this frame...
        if greencircle1_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_8.frameNStart = frameN  # exact frame index
            greencircle1_8.tStart = t  # local t and not account for scr refresh
            greencircle1_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_8.started')
            # update status
            greencircle1_8.status = STARTED
            greencircle1_8.setAutoDraw(True)
        
        # if greencircle1_8 is active this frame...
        if greencircle1_8.status == STARTED:
            # update params
            pass
        
        # *greencircle2_8* updates
        
        # if greencircle2_8 is starting this frame...
        if greencircle2_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_8.frameNStart = frameN  # exact frame index
            greencircle2_8.tStart = t  # local t and not account for scr refresh
            greencircle2_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_8.started')
            # update status
            greencircle2_8.status = STARTED
            greencircle2_8.setAutoDraw(True)
        
        # if greencircle2_8 is active this frame...
        if greencircle2_8.status == STARTED:
            # update params
            pass
        
        # *greencircle3_8* updates
        
        # if greencircle3_8 is starting this frame...
        if greencircle3_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_8.frameNStart = frameN  # exact frame index
            greencircle3_8.tStart = t  # local t and not account for scr refresh
            greencircle3_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_8.started')
            # update status
            greencircle3_8.status = STARTED
            greencircle3_8.setAutoDraw(True)
        
        # if greencircle3_8 is active this frame...
        if greencircle3_8.status == STARTED:
            # update params
            pass
        
        # *greencircle4_8* updates
        
        # if greencircle4_8 is starting this frame...
        if greencircle4_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_8.frameNStart = frameN  # exact frame index
            greencircle4_8.tStart = t  # local t and not account for scr refresh
            greencircle4_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_8.started')
            # update status
            greencircle4_8.status = STARTED
            greencircle4_8.setAutoDraw(True)
        
        # if greencircle4_8 is active this frame...
        if greencircle4_8.status == STARTED:
            # update params
            pass
        
        # *greencircle5_8* updates
        
        # if greencircle5_8 is starting this frame...
        if greencircle5_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_8.frameNStart = frameN  # exact frame index
            greencircle5_8.tStart = t  # local t and not account for scr refresh
            greencircle5_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_8.started')
            # update status
            greencircle5_8.status = STARTED
            greencircle5_8.setAutoDraw(True)
        
        # if greencircle5_8 is active this frame...
        if greencircle5_8.status == STARTED:
            # update params
            pass
        
        # *greencircle6_8* updates
        
        # if greencircle6_8 is starting this frame...
        if greencircle6_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_8.frameNStart = frameN  # exact frame index
            greencircle6_8.tStart = t  # local t and not account for scr refresh
            greencircle6_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_8.started')
            # update status
            greencircle6_8.status = STARTED
            greencircle6_8.setAutoDraw(True)
        
        # if greencircle6_8 is active this frame...
        if greencircle6_8.status == STARTED:
            # update params
            pass
        
        # *greencircle7_8* updates
        
        # if greencircle7_8 is starting this frame...
        if greencircle7_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_8.frameNStart = frameN  # exact frame index
            greencircle7_8.tStart = t  # local t and not account for scr refresh
            greencircle7_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_8.started')
            # update status
            greencircle7_8.status = STARTED
            greencircle7_8.setAutoDraw(True)
        
        # if greencircle7_8 is active this frame...
        if greencircle7_8.status == STARTED:
            # update params
            pass
        
        # *greentriangle_8* updates
        
        # if greentriangle_8 is starting this frame...
        if greentriangle_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_8.frameNStart = frameN  # exact frame index
            greentriangle_8.tStart = t  # local t and not account for scr refresh
            greentriangle_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_8.started')
            # update status
            greentriangle_8.status = STARTED
            greentriangle_8.setAutoDraw(True)
        
        # if greentriangle_8 is active this frame...
        if greentriangle_8.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image1_8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image1_8" ---
    for thisComponent in image1_8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image1_8.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image1_8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image3_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image3_1.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image3_1Components = [greencircle1_9, greencircle2_9, greencircle3_9, greencircle4_9, greencircle5_9, greencircle6_9, greencircle7_9, pinktriangle]
    for thisComponent in image3_1Components:
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
    
    # --- Run Routine "image3_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_9* updates
        
        # if greencircle1_9 is starting this frame...
        if greencircle1_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_9.frameNStart = frameN  # exact frame index
            greencircle1_9.tStart = t  # local t and not account for scr refresh
            greencircle1_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_9.started')
            # update status
            greencircle1_9.status = STARTED
            greencircle1_9.setAutoDraw(True)
        
        # if greencircle1_9 is active this frame...
        if greencircle1_9.status == STARTED:
            # update params
            pass
        
        # *greencircle2_9* updates
        
        # if greencircle2_9 is starting this frame...
        if greencircle2_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_9.frameNStart = frameN  # exact frame index
            greencircle2_9.tStart = t  # local t and not account for scr refresh
            greencircle2_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_9.started')
            # update status
            greencircle2_9.status = STARTED
            greencircle2_9.setAutoDraw(True)
        
        # if greencircle2_9 is active this frame...
        if greencircle2_9.status == STARTED:
            # update params
            pass
        
        # *greencircle3_9* updates
        
        # if greencircle3_9 is starting this frame...
        if greencircle3_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_9.frameNStart = frameN  # exact frame index
            greencircle3_9.tStart = t  # local t and not account for scr refresh
            greencircle3_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_9.started')
            # update status
            greencircle3_9.status = STARTED
            greencircle3_9.setAutoDraw(True)
        
        # if greencircle3_9 is active this frame...
        if greencircle3_9.status == STARTED:
            # update params
            pass
        
        # *greencircle4_9* updates
        
        # if greencircle4_9 is starting this frame...
        if greencircle4_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_9.frameNStart = frameN  # exact frame index
            greencircle4_9.tStart = t  # local t and not account for scr refresh
            greencircle4_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_9.started')
            # update status
            greencircle4_9.status = STARTED
            greencircle4_9.setAutoDraw(True)
        
        # if greencircle4_9 is active this frame...
        if greencircle4_9.status == STARTED:
            # update params
            pass
        
        # *greencircle5_9* updates
        
        # if greencircle5_9 is starting this frame...
        if greencircle5_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_9.frameNStart = frameN  # exact frame index
            greencircle5_9.tStart = t  # local t and not account for scr refresh
            greencircle5_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_9.started')
            # update status
            greencircle5_9.status = STARTED
            greencircle5_9.setAutoDraw(True)
        
        # if greencircle5_9 is active this frame...
        if greencircle5_9.status == STARTED:
            # update params
            pass
        
        # *greencircle6_9* updates
        
        # if greencircle6_9 is starting this frame...
        if greencircle6_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_9.frameNStart = frameN  # exact frame index
            greencircle6_9.tStart = t  # local t and not account for scr refresh
            greencircle6_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_9.started')
            # update status
            greencircle6_9.status = STARTED
            greencircle6_9.setAutoDraw(True)
        
        # if greencircle6_9 is active this frame...
        if greencircle6_9.status == STARTED:
            # update params
            pass
        
        # *greencircle7_9* updates
        
        # if greencircle7_9 is starting this frame...
        if greencircle7_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_9.frameNStart = frameN  # exact frame index
            greencircle7_9.tStart = t  # local t and not account for scr refresh
            greencircle7_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_9.started')
            # update status
            greencircle7_9.status = STARTED
            greencircle7_9.setAutoDraw(True)
        
        # if greencircle7_9 is active this frame...
        if greencircle7_9.status == STARTED:
            # update params
            pass
        
        # *pinktriangle* updates
        
        # if pinktriangle is starting this frame...
        if pinktriangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pinktriangle.frameNStart = frameN  # exact frame index
            pinktriangle.tStart = t  # local t and not account for scr refresh
            pinktriangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pinktriangle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pinktriangle.started')
            # update status
            pinktriangle.status = STARTED
            pinktriangle.setAutoDraw(True)
        
        # if pinktriangle is active this frame...
        if pinktriangle.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image3_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image3_1" ---
    for thisComponent in image3_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image3_1.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image3_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image3_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image3_2.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image3_2Components = [greencircle1_10, greencircle2_10, greencircle3_10, greencircle4_10, greencircle5_10, greencircle6_10, greencircle7_10, greentriangle_9]
    for thisComponent in image3_2Components:
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
    
    # --- Run Routine "image3_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_10* updates
        
        # if greencircle1_10 is starting this frame...
        if greencircle1_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_10.frameNStart = frameN  # exact frame index
            greencircle1_10.tStart = t  # local t and not account for scr refresh
            greencircle1_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_10.started')
            # update status
            greencircle1_10.status = STARTED
            greencircle1_10.setAutoDraw(True)
        
        # if greencircle1_10 is active this frame...
        if greencircle1_10.status == STARTED:
            # update params
            pass
        
        # *greencircle2_10* updates
        
        # if greencircle2_10 is starting this frame...
        if greencircle2_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_10.frameNStart = frameN  # exact frame index
            greencircle2_10.tStart = t  # local t and not account for scr refresh
            greencircle2_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_10.started')
            # update status
            greencircle2_10.status = STARTED
            greencircle2_10.setAutoDraw(True)
        
        # if greencircle2_10 is active this frame...
        if greencircle2_10.status == STARTED:
            # update params
            pass
        
        # *greencircle3_10* updates
        
        # if greencircle3_10 is starting this frame...
        if greencircle3_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_10.frameNStart = frameN  # exact frame index
            greencircle3_10.tStart = t  # local t and not account for scr refresh
            greencircle3_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_10.started')
            # update status
            greencircle3_10.status = STARTED
            greencircle3_10.setAutoDraw(True)
        
        # if greencircle3_10 is active this frame...
        if greencircle3_10.status == STARTED:
            # update params
            pass
        
        # *greencircle4_10* updates
        
        # if greencircle4_10 is starting this frame...
        if greencircle4_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_10.frameNStart = frameN  # exact frame index
            greencircle4_10.tStart = t  # local t and not account for scr refresh
            greencircle4_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_10.started')
            # update status
            greencircle4_10.status = STARTED
            greencircle4_10.setAutoDraw(True)
        
        # if greencircle4_10 is active this frame...
        if greencircle4_10.status == STARTED:
            # update params
            pass
        
        # *greencircle5_10* updates
        
        # if greencircle5_10 is starting this frame...
        if greencircle5_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_10.frameNStart = frameN  # exact frame index
            greencircle5_10.tStart = t  # local t and not account for scr refresh
            greencircle5_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_10.started')
            # update status
            greencircle5_10.status = STARTED
            greencircle5_10.setAutoDraw(True)
        
        # if greencircle5_10 is active this frame...
        if greencircle5_10.status == STARTED:
            # update params
            pass
        
        # *greencircle6_10* updates
        
        # if greencircle6_10 is starting this frame...
        if greencircle6_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_10.frameNStart = frameN  # exact frame index
            greencircle6_10.tStart = t  # local t and not account for scr refresh
            greencircle6_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_10.started')
            # update status
            greencircle6_10.status = STARTED
            greencircle6_10.setAutoDraw(True)
        
        # if greencircle6_10 is active this frame...
        if greencircle6_10.status == STARTED:
            # update params
            pass
        
        # *greencircle7_10* updates
        
        # if greencircle7_10 is starting this frame...
        if greencircle7_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_10.frameNStart = frameN  # exact frame index
            greencircle7_10.tStart = t  # local t and not account for scr refresh
            greencircle7_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_10.started')
            # update status
            greencircle7_10.status = STARTED
            greencircle7_10.setAutoDraw(True)
        
        # if greencircle7_10 is active this frame...
        if greencircle7_10.status == STARTED:
            # update params
            pass
        
        # *greentriangle_9* updates
        
        # if greentriangle_9 is starting this frame...
        if greentriangle_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_9.frameNStart = frameN  # exact frame index
            greentriangle_9.tStart = t  # local t and not account for scr refresh
            greentriangle_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_9.started')
            # update status
            greentriangle_9.status = STARTED
            greentriangle_9.setAutoDraw(True)
        
        # if greentriangle_9 is active this frame...
        if greentriangle_9.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image3_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image3_2" ---
    for thisComponent in image3_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image3_2.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image3_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image3_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image3_3.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image3_3Components = [greencircle1_11, greencircle2_11, greencircle3_11, greencircle4_11, greencircle5_11, greencircle6_11, greencircle7_11, greentriangle_10]
    for thisComponent in image3_3Components:
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
    
    # --- Run Routine "image3_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_11* updates
        
        # if greencircle1_11 is starting this frame...
        if greencircle1_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_11.frameNStart = frameN  # exact frame index
            greencircle1_11.tStart = t  # local t and not account for scr refresh
            greencircle1_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_11.started')
            # update status
            greencircle1_11.status = STARTED
            greencircle1_11.setAutoDraw(True)
        
        # if greencircle1_11 is active this frame...
        if greencircle1_11.status == STARTED:
            # update params
            pass
        
        # *greencircle2_11* updates
        
        # if greencircle2_11 is starting this frame...
        if greencircle2_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_11.frameNStart = frameN  # exact frame index
            greencircle2_11.tStart = t  # local t and not account for scr refresh
            greencircle2_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_11.started')
            # update status
            greencircle2_11.status = STARTED
            greencircle2_11.setAutoDraw(True)
        
        # if greencircle2_11 is active this frame...
        if greencircle2_11.status == STARTED:
            # update params
            pass
        
        # *greencircle3_11* updates
        
        # if greencircle3_11 is starting this frame...
        if greencircle3_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_11.frameNStart = frameN  # exact frame index
            greencircle3_11.tStart = t  # local t and not account for scr refresh
            greencircle3_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_11.started')
            # update status
            greencircle3_11.status = STARTED
            greencircle3_11.setAutoDraw(True)
        
        # if greencircle3_11 is active this frame...
        if greencircle3_11.status == STARTED:
            # update params
            pass
        
        # *greencircle4_11* updates
        
        # if greencircle4_11 is starting this frame...
        if greencircle4_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_11.frameNStart = frameN  # exact frame index
            greencircle4_11.tStart = t  # local t and not account for scr refresh
            greencircle4_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_11.started')
            # update status
            greencircle4_11.status = STARTED
            greencircle4_11.setAutoDraw(True)
        
        # if greencircle4_11 is active this frame...
        if greencircle4_11.status == STARTED:
            # update params
            pass
        
        # *greencircle5_11* updates
        
        # if greencircle5_11 is starting this frame...
        if greencircle5_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_11.frameNStart = frameN  # exact frame index
            greencircle5_11.tStart = t  # local t and not account for scr refresh
            greencircle5_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_11.started')
            # update status
            greencircle5_11.status = STARTED
            greencircle5_11.setAutoDraw(True)
        
        # if greencircle5_11 is active this frame...
        if greencircle5_11.status == STARTED:
            # update params
            pass
        
        # *greencircle6_11* updates
        
        # if greencircle6_11 is starting this frame...
        if greencircle6_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_11.frameNStart = frameN  # exact frame index
            greencircle6_11.tStart = t  # local t and not account for scr refresh
            greencircle6_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_11.started')
            # update status
            greencircle6_11.status = STARTED
            greencircle6_11.setAutoDraw(True)
        
        # if greencircle6_11 is active this frame...
        if greencircle6_11.status == STARTED:
            # update params
            pass
        
        # *greencircle7_11* updates
        
        # if greencircle7_11 is starting this frame...
        if greencircle7_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_11.frameNStart = frameN  # exact frame index
            greencircle7_11.tStart = t  # local t and not account for scr refresh
            greencircle7_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_11.started')
            # update status
            greencircle7_11.status = STARTED
            greencircle7_11.setAutoDraw(True)
        
        # if greencircle7_11 is active this frame...
        if greencircle7_11.status == STARTED:
            # update params
            pass
        
        # *greentriangle_10* updates
        
        # if greentriangle_10 is starting this frame...
        if greentriangle_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_10.frameNStart = frameN  # exact frame index
            greentriangle_10.tStart = t  # local t and not account for scr refresh
            greentriangle_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_10.started')
            # update status
            greentriangle_10.status = STARTED
            greentriangle_10.setAutoDraw(True)
        
        # if greentriangle_10 is active this frame...
        if greentriangle_10.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image3_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image3_3" ---
    for thisComponent in image3_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image3_3.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image3_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image3_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image3_4.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image3_4Components = [greencircle1_12, greencircle2_12, greencircle3_12, greencircle4_12, greencircle5_12, greencircle6_12, greencircle7_12, greentriangle_11]
    for thisComponent in image3_4Components:
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
    
    # --- Run Routine "image3_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_12* updates
        
        # if greencircle1_12 is starting this frame...
        if greencircle1_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_12.frameNStart = frameN  # exact frame index
            greencircle1_12.tStart = t  # local t and not account for scr refresh
            greencircle1_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_12.started')
            # update status
            greencircle1_12.status = STARTED
            greencircle1_12.setAutoDraw(True)
        
        # if greencircle1_12 is active this frame...
        if greencircle1_12.status == STARTED:
            # update params
            pass
        
        # *greencircle2_12* updates
        
        # if greencircle2_12 is starting this frame...
        if greencircle2_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_12.frameNStart = frameN  # exact frame index
            greencircle2_12.tStart = t  # local t and not account for scr refresh
            greencircle2_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_12.started')
            # update status
            greencircle2_12.status = STARTED
            greencircle2_12.setAutoDraw(True)
        
        # if greencircle2_12 is active this frame...
        if greencircle2_12.status == STARTED:
            # update params
            pass
        
        # *greencircle3_12* updates
        
        # if greencircle3_12 is starting this frame...
        if greencircle3_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_12.frameNStart = frameN  # exact frame index
            greencircle3_12.tStart = t  # local t and not account for scr refresh
            greencircle3_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_12.started')
            # update status
            greencircle3_12.status = STARTED
            greencircle3_12.setAutoDraw(True)
        
        # if greencircle3_12 is active this frame...
        if greencircle3_12.status == STARTED:
            # update params
            pass
        
        # *greencircle4_12* updates
        
        # if greencircle4_12 is starting this frame...
        if greencircle4_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_12.frameNStart = frameN  # exact frame index
            greencircle4_12.tStart = t  # local t and not account for scr refresh
            greencircle4_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_12.started')
            # update status
            greencircle4_12.status = STARTED
            greencircle4_12.setAutoDraw(True)
        
        # if greencircle4_12 is active this frame...
        if greencircle4_12.status == STARTED:
            # update params
            pass
        
        # *greencircle5_12* updates
        
        # if greencircle5_12 is starting this frame...
        if greencircle5_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_12.frameNStart = frameN  # exact frame index
            greencircle5_12.tStart = t  # local t and not account for scr refresh
            greencircle5_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_12.started')
            # update status
            greencircle5_12.status = STARTED
            greencircle5_12.setAutoDraw(True)
        
        # if greencircle5_12 is active this frame...
        if greencircle5_12.status == STARTED:
            # update params
            pass
        
        # *greencircle6_12* updates
        
        # if greencircle6_12 is starting this frame...
        if greencircle6_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_12.frameNStart = frameN  # exact frame index
            greencircle6_12.tStart = t  # local t and not account for scr refresh
            greencircle6_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_12.started')
            # update status
            greencircle6_12.status = STARTED
            greencircle6_12.setAutoDraw(True)
        
        # if greencircle6_12 is active this frame...
        if greencircle6_12.status == STARTED:
            # update params
            pass
        
        # *greencircle7_12* updates
        
        # if greencircle7_12 is starting this frame...
        if greencircle7_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_12.frameNStart = frameN  # exact frame index
            greencircle7_12.tStart = t  # local t and not account for scr refresh
            greencircle7_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_12.started')
            # update status
            greencircle7_12.status = STARTED
            greencircle7_12.setAutoDraw(True)
        
        # if greencircle7_12 is active this frame...
        if greencircle7_12.status == STARTED:
            # update params
            pass
        
        # *greentriangle_11* updates
        
        # if greentriangle_11 is starting this frame...
        if greentriangle_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_11.frameNStart = frameN  # exact frame index
            greentriangle_11.tStart = t  # local t and not account for scr refresh
            greentriangle_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_11.started')
            # update status
            greentriangle_11.status = STARTED
            greentriangle_11.setAutoDraw(True)
        
        # if greentriangle_11 is active this frame...
        if greentriangle_11.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image3_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image3_4" ---
    for thisComponent in image3_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image3_4.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image3_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image3_5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image3_5.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image3_5Components = [greencircle1_13, greencircle2_13, greencircle3_13, greencircle4_13, greencircle5_13, greencircle6_13, greencircle7_13, greentriangle_12]
    for thisComponent in image3_5Components:
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
    
    # --- Run Routine "image3_5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_13* updates
        
        # if greencircle1_13 is starting this frame...
        if greencircle1_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_13.frameNStart = frameN  # exact frame index
            greencircle1_13.tStart = t  # local t and not account for scr refresh
            greencircle1_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_13.started')
            # update status
            greencircle1_13.status = STARTED
            greencircle1_13.setAutoDraw(True)
        
        # if greencircle1_13 is active this frame...
        if greencircle1_13.status == STARTED:
            # update params
            pass
        
        # *greencircle2_13* updates
        
        # if greencircle2_13 is starting this frame...
        if greencircle2_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_13.frameNStart = frameN  # exact frame index
            greencircle2_13.tStart = t  # local t and not account for scr refresh
            greencircle2_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_13.started')
            # update status
            greencircle2_13.status = STARTED
            greencircle2_13.setAutoDraw(True)
        
        # if greencircle2_13 is active this frame...
        if greencircle2_13.status == STARTED:
            # update params
            pass
        
        # *greencircle3_13* updates
        
        # if greencircle3_13 is starting this frame...
        if greencircle3_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_13.frameNStart = frameN  # exact frame index
            greencircle3_13.tStart = t  # local t and not account for scr refresh
            greencircle3_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_13.started')
            # update status
            greencircle3_13.status = STARTED
            greencircle3_13.setAutoDraw(True)
        
        # if greencircle3_13 is active this frame...
        if greencircle3_13.status == STARTED:
            # update params
            pass
        
        # *greencircle4_13* updates
        
        # if greencircle4_13 is starting this frame...
        if greencircle4_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_13.frameNStart = frameN  # exact frame index
            greencircle4_13.tStart = t  # local t and not account for scr refresh
            greencircle4_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_13.started')
            # update status
            greencircle4_13.status = STARTED
            greencircle4_13.setAutoDraw(True)
        
        # if greencircle4_13 is active this frame...
        if greencircle4_13.status == STARTED:
            # update params
            pass
        
        # *greencircle5_13* updates
        
        # if greencircle5_13 is starting this frame...
        if greencircle5_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_13.frameNStart = frameN  # exact frame index
            greencircle5_13.tStart = t  # local t and not account for scr refresh
            greencircle5_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_13.started')
            # update status
            greencircle5_13.status = STARTED
            greencircle5_13.setAutoDraw(True)
        
        # if greencircle5_13 is active this frame...
        if greencircle5_13.status == STARTED:
            # update params
            pass
        
        # *greencircle6_13* updates
        
        # if greencircle6_13 is starting this frame...
        if greencircle6_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_13.frameNStart = frameN  # exact frame index
            greencircle6_13.tStart = t  # local t and not account for scr refresh
            greencircle6_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_13.started')
            # update status
            greencircle6_13.status = STARTED
            greencircle6_13.setAutoDraw(True)
        
        # if greencircle6_13 is active this frame...
        if greencircle6_13.status == STARTED:
            # update params
            pass
        
        # *greencircle7_13* updates
        
        # if greencircle7_13 is starting this frame...
        if greencircle7_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_13.frameNStart = frameN  # exact frame index
            greencircle7_13.tStart = t  # local t and not account for scr refresh
            greencircle7_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_13.started')
            # update status
            greencircle7_13.status = STARTED
            greencircle7_13.setAutoDraw(True)
        
        # if greencircle7_13 is active this frame...
        if greencircle7_13.status == STARTED:
            # update params
            pass
        
        # *greentriangle_12* updates
        
        # if greentriangle_12 is starting this frame...
        if greentriangle_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_12.frameNStart = frameN  # exact frame index
            greentriangle_12.tStart = t  # local t and not account for scr refresh
            greentriangle_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_12.started')
            # update status
            greentriangle_12.status = STARTED
            greentriangle_12.setAutoDraw(True)
        
        # if greentriangle_12 is active this frame...
        if greentriangle_12.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image3_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image3_5" ---
    for thisComponent in image3_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image3_5.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image3_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image3_6" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image3_6.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image3_6Components = [greencircle1_14, greencircle2_14, greencircle3_14, greencircle4_14, greencircle5_14, greencircle6_14, greencircle7_14, greentriangle_13]
    for thisComponent in image3_6Components:
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
    
    # --- Run Routine "image3_6" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_14* updates
        
        # if greencircle1_14 is starting this frame...
        if greencircle1_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_14.frameNStart = frameN  # exact frame index
            greencircle1_14.tStart = t  # local t and not account for scr refresh
            greencircle1_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_14.started')
            # update status
            greencircle1_14.status = STARTED
            greencircle1_14.setAutoDraw(True)
        
        # if greencircle1_14 is active this frame...
        if greencircle1_14.status == STARTED:
            # update params
            pass
        
        # *greencircle2_14* updates
        
        # if greencircle2_14 is starting this frame...
        if greencircle2_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_14.frameNStart = frameN  # exact frame index
            greencircle2_14.tStart = t  # local t and not account for scr refresh
            greencircle2_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_14.started')
            # update status
            greencircle2_14.status = STARTED
            greencircle2_14.setAutoDraw(True)
        
        # if greencircle2_14 is active this frame...
        if greencircle2_14.status == STARTED:
            # update params
            pass
        
        # *greencircle3_14* updates
        
        # if greencircle3_14 is starting this frame...
        if greencircle3_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_14.frameNStart = frameN  # exact frame index
            greencircle3_14.tStart = t  # local t and not account for scr refresh
            greencircle3_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_14.started')
            # update status
            greencircle3_14.status = STARTED
            greencircle3_14.setAutoDraw(True)
        
        # if greencircle3_14 is active this frame...
        if greencircle3_14.status == STARTED:
            # update params
            pass
        
        # *greencircle4_14* updates
        
        # if greencircle4_14 is starting this frame...
        if greencircle4_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_14.frameNStart = frameN  # exact frame index
            greencircle4_14.tStart = t  # local t and not account for scr refresh
            greencircle4_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_14.started')
            # update status
            greencircle4_14.status = STARTED
            greencircle4_14.setAutoDraw(True)
        
        # if greencircle4_14 is active this frame...
        if greencircle4_14.status == STARTED:
            # update params
            pass
        
        # *greencircle5_14* updates
        
        # if greencircle5_14 is starting this frame...
        if greencircle5_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_14.frameNStart = frameN  # exact frame index
            greencircle5_14.tStart = t  # local t and not account for scr refresh
            greencircle5_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_14.started')
            # update status
            greencircle5_14.status = STARTED
            greencircle5_14.setAutoDraw(True)
        
        # if greencircle5_14 is active this frame...
        if greencircle5_14.status == STARTED:
            # update params
            pass
        
        # *greencircle6_14* updates
        
        # if greencircle6_14 is starting this frame...
        if greencircle6_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_14.frameNStart = frameN  # exact frame index
            greencircle6_14.tStart = t  # local t and not account for scr refresh
            greencircle6_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_14.started')
            # update status
            greencircle6_14.status = STARTED
            greencircle6_14.setAutoDraw(True)
        
        # if greencircle6_14 is active this frame...
        if greencircle6_14.status == STARTED:
            # update params
            pass
        
        # *greencircle7_14* updates
        
        # if greencircle7_14 is starting this frame...
        if greencircle7_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_14.frameNStart = frameN  # exact frame index
            greencircle7_14.tStart = t  # local t and not account for scr refresh
            greencircle7_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_14.started')
            # update status
            greencircle7_14.status = STARTED
            greencircle7_14.setAutoDraw(True)
        
        # if greencircle7_14 is active this frame...
        if greencircle7_14.status == STARTED:
            # update params
            pass
        
        # *greentriangle_13* updates
        
        # if greentriangle_13 is starting this frame...
        if greentriangle_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_13.frameNStart = frameN  # exact frame index
            greentriangle_13.tStart = t  # local t and not account for scr refresh
            greentriangle_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_13.started')
            # update status
            greentriangle_13.status = STARTED
            greentriangle_13.setAutoDraw(True)
        
        # if greentriangle_13 is active this frame...
        if greentriangle_13.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image3_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image3_6" ---
    for thisComponent in image3_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image3_6.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image3_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image3_7" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image3_7.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image3_7Components = [greencircle1_15, greencircle2_15, greencircle3_15, greencircle4_15, greencircle5_15, greencircle6_15, greencircle7_15, greentriangle_14]
    for thisComponent in image3_7Components:
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
    
    # --- Run Routine "image3_7" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_15* updates
        
        # if greencircle1_15 is starting this frame...
        if greencircle1_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_15.frameNStart = frameN  # exact frame index
            greencircle1_15.tStart = t  # local t and not account for scr refresh
            greencircle1_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_15.started')
            # update status
            greencircle1_15.status = STARTED
            greencircle1_15.setAutoDraw(True)
        
        # if greencircle1_15 is active this frame...
        if greencircle1_15.status == STARTED:
            # update params
            pass
        
        # *greencircle2_15* updates
        
        # if greencircle2_15 is starting this frame...
        if greencircle2_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_15.frameNStart = frameN  # exact frame index
            greencircle2_15.tStart = t  # local t and not account for scr refresh
            greencircle2_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_15.started')
            # update status
            greencircle2_15.status = STARTED
            greencircle2_15.setAutoDraw(True)
        
        # if greencircle2_15 is active this frame...
        if greencircle2_15.status == STARTED:
            # update params
            pass
        
        # *greencircle3_15* updates
        
        # if greencircle3_15 is starting this frame...
        if greencircle3_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_15.frameNStart = frameN  # exact frame index
            greencircle3_15.tStart = t  # local t and not account for scr refresh
            greencircle3_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_15.started')
            # update status
            greencircle3_15.status = STARTED
            greencircle3_15.setAutoDraw(True)
        
        # if greencircle3_15 is active this frame...
        if greencircle3_15.status == STARTED:
            # update params
            pass
        
        # *greencircle4_15* updates
        
        # if greencircle4_15 is starting this frame...
        if greencircle4_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_15.frameNStart = frameN  # exact frame index
            greencircle4_15.tStart = t  # local t and not account for scr refresh
            greencircle4_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_15.started')
            # update status
            greencircle4_15.status = STARTED
            greencircle4_15.setAutoDraw(True)
        
        # if greencircle4_15 is active this frame...
        if greencircle4_15.status == STARTED:
            # update params
            pass
        
        # *greencircle5_15* updates
        
        # if greencircle5_15 is starting this frame...
        if greencircle5_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_15.frameNStart = frameN  # exact frame index
            greencircle5_15.tStart = t  # local t and not account for scr refresh
            greencircle5_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_15.started')
            # update status
            greencircle5_15.status = STARTED
            greencircle5_15.setAutoDraw(True)
        
        # if greencircle5_15 is active this frame...
        if greencircle5_15.status == STARTED:
            # update params
            pass
        
        # *greencircle6_15* updates
        
        # if greencircle6_15 is starting this frame...
        if greencircle6_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_15.frameNStart = frameN  # exact frame index
            greencircle6_15.tStart = t  # local t and not account for scr refresh
            greencircle6_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_15.started')
            # update status
            greencircle6_15.status = STARTED
            greencircle6_15.setAutoDraw(True)
        
        # if greencircle6_15 is active this frame...
        if greencircle6_15.status == STARTED:
            # update params
            pass
        
        # *greencircle7_15* updates
        
        # if greencircle7_15 is starting this frame...
        if greencircle7_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_15.frameNStart = frameN  # exact frame index
            greencircle7_15.tStart = t  # local t and not account for scr refresh
            greencircle7_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_15.started')
            # update status
            greencircle7_15.status = STARTED
            greencircle7_15.setAutoDraw(True)
        
        # if greencircle7_15 is active this frame...
        if greencircle7_15.status == STARTED:
            # update params
            pass
        
        # *greentriangle_14* updates
        
        # if greentriangle_14 is starting this frame...
        if greentriangle_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_14.frameNStart = frameN  # exact frame index
            greentriangle_14.tStart = t  # local t and not account for scr refresh
            greentriangle_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_14.started')
            # update status
            greentriangle_14.status = STARTED
            greentriangle_14.setAutoDraw(True)
        
        # if greentriangle_14 is active this frame...
        if greentriangle_14.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image3_7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image3_7" ---
    for thisComponent in image3_7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image3_7.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image3_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "image3_8" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('image3_8.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    image3_8Components = [greencircle1_16, greencircle2_16, greencircle3_16, greencircle4_16, greencircle5_16, greencircle6_16, greencircle7_16, greentriangle_15]
    for thisComponent in image3_8Components:
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
    
    # --- Run Routine "image3_8" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 1-frameTolerance:
            continueRoutine = False
        
        # *greencircle1_16* updates
        
        # if greencircle1_16 is starting this frame...
        if greencircle1_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle1_16.frameNStart = frameN  # exact frame index
            greencircle1_16.tStart = t  # local t and not account for scr refresh
            greencircle1_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle1_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle1_16.started')
            # update status
            greencircle1_16.status = STARTED
            greencircle1_16.setAutoDraw(True)
        
        # if greencircle1_16 is active this frame...
        if greencircle1_16.status == STARTED:
            # update params
            pass
        
        # *greencircle2_16* updates
        
        # if greencircle2_16 is starting this frame...
        if greencircle2_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle2_16.frameNStart = frameN  # exact frame index
            greencircle2_16.tStart = t  # local t and not account for scr refresh
            greencircle2_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle2_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle2_16.started')
            # update status
            greencircle2_16.status = STARTED
            greencircle2_16.setAutoDraw(True)
        
        # if greencircle2_16 is active this frame...
        if greencircle2_16.status == STARTED:
            # update params
            pass
        
        # *greencircle3_16* updates
        
        # if greencircle3_16 is starting this frame...
        if greencircle3_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle3_16.frameNStart = frameN  # exact frame index
            greencircle3_16.tStart = t  # local t and not account for scr refresh
            greencircle3_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle3_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle3_16.started')
            # update status
            greencircle3_16.status = STARTED
            greencircle3_16.setAutoDraw(True)
        
        # if greencircle3_16 is active this frame...
        if greencircle3_16.status == STARTED:
            # update params
            pass
        
        # *greencircle4_16* updates
        
        # if greencircle4_16 is starting this frame...
        if greencircle4_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle4_16.frameNStart = frameN  # exact frame index
            greencircle4_16.tStart = t  # local t and not account for scr refresh
            greencircle4_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle4_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle4_16.started')
            # update status
            greencircle4_16.status = STARTED
            greencircle4_16.setAutoDraw(True)
        
        # if greencircle4_16 is active this frame...
        if greencircle4_16.status == STARTED:
            # update params
            pass
        
        # *greencircle5_16* updates
        
        # if greencircle5_16 is starting this frame...
        if greencircle5_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle5_16.frameNStart = frameN  # exact frame index
            greencircle5_16.tStart = t  # local t and not account for scr refresh
            greencircle5_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle5_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle5_16.started')
            # update status
            greencircle5_16.status = STARTED
            greencircle5_16.setAutoDraw(True)
        
        # if greencircle5_16 is active this frame...
        if greencircle5_16.status == STARTED:
            # update params
            pass
        
        # *greencircle6_16* updates
        
        # if greencircle6_16 is starting this frame...
        if greencircle6_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle6_16.frameNStart = frameN  # exact frame index
            greencircle6_16.tStart = t  # local t and not account for scr refresh
            greencircle6_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle6_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle6_16.started')
            # update status
            greencircle6_16.status = STARTED
            greencircle6_16.setAutoDraw(True)
        
        # if greencircle6_16 is active this frame...
        if greencircle6_16.status == STARTED:
            # update params
            pass
        
        # *greencircle7_16* updates
        
        # if greencircle7_16 is starting this frame...
        if greencircle7_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greencircle7_16.frameNStart = frameN  # exact frame index
            greencircle7_16.tStart = t  # local t and not account for scr refresh
            greencircle7_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greencircle7_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greencircle7_16.started')
            # update status
            greencircle7_16.status = STARTED
            greencircle7_16.setAutoDraw(True)
        
        # if greencircle7_16 is active this frame...
        if greencircle7_16.status == STARTED:
            # update params
            pass
        
        # *greentriangle_15* updates
        
        # if greentriangle_15 is starting this frame...
        if greentriangle_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greentriangle_15.frameNStart = frameN  # exact frame index
            greentriangle_15.tStart = t  # local t and not account for scr refresh
            greentriangle_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greentriangle_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'greentriangle_15.started')
            # update status
            greentriangle_15.status = STARTED
            greentriangle_15.setAutoDraw(True)
        
        # if greentriangle_15 is active this frame...
        if greentriangle_15.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in image3_8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image3_8" ---
    for thisComponent in image3_8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('image3_8.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "image3_8" was not non-slip safe, so reset the non-slip timer
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

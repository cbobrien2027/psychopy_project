/****************** 
 * Test2_Run *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'test2_run';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(routine_1RoutineBegin());
flowScheduler.add(routine_1RoutineEachFrame());
flowScheduler.add(routine_1RoutineEnd());
flowScheduler.add(Instruction_PageRoutineBegin());
flowScheduler.add(Instruction_PageRoutineEachFrame());
flowScheduler.add(Instruction_PageRoutineEnd());
const trials24LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials24LoopBegin(trials24LoopScheduler));
flowScheduler.add(trials24LoopScheduler);
flowScheduler.add(trials24LoopEnd);


flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "routine_1"
  routine_1Clock = new util.Clock();
  // Initialize components for Routine "Instruction_Page"
  Instruction_PageClock = new util.Clock();
  // Run 'Begin Experiment' code from code_2
  import {clock, core, event, visual} from 'psychopy';
  import {keyboard} from 'psychopy/hardware';
  mywin = new visual.Window([600, 600], {"monitor": "testMonitor", "units": "deg", "color": [(- 1), (- 1), (- 1)]});
  text_msg = new visual.TextStim({"win": mywin, "text": "Welcome to the experiment. Choose the triangle in the following images. Press the space bar to begin."});
  text_msg.draw();
  mywin.update();
  instruction_msg_time = psychoJS.eventManager.waitKeys({"keyList": ["space"]});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function routine_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'routine_1' ---
    t = 0;
    routine_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('routine_1.started', globalClock.getTime());
    // keep track of which components have finished
    routine_1Components = [];
    
    for (const thisComponent of routine_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function routine_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'routine_1' ---
    // get current time
    t = routine_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of routine_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function routine_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'routine_1' ---
    for (const thisComponent of routine_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('routine_1.stopped', globalClock.getTime());
    // the Routine "routine_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Instruction_PageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction_Page' ---
    t = 0;
    Instruction_PageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instruction_Page.started', globalClock.getTime());
    // keep track of which components have finished
    Instruction_PageComponents = [];
    
    for (const thisComponent of Instruction_PageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Instruction_PageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction_Page' ---
    // get current time
    t = Instruction_PageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction_PageComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Instruction_PageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction_Page' ---
    for (const thisComponent of Instruction_PageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instruction_Page.stopped', globalClock.getTime());
    // the Routine "Instruction_Page" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trials24LoopBegin(trials24LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials24 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: undefined, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: '/Users/carolineobrien/Downloads/Conditions Spreadsheet.xlsx',
      seed: undefined, name: 'trials24'
    });
    psychoJS.experiment.addLoop(trials24); // add the loop to the experiment
    currentLoop = trials24;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials24 of trials24) {
      snapshot = trials24.getSnapshot();
      trials24LoopScheduler.add(importConditions(snapshot));
      trials24LoopScheduler.add(trialRoutineBegin(snapshot));
      trials24LoopScheduler.add(trialRoutineEachFrame());
      trials24LoopScheduler.add(trialRoutineEnd(snapshot));
      trials24LoopScheduler.add(trials24LoopEndIteration(trials24LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trials24LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials24);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials24LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    // Run 'Begin Routine' code from code
    import {clock, core, event, visual} from 'psychopy';
    import {keyboard} from 'psychopy/hardware';
    mywin = new visual.Window([600, 600], {"monitor": "testMonitor", "units": "deg", "color": [(- 1), (- 1), (- 1)]});
    text_msg = new visual.TextStim({"win": mywin, "text": "Welcome to the experiment. Choose the triangle in the following images. Press the space bar to begin."});
    text_msg.draw();
    mywin.update();
    instruction_msg_time = psychoJS.eventManager.waitKeys({"keyList": ["space"]});
    xvalues_range = [0, 3, 4, 3, 0, (- 3), (- 4), (- 3)];
    yvalues_range = [4, 3, 0, (- 3), (- 4), (- 3), 0, 3];
    possible_positions = [[0, 4], [3, 3], [4, 0], [3, (- 3)], [0, (- 4)], [(- 3), (- 3)], [(- 4), 0], [(- 3), 3]];
    for (var ii, _pj_c = 0, _pj_a = possible_positions, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        ii = _pj_a[_pj_c];
        if ((ii === triangle_pos)) {
            triangle1 = new visual.Polygon({"win": mywin, "edges": 3, "radius": 1.25, "colorSpace": "rgb", "pos": ii});
            if ((triangle_color === "g")) {
                triangle1.color = [0, 255, 0];
            } else {
                triangle1.color = [255, 0, 0];
            }
            triangle1.draw();
        } else {
            circle1 = new visual.Circle({"win": mywin, "radius": 1, "edges": "circle", "colorSpace": "rgb", "pos": ii});
            if ((ii === pink_circle_pos)) {
                circle1.color(255, 0, 0);
            } else {
                circle1.color(0, 255, 0);
            }
            circle1.draw();
        }
        mywin.update();
    }
    
    // keep track of which components have finished
    trialComponents = [];
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

/************************** 
 * Creatingimagesnew *
 **************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'creatingimagesNEW';  // from the Builder filename that created this script
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
  fullscr: false,
  color: new util.Color([-1,-1,-1]),
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
flowScheduler.add(Welcome_PageRoutineBegin());
flowScheduler.add(Welcome_PageRoutineEachFrame());
flowScheduler.add(Welcome_PageRoutineEnd());
flowScheduler.add(Test_Trial_routine_instructionsRoutineBegin());
flowScheduler.add(Test_Trial_routine_instructionsRoutineEachFrame());
flowScheduler.add(Test_Trial_routine_instructionsRoutineEnd());
const test_trial_before_experimentLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(test_trial_before_experimentLoopBegin(test_trial_before_experimentLoopScheduler));
flowScheduler.add(test_trial_before_experimentLoopScheduler);
flowScheduler.add(test_trial_before_experimentLoopEnd);


flowScheduler.add(Actual_Trial_InstructionsRoutineBegin());
flowScheduler.add(Actual_Trial_InstructionsRoutineEachFrame());
flowScheduler.add(Actual_Trial_InstructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


flowScheduler.add(End_RoutineRoutineBegin());
flowScheduler.add(End_RoutineRoutineEachFrame());
flowScheduler.add(End_RoutineRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Conditions_Spreadsheet_for_test_trials.csv', 'path': 'Conditions_Spreadsheet_for_test_trials.csv'},
    {'name': 'ConditionsSpreadSheet.xlsx', 'path': 'ConditionsSpreadSheet.xlsx'},
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
  // Initialize components for Routine "Welcome_Page"
  Welcome_PageClock = new util.Clock();
  textWelcomePage = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcomePage',
    text: 'Hello!\n\nThank you for participating in this experiment. Please read the instructions before beginning. \n\nInstructions:\nYou will be presented with a variety of shapes. Your task is to choose the triangle. You will not be able to move on to the next slide unless you correctly choose the triangle with your mouse. Once you begin the experiment you will not be able to leave until you have successfully completed all tasks. This experiment will take approximately 5 minutes. \n\nPLEASE PRESS THE SPACE BAR TO BEGIN THE EXPERIMENT',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.05)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Test_Trial_routine_instructions"
  Test_Trial_routine_instructionsClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'The following images will serve as test trials so that you can get accustomed to how the actual trials will proceed. Please note that once you begin, it is advised that you do not exit the program at any point in time. \n\nPlease press the SPACE BAR to continue to the test trials. \n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test_trial"
  test_trialClock = new util.Clock();
  // Initialize components for Routine "Actual_Trial_Instructions"
  Actual_Trial_InstructionsClock = new util.Clock();
  actual_trial_intructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'actual_trial_intructions',
    text: 'Congratulations on competing the trial! You will now begin the actual experiment. Try your best to choose the triangle in as little time as possible. For proper data collection, it is advised that you do not exit the trial once it begins. \n\nPlease press the SPACE BAR to continue to the trial. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Real_Trials"
  Real_TrialsClock = new util.Clock();
  // Initialize components for Routine "End_Routine"
  End_RoutineClock = new util.Clock();
  End_Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'End_Text',
    text: 'Thank you for completing the experiment! Please press the SPACE BAR to exit the program. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function Welcome_PageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome_Page' ---
    t = 0;
    Welcome_PageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Welcome_Page.started', globalClock.getTime());
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    Welcome_PageComponents = [];
    Welcome_PageComponents.push(textWelcomePage);
    Welcome_PageComponents.push(key_resp);
    
    for (const thisComponent of Welcome_PageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Welcome_PageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome_Page' ---
    // get current time
    t = Welcome_PageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcomePage* updates
    if (t >= 0.0 && textWelcomePage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcomePage.tStart = t;  // (not accounting for frame time here)
      textWelcomePage.frameNStart = frameN;  // exact frame index
      
      textWelcomePage.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 2 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Welcome_PageComponents)
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

function Welcome_PageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome_Page' ---
    for (const thisComponent of Welcome_PageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Welcome_Page.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Welcome_Page" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Test_Trial_routine_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Test_Trial_routine_instructions' ---
    t = 0;
    Test_Trial_routine_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Test_Trial_routine_instructions.started', globalClock.getTime());
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    Test_Trial_routine_instructionsComponents = [];
    Test_Trial_routine_instructionsComponents.push(text);
    Test_Trial_routine_instructionsComponents.push(key_resp_3);
    
    for (const thisComponent of Test_Trial_routine_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Test_Trial_routine_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Test_Trial_routine_instructions' ---
    // get current time
    t = Test_Trial_routine_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 1 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Test_Trial_routine_instructionsComponents)
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

function Test_Trial_routine_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Test_Trial_routine_instructions' ---
    for (const thisComponent of Test_Trial_routine_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Test_Trial_routine_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "Test_Trial_routine_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function test_trial_before_experimentLoopBegin(test_trial_before_experimentLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    test_trial_before_experiment = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Conditions_Spreadsheet_for_test_trials.csv',
      seed: undefined, name: 'test_trial_before_experiment'
    });
    psychoJS.experiment.addLoop(test_trial_before_experiment); // add the loop to the experiment
    currentLoop = test_trial_before_experiment;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTest_trial_before_experiment of test_trial_before_experiment) {
      snapshot = test_trial_before_experiment.getSnapshot();
      test_trial_before_experimentLoopScheduler.add(importConditions(snapshot));
      test_trial_before_experimentLoopScheduler.add(test_trialRoutineBegin(snapshot));
      test_trial_before_experimentLoopScheduler.add(test_trialRoutineEachFrame());
      test_trial_before_experimentLoopScheduler.add(test_trialRoutineEnd(snapshot));
      test_trial_before_experimentLoopScheduler.add(test_trial_before_experimentLoopEndIteration(test_trial_before_experimentLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function test_trial_before_experimentLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(test_trial_before_experiment);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function test_trial_before_experimentLoopEndIteration(scheduler, snapshot) {
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

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'ConditionsSpreadSheet.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(Real_TrialsRoutineBegin(snapshot));
      trialsLoopScheduler.add(Real_TrialsRoutineEachFrame());
      trialsLoopScheduler.add(Real_TrialsRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trialsLoopEndIteration(scheduler, snapshot) {
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

function test_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test_trial' ---
    t = 0;
    test_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('test_trial.started', globalClock.getTime());
    // Run 'Begin Routine' code from test_trial_code
    import * as ast from 'ast';
    fixation_square = new visual.Polygon({"win": psychoJS.window, "edges": 4, "radius": 0.1, "pos": [0, 0], "size": 0.3, "fillColor": [1, 1, 1], "fillColorSpace": "rgb", "ori": 90.0});
    fixation_square.draw();
    psychoJS.window.update();
    core.wait(0.2);
    mouse = new psychoJS.eventManager.Mouse({"win": psychoJS.window});
    mouse.mouseClock = new util.Clock();
    mouse.setPos(0);
    circlepos = [[0, 0.25], [0.1875, 0.1875], [0.25, 0], [0.1875, (- 0.1875)], [0, (- 0.25)], [(- 0.1875), (- 0.1875)], [(- 0.25), 0], [(- 0.1875), 0.1875]];
    triangle_pos_tuple = tuple(ast.literal_eval(triangle_pos));
    if ((pink_circle_pos === "0")) {
        pink_circle_pos_tuple = 0;
    } else {
        pink_circle_pos_tuple = tuple(ast.literal_eval(pink_circle_pos));
        console.log(1);
    }
    if ((blue_circle_pos === "0")) {
        console.log(2);
        blue_circle_pos_tuple = 0;
        console.log(blue_circle_pos);
    } else {
        blue_circle_pos_tuple = tuple(ast.literal_eval(blue_circle_pos));
        console.log(blue_circle_pos_tuple);
    }
    circlepos.remove(triangle_pos_tuple);
    if ((triangle_color === "g")) {
        triangle1 = new visual.Polygon({"win": psychoJS.window, "edges": 3, "pos": triangle_pos_tuple, "size": 0.125, "fillColor": [(- 0.5833), 0.3402, (- 0.7333)], "lineColor": [(- 0.5833), 0.3402, (- 0.7333)], "fillColorSpace": "rgb", "lineColorSpace": "rgb"});
    } else {
        if ((triangle_color === "b")) {
            triangle1 = new visual.Polygon({"win": psychoJS.window, "edges": 3, "pos": triangle_pos_tuple, "size": 0.125, "fillColor": [(- 1.0), 0.0039, 0.0039], "lineColor": [(- 1.0), 0.0039, 0.0039], "fillColorSpace": "rgb", "lineColorSpace": "rgb"});
        } else {
            triangle1 = new visual.Polygon({"win": psychoJS.window, "edges": 3, "pos": triangle_pos_tuple, "size": 0.125, "fillColor": [1.0, (- 1.0), 1.0], "lineColor": [1.0, (- 1.0), 1.0], "fillColorSpace": "rgb", "lineColorSpace": "rgb"});
        }
    }
    triangle1.draw();
    for (var i, _pj_c = 0, _pj_a = circlepos, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if ((pink_circle_pos_tuple === i)) {
            circle = new visual.Circle({"win": psychoJS.window, "edges": "circle", "pos": i, "size": 0.1, "fillColor": [1.0, (- 1.0), 1.0], "fillColorSpace": "rgb"});
        } else {
            if ((blue_circle_pos_tuple === i)) {
                circle = new visual.Circle({"win": psychoJS.window, "edges": "circle", "pos": i, "size": 0.1, "fillColor": [(- 1.0), 0.0039, 0.0039], "fillColorSpace": "rgb"});
            } else {
                circle = new visual.Circle({"win": psychoJS.window, "edges": "circle", "pos": i, "size": 0.1, "fillColor": [(- 0.5833), 0.3402, (- 0.7333)], "fillColorSpace": "rgb"});
            }
        }
        circle.draw();
    }
    psychoJS.window.update();
    while ((triangle1.contains(mouse) === false)) {
        core.wait(0.1);
    }
    continueRoutine = false;
    
    // keep track of which components have finished
    test_trialComponents = [];
    
    for (const thisComponent of test_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function test_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test_trial' ---
    // get current time
    t = test_trialClock.getTime();
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
    for (const thisComponent of test_trialComponents)
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

function test_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test_trial' ---
    for (const thisComponent of test_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test_trial.stopped', globalClock.getTime());
    // the Routine "test_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Actual_Trial_InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Actual_Trial_Instructions' ---
    t = 0;
    Actual_Trial_InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Actual_Trial_Instructions.started', globalClock.getTime());
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    Actual_Trial_InstructionsComponents = [];
    Actual_Trial_InstructionsComponents.push(actual_trial_intructions);
    Actual_Trial_InstructionsComponents.push(key_resp_4);
    
    for (const thisComponent of Actual_Trial_InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Actual_Trial_InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Actual_Trial_Instructions' ---
    // get current time
    t = Actual_Trial_InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *actual_trial_intructions* updates
    if (t >= 0.0 && actual_trial_intructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      actual_trial_intructions.tStart = t;  // (not accounting for frame time here)
      actual_trial_intructions.frameNStart = frameN;  // exact frame index
      
      actual_trial_intructions.setAutoDraw(true);
    }
    
    
    // *key_resp_4* updates
    if (t >= 1 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Actual_Trial_InstructionsComponents)
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

function Actual_Trial_InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Actual_Trial_Instructions' ---
    for (const thisComponent of Actual_Trial_InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Actual_Trial_Instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "Actual_Trial_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Real_TrialsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Real_Trials' ---
    t = 0;
    Real_TrialsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Real_Trials.started', globalClock.getTime());
    // Run 'Begin Routine' code from real_trials_code
     
    // keep track of which components have finished
    Real_TrialsComponents = [];
    
    for (const thisComponent of Real_TrialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Real_TrialsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Real_Trials' ---
    // get current time
    t = Real_TrialsClock.getTime();
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
    for (const thisComponent of Real_TrialsComponents)
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

function Real_TrialsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Real_Trials' ---
    for (const thisComponent of Real_TrialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Real_Trials.stopped', globalClock.getTime());
    // the Routine "Real_Trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function End_RoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'End_Routine' ---
    t = 0;
    End_RoutineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('End_Routine.started', globalClock.getTime());
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    End_RoutineComponents = [];
    End_RoutineComponents.push(End_Text);
    End_RoutineComponents.push(key_resp_2);
    
    for (const thisComponent of End_RoutineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function End_RoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'End_Routine' ---
    // get current time
    t = End_RoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *End_Text* updates
    if (t >= 0.0 && End_Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      End_Text.tStart = t;  // (not accounting for frame time here)
      End_Text.frameNStart = frameN;  // exact frame index
      
      End_Text.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of End_RoutineComponents)
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

function End_RoutineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'End_Routine' ---
    for (const thisComponent of End_RoutineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('End_Routine.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "End_Routine" was not non-slip safe, so reset the non-slip timer
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

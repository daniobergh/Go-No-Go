import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim, Circle
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random

exp_info = {'participant_nr': '', 'age': '21'}
dlg = DlgFromDict(exp_info)

p_name= exp_info['participant_nr']

win = Window(size=(1200, 800), fullscr=False)

mouse = Mouse(visible=False)

clock = Clock()
f_list = f"/Users/danielleobergh/Desktop/Prog4Psych/HF_LF_60.csv"
foods = pd.read_csv(f_list)
hf = foods[foods['fat']==1]
lf = foods[foods['fat']==0]
lf = lf.sample(frac=0.4)
hf = hf.sample(frac=0.4)
trial_foods=pd.concat([lf,lf,lf,hf])
trial_foods = trial_foods.sample(frac=1)
kb=Keyboard()

instructions = TextStim(
    win,
    text="""In this task you will see pictures of food.
         Press the SPACEBAR for every food image UNLESS you see a RED circle.
         Green circle = PRESS SPACE
         Red circle = DO NOT PRESS
         Press SPACE to begin.,""",
         
    height=0.05,
    wrapWidth=1.2
)

instructions.draw()
win.flip()

event.waitKeys(keyList=['space'])


for i in range(0,len(trial_foods)):
    trial=trial_foods.iloc[i]
    print(trial)
    t=TextStim(win,"+")
    t.draw()
    win.flip()
    wait(0.5)
    path = "/Users/danielleobergh/Desktop/Prog4Psych/Food-Choice-Task-main/stimuli" + trial.food
    print(trial.fat)
    if trial.fat==1:
        correct = "nogo"
        go_cue = Circle(
                    win,
                    radius=0.05,
                    fillColor='red',
                    lineColor='red',
                    pos=(0.7, 0.4) 
                ) 
    else: 
        correct = "go"
        go_cue = Circle(
                    win,
                    radius=0.05,
                    fillColor='green',
                    lineColor='green',
                    pos=(0.7, 0.4) 
                )
    im=ImageStim(win, path)
    
    
    t_clock=Clock()
    response = "nongo"
    rt="NA"
    while t_clock.getTime() < .75:
        if correct == "go":
            go_cue.draw()
        else:
            nogo_cue.draw()

win.flip()
        
        keys = kb.getKeys(['space','escape'], waitRelease=False)
        if keys:
            resp = keys[0].name
            rt = keys[0].rt
            if resp == 'escape':
                win.close()
                quit()
            else:
                response = "go"

    win.flip()
    wait(.5)
    trial_foods['response']=response
    trial_foods['rt']= rt

trials.save(f"{p_name}_gonogo.csv")

## tasks
# 1. figure out what is happening in the task & add instructions
# 2. we need to add go-nogo! How would we do that?

    

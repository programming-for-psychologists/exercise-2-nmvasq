import time
import sys
import random
from psychopy import visual,event,core,gui

win = visual.Window([800,600],color="black", units='pix')
fixStim = visual.TextStim(win, text = "+", height=40, color="white",pos=[0,0])
randomNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
corStim = visual.TextStim(win,text="O", height=40, color="green",pos=[0,0])
errStim = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])
res_dict = {0:'f', 1:'l'}

names = open('C:/Users/NMVasquez/Downloads/names.txt', 'r').readlines()
def ran_name():
    global binary
    randomNames = [name.split(' ')[binary] for name in names]
    return randomNames

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()

userVar = {'Name':'Enter your name'}
dlg = gui.DlgFromDict(userVar)

while 'q' not in event.getKeys(keyList = ['q']): #built in a rough escape option . . .
    binary = random.choice([0,1]) 
    nameShown = random.choice(ran_name()).strip()
    randomNameStim.setText(nameShown)
    fixStim.draw()
    win.flip()
    core.wait(.5)
    randomNameStim.draw()
    win.flip()
    timer = core.Clock()
    rec_key = event.waitKeys(maxWait = 1, keyList = ['space'])
    latency = timer.getTime()
    if None != rec_key:
        if 'space' == rec_key[0]:
            if nameShown == userVar['Name']:
                corStim.draw()
            else:
                errStim.draw()
            win.flip()
            core.wait(.5)
    else:
        if nameShown == userVar['Name']:
            errStim.draw()
            win.flip()
            core.wait(.5)

win.close()
sys.exit()
import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('C:/Users/NMVasquez/Downloads/names.txt', 'r').readlines()

def ran_name():
    global binary
    randomNames = [name.split(' ')[binary] for name in names]
    return randomNames

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
fixStim = visual.TextStim(win, text = "+", height=40, color="white",pos=[0,0])
randomNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
while 'q' not in event.getKeys(keyList = ['q']): #built in a rough escape option . . .
    binary = random.choice([0,1])
    nameShown = random.choice(ran_name())
    randomNameStim.setText(nameShown)
    fixStim.draw()
    win.flip()
    core.wait(.5)
    randomNameStim.draw()
    win.flip()
    core.wait(.75)
    if binary == 0:
        if 'f' in event.waitKeys(keyList = ['f']):
            continue
    else:
        if 'l' in event.waitKeys(keyList = ['l']):
            continue

win.close()
sys.exit()
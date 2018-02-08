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

def feedback(con):
    if con in event.waitKeys(keyList = ['f', 'l']):
        corStim.draw()
        win.flip()
        core.wait(.5)
    else:
        errStim.draw()
        win.flip()
        core.wait(.5)

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	


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
        feedback(res_dict[binary])
    else:
        feedback(res_dict[binary])

win.close()
sys.exit()
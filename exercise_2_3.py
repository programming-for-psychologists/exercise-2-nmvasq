import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('C:/Users/NMVasquez/Downloads/names.txt', 'r').readlines()
binary = [0,1]

def ran_name():
    global binary
    randomNames = [name.split(' ')[random.choice(binary)] for name in names]
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
while True:
    nameShown = random.choice(ran_name())
    randomNameStim.setText(nameShown)
    fixStim.draw()
    win.flip()
    core.wait(.5)
    randomNameStim.draw()
    win.flip()
    core.wait(.75)

    if event.getKeys(['q']):
        break

win.close()
sys.exit()
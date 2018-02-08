import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('C:/Users/NMVasquez/Downloads/names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names]

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
fixStim = visual.TextStim(win, text = "+", height=40, color="white",pos=[0,0])
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
while True:
    nameShown = random.choice(lastNames)
    lastNameStim.setText(nameShown)
    fixStim.draw()
    win.flip()
    core.wait(.5)
    lastNameStim.draw()
    win.flip()
    core.wait(.75)

    if event.getKeys(['q']):
        break

win.close()
sys.exit()
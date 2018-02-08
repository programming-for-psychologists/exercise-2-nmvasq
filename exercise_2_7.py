import time
import sys
import random
from psychopy import visual,event,core,gui

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()

names = open('C:/Users/NMVasquez/Downloads/names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

userVar = {'Name':'Enter your name'}
dlg = gui.DlgFromDict(userVar)

if userVar['Name'] in names:
    continue
else:
    popupError("Name does not exist!")

sys.exit()
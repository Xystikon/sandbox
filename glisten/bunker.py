import time
import random

def init():
    global n, s, e, w, currentloc
    
    n=0
    s=0
    w=0
    e=0
    
    currentloc='sleepingbag'

    bunker()
    
def bunker():
    action = input('')
    
    if currentloc == 'sleepingbag':
        n='door'
        w='shelf'
        s='wall'
        e='corner'

        print('sleepingbag')

    elif currentloc == 'door':
        n='outside'
        w='shelf2'
        s='sleepingbag'
        e='wall'

        print('door')

    if action == 'n':
        currentloc = n
    if action == 'w':
        currentloc = w
    if action == 's':
        currentloc = s
    if action == 'e':
        currentloc = e

from ConfigParser import ConfigParser

config = ConfigParser()
config.read('data/configs.ini')
vf = config.get('Watch', 'Vid_Fle')
minDelay = config.getint('Watch', 'Min_Delay')
maxDelay = config.getint('Watch', 'Max_Delay')
Adv = config.getboolean('Watch', 'Advance')
sleeptime = config.getint('Watch', 'Sleep')

import pyscreeze
import pyautogui
import webbrowser
import time
from random import randint
import os
playlists = []
sleeptime = 10

def main():
    with open(vf) as f:
        playlists = f.read().splitlines()
    webbrowser.open("www.swagbucks.com")
    time.sleep(3)
    pyautogui.press('f11')
    pyautogui.hotkey('ctrl','w')
    time.sleep(5)
    for U in playlists:
        tcnt = 0
        done = False
        webbrowser.open(U)
        time.sleep(5)
        while done != True:
            err = pyscreeze.locateOnScreen('data/error.png',grayscale=True)
            kll =pyscreeze.locateOnScreen('data/kill.png',grayscale=True)
            if (err!= None or kll != None):
                print "found error"
                pyautogui.press('f5')
                time.sleep(10)
                err = pyscreeze.locateOnScreen('data/error.png',grayscale=True)
                kll =pyscreeze.locateOnScreen('data/kill.png',grayscale=True)
                if (err!= None or kll != None):
                    print "playlist: " + U + " seems unavalible at this time"
                    done = True
            nne = pyscreeze.locateOnScreen("data/viewall.png",grayscale=True)
            if (nne!= None and done != True):
                print "playlist: " +U+ " seems to have been removed from swagbucks"
                done = True
            dne = pyscreeze.locateOnScreen('data/fullbar.png',grayscale=True)
            if (dne!= None and done != True):
                print "playlist finished"
                done = True
            else:
                time.sleep(sleeptime)
            tks = list(pyscreeze.locateAllOnScreen("data/tick.png"))
            if (len(tks) >tcnt and done != True and Adv):
                print "advancing video"
                tmp = tks[len(tks)-1]
                pyautogui.click(tmp[0]+stp,tmp[1])
                time.sleep(5)
                tcnt = len(list(pyscreeze.locateAllOnScreen("data/tick.png")))


        pyautogui.hotkey('ctrl','w')
        pause = randint(minDelay,maxDelay)
        print "sleep for: " + str(pause) + "seconds"
        time.sleep(pause)



if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
import ctypes
import time
import pyautogui
import win32gui
import pieConfig


mouseButtonRight = 0x02
mouseButtonMiddle = 0x04

pyautogui.PAUSE=.05
pyautogui.FAILSAFE = True

pos = (0,0)
shortDist = 20
longDist = 100
longClick = 900000
maxWaitTime = 30

def test():
    logging.debug("it's alive!")
                
def _click (coordinates):
        logging.debug("clicking")
        if coordinates != 1:
                pyautogui.click(coordinates)
def _go (coordinates):
        logging.debug("moving...")
        pyautogui.moveTo(coordinates)
def _find(icon, iconB=None):
        logging.debug("finding...")
        logging.debug(icon)
        location = pyautogui.locateOnScreen(icon)
        if location == None and iconB != None:
                logging.debug(icon + " not found, trying " + iconB)
                location = _find(iconB)
                return location
        """ what follows is an example of extended functionality added to scroll through a ribbon.
            the name of that software is obfuscated.

        if location == None and pyautogui.locateOnScreen('icons/rightArrow.png') != None or  pyautogui.locateOnScreen('icons/leftArrow.png') != None:
                if pyautogui.locateOnScreen('icons/rightArrow.png') != None:
                        logging.debug("scrolling to the right")
                        pyautogui.mouseDown(pyautogui.center(pyautogui.locateOnScreen('icons/rightArrow.png')))
                        time.sleep(2)
                        pyautogui.mouseUp
                        location = pyautogui.locateOnScreen(icon)
                if pyautogui.locateOnScreen('icons/leftArrow.png') != None and location == None:
                        logging.debug("scrolling to the left")
                        pyautogui.mouseDown(pyautogui.center(pyautogui.locateOnScreen('icons/leftArrow.png')))
                        time.sleep(2)
                        pyautogui.mouseUp
                        location = pyautogui.locateOnScreen(icon)
                if location == None:
                        return 1
        """
        if location == None and iconB == None:
                logging.debug('wating for icon...')
                wait = 0
                while wait < maxWaitTime:
                        wait +=1
                        location = pyautogui.locateOnScreen(icon)
                        if location != None:
                                wait = maxWaitTime
                if wait >= maxWaitTime:
                        return 1
        logging.debug(location)
        location = pyautogui.center(location)
        logging.debug(location)
        return location

def handle_pie():        
        dwell = 0
        Sdwel = 0
        while(1):
                time.sleep(0.01)
                windowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
                #while the right mouse button is held calculate how long
                while ctypes.windll.user32.GetKeyState(mouseButtonRight) > 5:
                        dwell += 1
                        #if the betton was just clicked record the current cursor position
                        if dwell == 1:
                                pos = pyautogui.position()
                if dwell >= 5:
                        logging.debug("dwell = " + str(dwell))
                
                        #calculate movement
                        pos2 = pyautogui.position()
                        deltaV = pos[1] - pos2[1]
                        deltaH = pos[0] -pos2[0]
                        #logging.debug("deltaV: " + str(deltaV) + "\ndeltaH: " + str(deltaH))
                        #right-------------------------------------------
                        if deltaH <= (shortDist * -1) and abs(deltaV)< shortDist:
                                logging.debug("right")
                                pieConfig.right(pos, windowName)
                                
                        #left--------------------------------------------
                        elif deltaH >= shortDist and abs(deltaV)<shortDist:
                                logging.debug("left")
                                pieConfig.left(pos, windowName)
                                
                        #up----------------------------------------------
                        elif abs(deltaH) < shortDist and deltaV >= shortDist:
                                logging.debug("up")
                                pieConfig.up(pos, windowName)
                                
                        #down--------------------------------------------
                        elif abs(deltaH) < shortDist and deltaV <= (shortDist * -1):
                                logging.debug("down")
                                pieConfig.down(pos, windowName)
                                
                        #upper right-------------------------------------
                        elif deltaH <= (shortDist * -1) and deltaV >= shortDist:
                                logging.debug("upper right")
                                pieConfig.up_right(pos, windowName)

                        #upper left--------------------------------------
                        elif deltaH >= shortDist and deltaV >= shortDist:
                                logging.debug("upper left")
                                pieConfig.up_left(pos, windowName)

                        #lower right-------------------------------------
                        elif deltaH <= (shortDist * -1) and deltaV <= (shortDist * -1):
                                logging.debug("lower right")
                                pieConfig.down_right(pos, windowName)

                        #lower left--------------------------------------
                        elif deltaH >= shortDist and deltaV <= (shortDist * -1):
                                logging.debug("lower left")
                                pieConfig.down_left(pos, windowName)
                                

                        #click
                        else:
                                #long click
                                if dwell >= longClick:
                                        logging.debug("long click!")
                                        pieConfig.long_click(pos, windowName)
                                #quick click
                                else:
                                        pieConfig.short_click(pos, windowName)
                        dwell = 0

                        
                else:
                        dwell = 0
        
if __name__ == "__main__":
        handle_pie()

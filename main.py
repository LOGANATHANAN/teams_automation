import time 
from datetime import datetime 
import pyautogui
import pyperclip
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb
lst=[
    ['https://teams.microsoft.com/_?culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school/conversations/General?threadId=19:7aec37e356c64f8385233c8156047bf2@thread.tacv2&ctx=channel','11:08','11:47']
#input lecture stats in form of list ......
# ["Link","start_time","end_time"]
# give time in 24 hrs format...
]
keyboard= Controller()

is_class_started =False
for lecture  in lst:
    global x,y
    while True :
        if is_class_started==False:
            if (datetime.now().hour == int(lecture[1].split(':')[0])and 
                datetime.now().minute >= int(lecture[1].split(':')[1])):
                wb.open(lecture[0])
                is_class_started=True
                print("Opening App...")
                time.sleep(5)
        
                while True:
                    position=pyautogui.locateOnScreen("join.png",confidence=0.70)
                    if position is None:
                        print("waiting to click join..")
                        continue
                    else:
                        x=position[0]
                        y=position[1]
                        break

                pyautogui.moveTo(x+20,y+10,duration=.1)
                pyautogui.click()
                print("Clicking Join..")
                time.sleep(5)

                while True:
                    position=pyautogui.locateOnScreen("join_now.png",confidence=0.55)
                    if position is None:
                        print("waiting to join..")
                        continue
                    else:
                        x=position[0]
                        y=position[1]
                        break

                pyautogui.moveTo(x+20,y+10,duration=.1)
                pyautogui.click()
                #pyautogui.press('right')
                #time.sleep(5)
                #pyautogui.press('enter')
                #time.sleep(5)
                time.sleep(10)
                print("Joined the meet")
                pyautogui.hotkey('ctrl','shift','m')
        
        elif   (datetime.now().hour == int(lecture[2].split(':')[0]) and
                datetime.now().minute == int(lecture[2].split(':')[1])):
                is_class_started=False
                pyautogui.hotkey('ctrl','shift','b')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                #time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                break
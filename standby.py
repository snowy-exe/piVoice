import pyautogui #(To automate mouse and keyboard strokes)
import pyperclip #(To paste received messages)
import keyboard #(For the failsafe)
import random #(For dynamic responses)
import time #(To prevent the script before sending too many messages before rechecking if there is a color change)
import webbrowser #(To open the voice site in case it isn't already open)

ready = 0

#  Checks if the google voice wepbage is open and on the left hand side by checking if the color value where the voice logo should be is correct
while not ready:
    pyautogui.moveTo(125, 155)
    if keyboard.is_pressed('q'):
            exit()
    checkX, checkY = pyautogui.position()
    color = pyautogui.screenshot(region=(checkX, checkY, 1, 1))
    rgb = color.getcolors()
    print(rgb)
    ready = pyautogui.pixelMatchesColor(125, 155, (13, 143, 130), tolerance=10)
    if ready:
        break
    url = 'https://voice.google.com/u/0/messages?itemId=t.%2B12015196184'
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)
    time.sleep(7)


if ready:
    running = 1
    while (running > 0):
        #  Moving to readMessage box to standby for incoming message:
        pyautogui.moveTo(705, 885)
        readX, readY = pyautogui.position()

        #  Detecting the correct grey color of an incoming message (RGB 241, 243, 244)
        #  in order to detect that there was an incoming message
        color = pyautogui.screenshot(region=(readX, readY, 1, 1))
        rgb = color.getcolors()
        messageReceived = pyautogui.pixelMatchesColor(705, 885, (241, 243, 244))
        if messageReceived:

            #  Moving to copy the text now that a color change was detected
            pyautogui.moveTo(710, 885)
            pyautogui.click()
            pyautogui.click()
            #pyautogui.click()
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')


            #  Moving to input copy into input string within python console

            #  Moving to and selecting sendMessage box
            pyautogui.moveTo(800, 1050, duration=0)
            pyautogui.click()

            #  Message: keyDown holds a key down, keyUp lifts off of it
            pyautogui.moveTo(800, 1050, duration=0)
            pyautogui.click()

            receivedMessage = pyperclip.paste()

            #  FIND function -- looks things up on google for you
            if receivedMessage == 'Find':
                pyautogui.typewrite('What do you want me to look up?')
                pyautogui.press('enter')
                time.sleep(10)
                timeout = 0
                while (timeout < 30):
                    if pyautogui.pixelMatchesColor(705, 885, (241, 243, 244)):
                        pyautogui.moveTo(710, 885)
                        pyautogui.click()
                        pyautogui.click()
                        pyautogui.click()
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('c')
                        pyautogui.keyUp('ctrl')
                        url = 'google.com'
                        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)
                        pyautogui.moveTo(450, 630)
                        pyautogui.click()
                        time.sleep(1) # Waiting for google to finish loading
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('v')
                        pyautogui.keyUp('ctrl')
                        pyautogui.press('enter')
                        time.sleep(3) # Wating for the search results to load
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('a')
                        pyautogui.press('c')
                        pyautogui.press('w')
                        pyautogui.moveTo(800, 1050, duration=0)
                        pyautogui.click()
                        pyautogui.press('v')
                        pyautogui.keyUp('ctrl')
                        pyautogui.press('enter')

                    else:
                        timeout += 1
                        print(timeout)
                        time.sleep(1)

            # Courier command. Sends a text message to another anonymously through this number.
            if receivedMessage == 'Courier':
                pyautogui.typewrite('What number do you want to send a message to?')
                pyautogui.press('enter')
                time.sleep(10)
                timeout = 0
                while (timeout < 30):
                    if pyautogui.pixelMatchesColor(705, 885, (241, 243, 244)):
                        pyautogui.moveTo(710, 885)
                        pyautogui.click()
                        pyautogui.click()
                        pyautogui.click()
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('c')
                        pyautogui.keyUp('ctrl')
                        url = 'https://voice.google.com/u/0/messages?itemId=t.%2B12012186244'
                        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)
                        time.sleep(5)
                        pyautogui.moveTo(275, 250)
                        pyautogui.click()
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('v')
                        pyautogui.keyUp('ctrl')
                        pyautogui.press('enter')
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('tab')
                        pyautogui.keyUp('ctrl')
                        pyautogui.moveTo(800, 1050)
                        pyautogui.click()
                        pyautogui.typewrite('What message do you want me to send them?')
                        pyautogui.press('enter')
                        time.sleep(7)
                        timeout = 0
                        while (timeout < 60):
                            if pyautogui.pixelMatchesColor(705, 885, (241, 243, 244)):
                                pyautogui.moveTo(710, 885)
                                pyautogui.click()
                                pyautogui.click()
                                pyautogui.click()
                                pyautogui.keyDown('ctrl')
                                pyautogui.press('c')
                                pyautogui.press('tab')
                                time.sleep(0.5)
                                pyautogui.moveTo(800, 1050)
                                pyautogui.click()
                                pyautogui.press('v')
                                pyautogui.keyUp('ctrl')
                                pyautogui.press('enter')
                                pyautogui.keyDown('ctrl')
                                pyautogui.press('w')
                                pyautogui.keyUp('ctrl')
                                timeout = 60 # better way of breaking the loop in this case, as it escapes both loops and moves back to neutral state

                            else:
                                timeout += 1
                                print(timeout)
                                time.sleep(1)

                    else:
                        timeout += 1
                        print(timeout)
                        time.sleep(1)



            # Sample:
            # if receivedMessage == 'Your command here':
            #     pyautogui.typewrite('Initiative response')
            #     - necessary pyautogui actions, more responses, etc.




            time.sleep(5) # Script waits for 5 seconds for the message to send before looping back to check


        else:
            if keyboard.is_pressed('q'):
                running=0 #(Press 'q' to quit, process finishes-- acts as failsafe)


import pyautogui as pa
import keyboard
from time import sleep
import math
import pyttsx3



def main():
    while True:
        try:
            lang = open('lang.txt','r',encoding='utf-8').read()
            break
        except FileNotFoundError:
            lang = open('lang.txt','w',encoding='utf-8')
            lang.write("en")

    lang = 1 if lang == "en" else 0

    count = 1
    x,y = 0,0
    x2,y2 = 0,0

    try:
        while True:
            if keyboard.is_pressed('z'):
                if count < 2:
                    x,y = pa.position()
                    count += 1
                else:
                    x2,y2 = pa.position()
                    g = str(int(math.sqrt((x2-x)**2 + (y-y2)**2)) * 2)
                    print(g)
                    engine = pyttsx3.init()
                    voices = engine.getProperty('voices')
                    engine.setProperty('voice', voices[lang].id)
                    engine.say(g)
                    engine.runAndWait()
                    count = 1
                sleep(0.25)
    except:
        pass



if __name__ == "__main__":
    main()
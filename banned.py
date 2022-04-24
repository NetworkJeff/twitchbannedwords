import pyautogui
import time

# This program is made by networkJeff and the libray used is called "pyautogui"

print("Welcome to the twitch banned words auto addition for moderators")
print(""" Tutortial Note
#1 Access moderator dashboard and select add banned words
#2 press 1 on the script then press the empty text box""")
Welcome = int(input("to start the auto word ban press 1 or to exit ...press anything else: "))

time.sleep(2)

if Welcome == 1:
    banned_words = ["best followers", "wop", "Timber nigger", "Sand nigger", "Raghead", "Pancake Face", "Mulignon",
                    "Mulignan", "Jewboy", "Hike", "Golliwog", "Dune coon", "darkie", "darkey", "Darky", "Curry-muncher",
                    "Coon-ass", "Coonass", "Coon", "Chinky", "Chink", "Ching Chong", "Camel Jockey", "Cabbage Eater",
                    "Buddhahead", "Beaner", "n!gg1r", "NIGG1R", "NI66ER", "NI66A", "NlGGER", "/\/igger",
                    "N!gger", "N!gga", "N!igga", "Nigga","Nigger", "fag", "faggot", "whore", "rape", "raped", "slut",
                    "simp", "terrorist", "incest", "virgin", "Anal", "Ballsack", "Blowjob", "Bollock", "Bollock",
                    "Boner", "Breast", "Buttplug", "Clitoris", "Cock", "Cum", "Cunt", "Dildo", "Felching", "Jizz",
                    "Knob", "Knobend", "Knobhead", "Penis", "Pussy", "Sex", "Spunk", "Tit", "Wank", "Wanker", "Cracker",
                    "Dyke", "Eskimo", "Fudgepacker", "Golliwog", "Gook", "Hobo", "Homo", "Hypsy", "Jigaboo", "Midget",
                    "thot", "lsis", "isis", "suicide", "Terrorist","fudgepacker", "glliwog", "gook", "hypsy", "jigaboo",
                    "retard", "tosser", "wigger", "knob jockey"]
    for i in range(0, len(banned_words)):
        pyautogui.write(banned_words[i])
        pyautogui.press("enter")
        time.sleep(2)
elif Welcome != 1:
    print("Exiting program , goodbye")
    exit()


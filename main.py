
import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set the engine properties
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 1)  # Volume 0-1


# Say the text
while True :
    print("enter your text")
    x= input()
    if x == "e":
        engine.say("Have a good day")
        engine.runAndWait()
        break

    else:
        engine.say(x)
        engine.runAndWait()







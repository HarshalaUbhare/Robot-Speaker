import os
import pyttsx3

if __name__ == '__main__':
    print("Welcome to RobotSpeaker 1.1 Created By Harshala Ubhare on 01-01-2024")

    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            engine.say("Bye bye friends")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()




'''import os
if __name__=='__main__':
    print("welcome to RobotSpeaker 1.1 Created By Harshala Ubhare on 01-01-2024")
    while True:
        x= input("Enter what you want me to speak: ")
        if x=="q":
            os.system("say 'Bye bye friends'")
            break
        command= f"say {x}"
        os.system(command)'''
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
botName = "Jarvis: "
fileName = "temporary.txt"
verifyResponse=0

def listenInput():
     r = sr.Recognizer()
     with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        saveFile = r.recognize_google(audio)
        return saveFile


def talk():
        
    userInput = listenInput()
    with open(fileName, "a") as f:
        f.write("\n"+userInput+":")
    return userInput

def main():
    print(botName+"Write something for me. Also, u can use /commands\n")
    engine.say("Write or say something for me. Also, u can use /commands")
    engine.runAndWait()

def findKnowledge(filename,string):
    with open(filename, 'r') as file:
        for line in file:
            colon_index = line.find(string)
            # procurando o índice do primeiro caractere ":"
            if colon_index != -1:
                colon_indexTwo = line.find(':')
                return line[colon_indexTwo+1:].strip()
            
        print(botName+ "Idk how to asnwer this")
        engine.say("Idk how to asnwer this")
        engine.runAndWait()

def newKnowledge():
    loop=1
    while loop==1:
        
        print(botName+"Sorry i dont know how to answer that, would you like to teach me? Yes | No")
        engine.say("Sorry i dont know how to answer that, would you like to teach me?  write Yes or No")
        engine.runAndWait()
        userResponse = input()
        
        if userResponse == "yes" or userResponse == "Yes":
            print(botName+"How i need to answer that?")
            engine.say("How i need to answer that?")
            engine.runAndWait()
            userResponse = input()
            with open(fileName, "a") as f:
                f.write(userResponse+"\n")
            loop=0
            
            
        elif userResponse == "no" or userResponse == "No":
            print(botName+"Ok, i will not learn that.")
            engine.say("Ok, i will not learn that.")
            engine.runAndWait()
            loop=0
        else:
            print(botName+"Sorry i didnt understand")
            engine.say("Sorry i didnt understand")
            engine.runAndWait()
            loop=1
        
    
if __name__ == "__main__":
    while(True):
        main()
        userInput = talk()
        botResponse = findKnowledge(fileName, userInput)
        if botResponse != "":
          print(botName+botResponse)
          engine.say(botResponse)
          engine.runAndWait()
        else:
            newKnowledge()

import pyttsx3

text_speech = pyttsx3.init()
text_speech.setProperty('rate', 150)

while True:
    answer = input("What do you want to convert to speech?")

    if answer.lower() == '':
        break  # Exit the loop and end the program

    text_speech.say(answer)
    text_speech.runAndWait()

import speech_recognition as Inexa

while True:
    print ('Press v & Speak:')
    read= input()
    if(read=='v'):
        AudioIn = Inexa.Recognizer()
        with Inexa.Microphone() as source:
            print("Speak:")
            audio = AudioIn.listen(source)

    command=AudioIn.recognize_google(audio)
    print("You said " + command )
    
    if 'how' in command:
        print("I am fine. Thank you!")
    if 'name' in command:
        print("I am Inexa from TechClub")
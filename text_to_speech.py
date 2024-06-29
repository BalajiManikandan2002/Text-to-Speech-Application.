import pyttsx3 as p

def textToSpeech():

    text_speech = p.init()

    var = str(input("Enter "))

    # fvar = open('news.txt' , 'r')
    # var = fvar.read()
    # fvar.close()

    voices = text_speech.getProperty('voices')
    print("\n ========================================== \n")
    for x in voices:
        print(x.id,x.name,x.languages)
    print("\n ========================================== \n")

    """SPEAKING RATE"""
    # getting details of current speaking rate
    rate = text_speech.getProperty('rate')   
    print (rate)
    text_speech.setProperty('rate', 150)

    """VOLUME"""
    #getting to know current volume level (min=0 and max=1)
    volume = text_speech.getProperty('volume')
    #printing current volume level
    print (volume)
    text_speech.setProperty('volume',2.0)

    """VOICE"""
    #getting details of current voice
    voices = text_speech.getProperty('voices')
    print(voices)
    text_speech.setProperty('voice', voices[1].id)


    # Speaking the scentence.
    text_speech.say(var)

    text_speech.save_to_file(var, 'test2.mp3')
    print(" Saaved the file ")

    text_speech.runAndWait()
    text_speech.stop()



textToSpeech()

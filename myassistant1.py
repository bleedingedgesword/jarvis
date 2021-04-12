import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Come on come on, turn the radio on, It's Friday night and I won't be long Gotta do my hair, put my make up on It's Friday night and I won't be long 'Til I hit the dance floor, Hit the dance floor I got all I need, No I ain't got cash, I ain't got cash But I got you baby, Baby I don't need dollar bills to have fun tonight (I love cheap thrills) Baby I don't need dollar bills to have fun tonight (I love cheap thrills) But I don't need no money, , As long as I can feel the beat, , I don't need no money, , As long as I keep dancing ") 
   
     
     
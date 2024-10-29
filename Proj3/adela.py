import speech_recognition as sr 
import pyttsx3 as tt
import pywhatkit as pwk
import re

nombre = "Adela"
receptor = sr.Recognizer()
motor = tt.init()
voces = motor.getProperty('voices')
motor.setProperty('voice', voces[81].id)

def displayLanguage(str_regex='es.*'):
    for i, v in enumerate(voces):
        if len(re.findall('es.*', v.languages[0])) > 0: 
            print(f"{i} : {v.name}, {v.gender}, {v.languages}")


def hablar(text):
    motor.say(text)
    motor.runAndWait()
def escuchar():
    try: 
        with sr.Microphone() as fuente:
            print("Adela está escuchando...")
            receptor.adjust_for_ambient_noise(fuente, duration=0.5)
            pc = receptor.listen(fuente)
            rec = receptor.recognize_google(pc, language="es")
            rec = rec.lower()
            if nombre in rec:
                #Por qué se hace esto
                rec = rec.replace(nombre, '')
            print(f"Texto capturado: {rec}")
        
        return rec
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print(f"No se pudo reconocer el audio")
    return None
def run_adela():
    while True:
        rec = escuchar()
        if "reproduce en youtube" or 'pon en youtube' or 'busca en youtube' in rec:
            line = rec.split('youtube')
            music = line[1]
            print(f"Reproduciendo {music}")
            hablar(f"Reproduciendo {music}")
            pwk.playonyt(music)




if __name__ == '__main__':
    run_adela()



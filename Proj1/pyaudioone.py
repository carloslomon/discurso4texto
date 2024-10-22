import speech_recognition as sr

grdr = sr.Recognizer()

def grabar_texto():
    """Función para grabar texto mediante micrófono."""
    try:
        with sr.Microphone() as fuente:
            grdr.adjust_for_ambient_noise(fuente, duration=0.2)
            print("Escuchando...")
            audio = grdr.listen(fuente)

            # Convertir el audio en texto
            txt = grdr.recognize_google(audio, language='es-ES')
            print(f"Texto capturado: {txt}")
            return txt

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print(f"No se pudo reconocer el audio")
    return None

def texto_salida(texto):
    """Función para escribir el texto en un archivo."""
    if texto:  # Solo escribir si hay texto válido
        with open("salida.txt", 'a') as f:
            f.write(texto + "\n")
        print(f"Texto guardado: {texto}")
    else:
        print("No hay texto para guardar.")

# Bucle principal
while True:
    texto = grabar_texto()  # Capturar el texto
    texto_salida(texto)      # Guardar el texto en el archivo

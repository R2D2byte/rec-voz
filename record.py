import sounddevice as sd
import wavio
import os 
import re


def record_voice():
    record_dir = 'records'
    if not os.path.exists(record_dir):
        os.makedirs(record_dir)
        print(f"Carpeta '{record_dir}' creada con éxito.")

    nombres = [nombres for nombres in os.listdir(record_dir) if os.path.isfile(os.path.join(record_dir, nombres))]
    nombres = [re.sub(r'\d+-|\.wav$', '', nombres) for nombres in nombres]
    nombres = list(set(nombres))
    print(f"\n Hello, let's record your voice, do I know you? Pls write the number\n ")
    for i,nombre in enumerate(nombres): 
        print(f"\t {i} - {nombre.capitalize()}")

    name = input(f"\n Can't u see ur name? just write it ... ")

    try:
        name = nombres[int(name)]
    except ValueError:
        pass
    except IndexError:
        print('\n Error')
        return
    
    files_n = len(os.listdir(record_dir))
    file_name = f"records/{files_n}-{name.lower()}.wav"
    # Duración de la grabación en segundos
    seconds = 5
    # Frecuencia de muestreo en Hz
    frecuencia_muestreo = 44100
    # Grabar audio y guardarlo en archivo WAV
    print(f'\n{name} Speak for 5 seconds\n')
    # Captura de audio
    audio = sd.rec(int(seconds * frecuencia_muestreo), samplerate=frecuencia_muestreo, channels=1, dtype='int16')
    sd.wait()
    # Guardar en archivo WAV
    wavio.write(file_name, audio, frecuencia_muestreo, sampwidth=3)
    print(f"Audio recorded and saved in {file_name} \n")

record_voice()
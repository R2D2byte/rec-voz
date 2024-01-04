from recordFromPc import grabar_audio
import os 
from utilities import getAllRecordNamesCleaned

def record_voice():
    record_dir = 'records'
    nombres = getAllRecordNamesCleaned(record_dir=record_dir)
    print(f"\nHello, let's record your voice, do I know you? Pls write the number\n ")
    for i,nombre in enumerate(nombres): 
        print(f"\t {i} - {nombre.capitalize()}")
    name = input(f"\nCan't u see ur name? just write it ... ")
    try:
        name = nombres[int(name)]
    except ValueError:
        pass
    except IndexError:
        print('\n Error')
        return

    file_name = f"records/{len(os.listdir(record_dir))}-{name.lower()}.wav"
    print(f'\n{name.capitalize()} Speak for 5 seconds')
    print(f'Please Read de folowing message ... \n')
    grabar_audio(file_name,5)
    print(f"Audio recorded and saved in {file_name} \n")
    return file_name
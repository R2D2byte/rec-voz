import pyaudio
import wave
import os 
import re

def grabar_audio(file_name, duration, sample_rate=44100, channels=1, format=pyaudio.paInt16):
    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)

    print("Grabando...")
    frames = []
    for i in range(int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    print("Terminado de grabar.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

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
    # Grabar audio y guardarlo en archivo WAV
    print(f'\n{name} Speak for 5 seconds\n')
    grabar_audio(file_name,seconds)
    print(f"Audio recorded and saved in {file_name} \n")

record_voice()
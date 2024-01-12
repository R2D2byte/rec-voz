import pyaudio
from text import randomText
import random
import wave

def grabar_audio(file_name, duration, sample_rate=44100, channels=1, format=pyaudio.paInt16):
    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)

    print("Recording... \n ")
    print(f"\t La única manera de hacer un gran trabajo es amar lo que haces. \n")
    frames = []
    for i in range(int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    print("Finish. \n")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
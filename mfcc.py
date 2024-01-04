import librosa 
import numpy as np

# Cargar archivo de audio
audio_path = "arturo.m4a"
audio, sr = librosa.load(audio_path, sr=None)

# Calcular MFCC
mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

print(mfccs)
print(mfccs.shape)
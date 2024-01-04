import librosa
import os
import numpy as np

##--Creamos una funcion para extraer las mediciones del audio.
def extract_features(file_name): 
    np.set_printoptions(suppress=True)
    # la serie de tiempo esta almacenada en [X]

    X, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 

    # genera Mel-frequency cepstral coefficients (MFCCs) de la serie de tiempo
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)

    # # Genera una transformada de Fourier a corto plazo (STFT) para usar en chroma_stft

    stft = np.abs(librosa.stft(X))

    # # Calcula un cromagrama a partir de una forma de onda o espectrograma de potencia.

    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)

    # # calcula un espectograma de mel-scaled 
    mel = np.mean(librosa.feature.melspectrogram(y=X, sr = sample_rate).T)

    # # Calcula el contraste espectral

    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)

    # # Calcula las características del centroide tonal (tonnetz)

    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X),sr=sample_rate).T,axis=0)
 
    # Pedimos que nos devuelva todos los indicadores mas el target
    return mfccs, chroma, mel, contrast , tonnetz
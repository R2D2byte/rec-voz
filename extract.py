import librosa
import os
import numpy as np

##--Creamos una funcion para extraer las mediciones del audio.
def extract_features(files): 
    np.set_printoptions(suppress=True)
    # Establece el nombre de la ruta a donde están los archivos de audio en mi computadora

    file_name = os.path.join(os.path.abspath(data_dir)+'//audios_enteros//'+str(files.id))

    # Carga el archivo de audio como una serie de tiempo de coma flotante y asigna la frecuencia de muestreo predeterminada
    # Sample rate is set to 22050 by default
    # la serie de tiempo esta almacenada en [X]
    X, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 

    # genera Mel-frequency cepstral coefficients (MFCCs) de la serie de tiempo
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)

    # Genera una transformada de Fourier a corto plazo (STFT) para usar en chroma_stft

    stft = np.abs(librosa.stft(X))

    # Calcula un cromagrama a partir de una forma de onda o espectrograma de potencia.

    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)

    # calcula un espectograma de mel-scaled 

    mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)

    # Calcula el contraste espectral

    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)

    # Calcula las características del centroide tonal (tonnetz)

    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X),sr=sample_rate).T,axis=0)

    # Agregamos también las clases de cada archivo como una etiqueta al final

    label = files.persona

    # Pedimos que nos devuelva todos los indicadores mas el target
    return mfccs, chroma, mel, contrast, tonnetz,label
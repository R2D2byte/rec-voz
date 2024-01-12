import joblib
from extract import extract_features
from buildDataframe import buildDataframe
import numpy as np
from utilities import getAllRecordNames
from recordFromPc import grabar_audio
import os


def record_voice():

    file_name = f"temp/{len(getAllRecordNames(record_dir='temp'))+1}.wav"
    print(f'Speak for 5 seconds')
    print(f'Please Read de folowing message ... \n')
    grabar_audio(file_name,5)
    print(f"Audio recorded and saved in {file_name} \n")
    return file_name


loaded_model = joblib.load('modelo_knn.joblib')
scaler = joblib.load('scaler.joblib')
modelo_pca = joblib.load('modelo_pca.pkl')

file_name = record_voice()
#OBTENEMOS LAS CARACTERISTICAS 
mfccs, chroma, mel, contrast, tonnetz = extract_features(file_name=file_name)
X_new = buildDataframe(mfccs,chroma,mel,contrast,tonnetz,False)

X_new_normalized = scaler.transform([X_new])

x_pca = modelo_pca.transform(X_new_normalized)

predictions = loaded_model.predict(x_pca)

# Imprimir las predicciones
print("Predicciones:", predictions)



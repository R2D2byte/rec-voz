import pandas as pd 
from extract import extract_features
from buildDataframe import buildDataframe

nombre_archivo = 'dataset.csv'
#INICIAMOS LA GRABACION

#OBTENEMOS LAS CARACTERISTICAS 
for i in range(6):
    mfccs, chroma, mel, contrast, tonnetz = extract_features(file_name=f'records/{i}-david.wav')
    last_df = pd.read_csv(nombre_archivo, delimiter=',') 
    new_row = buildDataframe(mfccs,chroma,mel,contrast,tonnetz,'david')
    nuevo_df = pd.DataFrame([new_row], columns=last_df.columns)
    df = pd.concat([last_df, nuevo_df], ignore_index=True)
    df.to_csv(nombre_archivo, index=False)
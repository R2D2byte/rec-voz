import pandas as pd 
from extract import extract_features
from record import record_voice
from buildDataframe import buildDataframe

if __name__ == "__main__":
    nombre_archivo = 'dataset.csv'
    #INICIAMOS LA GRABACION
    file_name, label = record_voice()
    #OBTENEMOS LAS CARACTERISTICAS 
    mfccs, chroma, mel, contrast, tonnetz = extract_features(file_name=file_name)
    last_df = pd.read_csv(nombre_archivo, delimiter=',') 
    new_row = buildDataframe(mfccs,chroma,mel,contrast,tonnetz,label)
    nuevo_df = pd.DataFrame([new_row], columns=last_df.columns)
    df = pd.concat([last_df, nuevo_df], ignore_index=True)
    df.to_csv(nombre_archivo, index=False)
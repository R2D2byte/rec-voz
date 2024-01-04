import pandas as pd 
from extract import extract_features
from record import record_voice

if __name__ == "__main__":

    #INICIAMOS LA GRABACION
    file_name = record_voice()
    #OBTENEMOS LAS CARACTERISTICAS 
    mfccs, chroma, mel, contrast, tonnetz = extract_features(file_name=file_name)

    print(mfccs, chroma, mel, contrast, tonnetz )
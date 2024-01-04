import pandas as pd 
import numpy as np

def buildDataframe(mfccs,chroma,mel,contrast,tonnetz,label):
    dataset = []

    for value in mfccs:
        dataset.append(value)

    for value in chroma:
        dataset.append(value)

    for value in contrast:
        dataset.append(value)

    for value in tonnetz:
        dataset.append(value)

    dataset.append(mel)
    dataset.append(label)
    return dataset
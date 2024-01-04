import os
import re

def getAllRecordNames(record_dir = 'records'):
    return [nombres for nombres in os.listdir(record_dir) if os.path.isfile(os.path.join(record_dir, nombres))]

def getRecordNameCleaned(name):
    return re.sub(r'\d+-|\.wav$', '', name)

def getAllRecordNamesCleaned(record_dir = 'records'):
    nombres = [nombres for nombres in os.listdir(record_dir) if os.path.isfile(os.path.join(record_dir, nombres))]
    nombres = [re.sub(r'\d+-|\.wav$', '', nombres) for nombres in nombres]
    return list(set(nombres))
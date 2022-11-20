import pandas as pd
import requests

def load_sentences(path):
    sd = pd.read_excel(path)
    return sd

def load_sentences_audio(path):
    sd = pd.read_excel(path)
    return sd

sd_df = load_sentences('DATA/CNY_SEN.xlsx')
sa_df = load_sentences_audio('DATA/sentences_with_audio.xlsx')

oko=5

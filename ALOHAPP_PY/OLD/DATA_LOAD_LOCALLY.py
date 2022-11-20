import pandas as pd

def load_words(path):
    words = pd.read_excel(path)
    return words

def save_words(df,name):
    df.to_excel(name)

def load_GFE():
    Ger = load_words('../../DATA/WORDS/5000WORDSGERMAN.xlsx')
    Fra = load_words('../../DATA/WORDS/5000WORDSFRENCH.xlsx')
    Esp = load_words('../../DATA/WORDS/5000WORDSSPANISH.xlsx')
    return Ger, Fra, Esp
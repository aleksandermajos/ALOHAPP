import pandas as pd
import requests

def load_words(path):
    words = pd.read_excel(path)
    return words

def make_order(words):
    words_df = words.WORD
    word_df = words_df.iloc[::2]
    word_df = word_df.reset_index(drop=True)
    pinyin_df = words_df.iloc[1::2]
    pinyin_df = pinyin_df.reset_index(drop=True)
    meaning_df = words.PINYIN
    meaning_df = meaning_df.iloc[::2]
    meaning_df = meaning_df.reset_index(drop=True)

    column_names = ["WORD", "PINYIN", "MEANING"]
    words = pd.DataFrame(columns=column_names)

    words['WORD'] = word_df
    words['PINYIN'] = pinyin_df
    words['MEANING'] = meaning_df
    return words



hsk1 = load_words('DATA/CHINESE_HSK1.xlsx')
hsk2 = load_words('DATA/CHINESE_HSK2.xlsx')
hsk3 = load_words('DATA/CHINESE_HSK3.xlsx')
hsk4 = load_words('DATA/CHINESE_HSK4.xlsx')
hsk5 = load_words('DATA/CHINESE_HSK5.xlsx')
hsk6 = load_words('DATA/CHINESE_HSK6.xlsx')
hsk7_8_9 = load_words('DATA/CHINESE_HSK7_8_9.xlsx')

hsk1 = make_order(hsk1)
hsk2 = make_order(hsk2)
hsk3 = make_order(hsk3)
hsk4 = make_order(hsk4)
hsk5 = make_order(hsk5)
hsk6 = make_order(hsk6)
hsk7_8_9 = make_order(hsk7_8_9)

hsk = pd.concat([hsk1, hsk2, hsk3,hsk4,hsk5,hsk6,hsk7_8_9], ignore_index=True, axis=0)
hsk.to_excel('DATA/CHINESE_HSK.xlsx')

oko=5
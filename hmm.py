import os
import pandas as pd

dataFolder = r'C:\Users\jylkka_a\Downloads\datasets\UD_English'

dataPath = os.path.join(dataFolder, 'en-ud-train.conllu')
# x = open(dataPath).readlines()

df = pd.read_csv(dataPath, sep='\t', header=None, index_col=False
                 ,names=['rownum', 'word', 'word_lc', 'POS']
                 ,usecols=['rownum', 'word', 'word_lc', 'POS']
                 )



#df.drop(df[:,5:], axis=1, inplace=True)

bigramcounts = {}

words = df.word.values

for i, word in enumerate(words[:200]):
    if i + 1 == len(words):
        break
    bigram = (word, words[i+1])
    if bigram in bigramcounts.keys():
        bigramcounts[bigram] += 1
    else:
        bigramcounts[bigram] = 1




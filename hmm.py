import os
import pandas as pd
from collections import defaultdict

# implementation help from https://github.com/usami/hmmner/blob/master/hmm_ne_tagger.py

# x = open(dataPath).readlines()

# df = pd.read_csv(dataPath, sep='\t', header=None, index_col=False
#                  ,names=['rownum', 'word', 'word_lc', 'POS']
#                  ,usecols=['rownum', 'word', 'word_lc', 'POS']
#                  )


def getData(file='en-ud-train.conllu'):
    dataFolder = r'C:\Users\jylkka_a\Downloads\datasets\UD_English'
    dataPath = os.path.join(dataFolder, file)
    data = open(dataPath, 'r').read()
    print 'done reading file'
    sentences = data.split('\n\n')
    sentences = [sentence.split('\n') for sentence in sentences]
    print 'done'
    result = []
    for sentence in sentences:
        sentence_parsed = []
        for line in sentence:
            try:
                line_split = line.split('\t')
                sentence_parsed.append((line_split[2], line_split[3]))
            except:
                pass
        result.append(sentence_parsed)
    print 'DONE'
    return result

def getCounts(file='train.counts'):
    emission_counts = defaultdict(int)
    ngram_counts = [defaultdict(int) for _ in range(3)]

    dataFolder = r'C:\Users\jylkka_a\Downloads\datasets\UD_English'
    dataPath = os.path.join(dataFolder, file)
    lines = open(dataPath, 'r').readlines()
    for line in lines:
        line_split = line.split()
        try:
            count, type, info = int(line_split[0]), line_split[1], line_split[2:]
            if type == 'WORDTAG':
                emission_counts[tuple(info)] = count
            else:
                ngram_counts[len(info) - 1][tuple(info)] = count
        except:
            pass

    return emission_counts, ngram_counts

def calc_parameters(emission_counts, ngram_counts):
    emission_probabilities = defaultdict(float)
    for tag, word in emission_counts.keys():
        try:
            # e(word | tag) = count(tag, word) / count(tag)
            emission_probabilities[(tag, word)] = float(emission_counts[(tag, word)]) / ngram_counts[0][tuple([tag])]
        except Exception as e:
            print tag, word, e

    transition_probabilities = defaultdict(float)
    for tag1, tag2, tag3 in ngram_counts[2].keys():
        try:
            # t(tag3 | tag1, tag2) = count(tag1, tag2, tag3) / count(tag1, tag2)
            transition_probabilities[(tag1, tag2, tag3)] = \
                float(ngram_counts[2][(tag1, tag2, tag3)]) / ngram_counts[1][(tag1, tag2)]
        except Exception as e:
            print e

    return emission_probabilities, transition_probabilities

def predict_tags(input, emission_probabilities, transition_probabilities,
                 emission_counts, ngram_counts,tags):
    tags = ['*'] + tags

    for sentence in input:
        # implement Viterbi algorithm

        sentence_words = [word_tag[0] for word_tag in sentence]
        sentence_tags = [word_tag[1] for word_tag in sentence]
        m = len(sentence)
        sentence =

        # pi[j,s,s'] stores maximum probability tag sequence ending with tags s, s' at position j
        pi = defaultdict(float)
        backpointers = {}

        for tag1 in tags:
            for tag2 in tags:
                pi[(0, tag1, tag2)] = 0
        pi[(0, '*', '*')] = 1

        for k in range(len(sentence) - 1):
            for u in tags:
                for v in tags[1:]:
                    likelihood = lambda w: \
                        pi[(k-1, w, u)] * transition_probabilities[(v,w,u)] * emission_probabilities[(sentence[k], v)]
                    # most likely tag
                    best_tag = max(tags, key=likelihood)
                    best_prob = max([likelihood(tag) for tag in tags])

                    pi[(k, u, v)] = best_prob
                    backpointers[(k, u, v)] = best_tag

        output_tags = ['*'] + [m * None]
        # start from the end of the sentence
        import itertools
        bigrams = itertools.permutations(tags, 2)
        end_tag_likelihood = lambda tag: pi[(m, tag[0], tag[1])] * transition_probabilities[('STOP', tag[0], tag[1])]
        best_end_bigram = max(bigrams, key=end_tag_likelihood)
        print best_end_bigram

        output_tags[m-1], output_tags[m] = best_end_bigram

        # go backwards from the end tags we just set
        for k in range(m-2, 0, -1):
            output_tags[k] = backpointers[(k+2, output_tags[k+1], output_tags[k+2])]

        print output_tags

        for thing in zip(sentence, )




    pass






testData = getData('en-ud-train.conllu')
emission_counts, ngram_counts = getCounts()
emission_probabilites, transition_probabilities = calc_parameters(emission_counts, ngram_counts)
tags = [one_gram[0] for one_gram in ngram_counts[0]]




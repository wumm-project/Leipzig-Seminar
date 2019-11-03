#!/usr/bin/python3
# -*- coding: utf-8 -*-
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from data.trizprinciples import methods

def download():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('wordnet_ic')

def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n' 
    if tag.startswith('V'):
        return 'v' 
    if tag.startswith('J'):
        return 'a' 
    if tag.startswith('R'):
        return 'r' 
    return None
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
 
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
 

#sentence similarity using Wordnet
def sentence_similarity(sentence1, sentence2):
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    score, count = 0.0, 0
    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        scores = []
        for ss in synsets2:
            simscore = synset.path_similarity(ss)
            if simscore == None:
                scores.append(0)
            else:
                scores.append(simscore)
        best_score = max(scores)
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1
    # Average the values
    score /= count
    return score

def symmetric_sentence_similarity(sentence1, sentence2):
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2

if __name__ == '__main__':
    #download()
    abstract = """Known conventional cigarette packs, especially those with a hinge-lid box (10), an inner blank (29) made of tin-foil and possibly an outer wrapping made of plastics foil, are not suitable for disposing of smoked cigarettes (waste-cigarettes 48). It is felt to be undesirable that smoked cigarettes be thrown away individually. This is especially true for "artificial cigarettes" which have recently appeared on the market. In order to achieve an improved waste-disposal, the present cigarette pack, especially as regards its embodiment with a hinge-lid box (10), is provided with a waste compartment (47) for holding waste-cigarettes (48). Park of the inner blank (28), namely its rear-wall (30), forms a partition between the waste compartment (47) and a cigarette compartment (46). Smoked cigarettes are reinserted into the pack through an insert-opening (54)."""
    
    res = []
    for method in methods:
        res.append( symmetric_sentence_similarity(abstract, method) )
    print(res)
        

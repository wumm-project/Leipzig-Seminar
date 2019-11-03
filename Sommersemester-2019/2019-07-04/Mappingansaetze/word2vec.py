#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import gensim.models
from data.trizprinciples import methoden, methods

def trainModel():
    sentences = []
    for methode in methoden:
        sentences.append(methode.split(' '))
    model = gensim.models.Word2Vec(sentences, min_count=1)
    model.wv.save('./models/model.bin')

def w2vCompare(s1, s2, wordmodel):
    s1wordsset = set(s1.split())
    s2wordsset = set(s2.split())
    for word in s1wordsset.copy():
        if (word not in wordmodel.vocab):
            try:
                s1wordsset.remove(word)
            except KeyError:
                pass
    for word in s2wordsset.copy():
        if (word not in wordmodel.vocab):
            try:
                s2wordsset.remove(word)
            except KeyError:
                pass
    return wordmodel.n_similarity(list(s1wordsset), list(s2wordsset))

def test1():
    # deutsch (eigenes model)
    abstract = """Zigaretten-Gruppen (11) sind innerhalb einer als Klapp­schachtel ausgebildeten Zigaretten-Packung durch einen Innen­zuschnitt (16) aus Stanniol oder dgl. umhüllt. Für die erleich­terte Entnahme von Zigaretten (12) ist der Innenzuschnitt (16) mit einem infolge von Stanzlinien (27) abziehbaren Lappen (26) - Flap - versehen. Zur weiteren Erleichterung der Entnahme von Zigaretten (12) ist der Innenzuschnitt (16) durch Seitenstanzlinien (31, 32) mit einem Aushebestreifen (30) versehen, der das Anheben einer Anzahl von Zigaretten (12) zur Entnahme derselben ermög­licht. Der Aushebestreifen (30) erstreckt sich mit einer Griff­lasche (34) in den Bereich des Lappens (26). Wird dieser abge­zogen, kommt die Grifflasche (34) frei, derart, daß sie aus der geöffneten Zigaretten-Packung herausragt und von Hand erfaßt werden kann. Der Aushebestreifen (30) ist dauerhaft mit dem Innenzuschnitt (16) verbunden als Teil desselben."""
    wordmodelfile = "./models/model.bin"
    wordmodel = gensim.models.KeyedVectors.load(wordmodelfile, mmap='r')
    res = []
    for method in methoden:
        res.append(w2vCompare(abstract, method, wordmodel))
    print("\ngerman, own model")
    print(res)

def test2():
        # englisch (gnews model)
    abstract = """Known conventional cigarette packs, especially those with a hinge-lid box (10), an inner blank (29) made of tin-foil and possibly an outer wrapping made of plastics foil, are not suitable for disposing of smoked cigarettes (waste-cigarettes 48). It is felt to be undesirable that smoked cigarettes be thrown away individually. This is especially true for "artificial cigarettes" which have recently appeared on the market. In order to achieve an improved waste-disposal, the present cigarette pack, especially as regards its embodiment with a hinge-lid box (10), is provided with a waste compartment (47) for holding waste-cigarettes (48). Park of the inner blank (28), namely its rear-wall (30), forms a partition between the waste compartment (47) and a cigarette compartment (46). Smoked cigarettes are reinserted into the pack through an insert-opening (54)."""
    wordmodelfile = "./models/GoogleNews-vectors-negative300.bin" #"./models/GoogleNews-vectors-negative300.bin.gz"
    wordmodel = gensim.models.KeyedVectors.load_word2vec_format(wordmodelfile, binary=True)
    res = []
    for method in methods:
        res.append(w2vCompare(abstract, method, wordmodel))
    print("\nenglish, gnews model")
    print(res)

if __name__ == '__main__':
    test1()
    #test2()
    


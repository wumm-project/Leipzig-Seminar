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

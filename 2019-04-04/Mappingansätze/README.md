# patenttextmatch

Applying text similarity algorythms on patenttexts and the 40 triz priziples to classify potential innovation methods.

## Getting Started

```sh
make install
```

## Load models

```sh
make load
```

## tfidf

[0., 0.01124889 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.01118105 0., 0., 0., 0.00913807 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.00997566 0., 0., 0., 0., 0., 0.]

## w2v

[0.58766514, 0.66835225, 0.71240354, 0.6649222, 0.64329594, 0.66402805, 0.78082335, 0.693567, 0.77501005, 0.7846895, 0.62681985, 0.65579087, 0.64211774, 0.58612865, 0.7568965, 0.74246585, 0.710278, 0.5357624, 0.69967353, 0.6756405, 0.55700743, 0.7103742, 0.60688776, 0.65232396, 0.6610202, 0.6873301, 0.6839913, 0.6221209, 0.69601005, 0.6572794, 0.7112712, 0.55912167, 0.6386556, 0.75620085, 0.539741, 0.51225054, 0.65765435, 0.51215994, 0.607432, 0.41427097]

### Notes

2: zigarettenpackung
27: teebeutel windel etc tetrapack, wegwerf zigaretten anzünder (feuer), 

### Linksammlung

tutorials:
https://medium.com/@adriensieg/text-similarities-da019229c894
http://www.lumenai.fr/blog/quick-review-on-text-clustering-and-text-similarity-approaches
https://rare-technologies.com/word2vec-tutorial/
https://www.kaggle.com/antriksh5235/semantic-similarity-using-wordnet

docs:
https://nlpforhackers.io/wordnet-sentence-similarity/
https://radimrehurek.com/gensim/models/word2vec.html
https://radimrehurek.com/gensim/models/doc2vec.html#gensim.models.doc2vec.Doc2Vec

papers:
https://www.researchgate.net/publication/220413726_Using_WordNet_for_Text_Categorization
https://arxiv.org/ftp/arxiv/papers/1510/1510.02755.pdf
https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf
https://www.sciencedirect.com/science/article/pii/S0957417414006472

repos:
https://www.codesharehub.com/post/0d9fb53454355468be96f4dae7a1f6b8e09eb3e5
https://github.com/daneads/pypatent
https://github.com/tensorflow/models/blob/master/tutorials/embedding/word2vec.py

data:
https://www.google.com/googlebooks/uspto-patents-grants-text.html
https://bulkdata.uspto.gov/
http://www.triz40.com/aff_Principles_TRIZ.php

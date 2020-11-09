# Patent Text Match

Applying text similarity algorithms on patent texts and the 40 TRIZ principles
to classify potential innovation methods.

## Getting Started

Requires python3 and python-pip to be installed

```
make install
```

## Load models

Es wird der 1.5G GoogleNews-vectors-negative300.bin.gz Datensatz geladen, also
der Google News corpus (3 billion running words), der aber nur an einer Stelle
für word2vec auf englischen Daten benötigt wird. Diese Stelle ist aktuell
auskommentiert.

```
make load
```

## tfidf

Term Frequenz - Inverse Dokumenten Frequenz

Mit diesem Ansatz wird die Ähnlichkeit von Texten untersucht, indem mit dem
*sklearn* Feature Extraktor jedem Text ein Punkt in einem hochdimensionalen
Vektorraum zugeordnet wird (der sich aus den normierten Termen des jeweiligen
Dokuments berechnet) und dann der Kosinus des Winkels zwischen zwei solchen
Vektoren als Ähnlichkeitsmaß genommen wird.

Als Vergleichstexte werden die Beschreibungen der 40 TRIZ-Prinzipien genommen,
gegen die einzelne Patenttexte als Probetexte untersucht werden.  Die
beobachteten Ähnlichkeiten bleiben weitgehend unter 0.1, die
Crossvalidierungen der 40 Referenztexte gegeneinander bewegen sich in
ähnlichen Größenordnungen.

Beim Vergleich englischer Texte wird eine Warung "Your stop_words may be
inconsistent with your preprocessing" ausgegeben.

## wordnet

Es werden die Daten des Wordnet-Modells von *nltk* nach $HOME/nltk_data
geladen (das muss nur einmal geschehen, danach kann die entsprechende
Codezeile auskommentiert werden), auf dieser Basis werden wieder
Ähnlichkeitsmaße zwischen dem Probetext und den Vergleichstexten der 40
TRIZ-Methoden berechnet.

## word2vec

Mit *gensim* wird eine Bibliothek verwendet, die zunächst ein eigenes
neuronales Netz auf den Vergleichsdaten trainiert.  Im Fall deutscher Texte
wird dieses Modell unter models/model.bin abgespeichert (dazu muss der
aktuelle Code aber weiter modifiziert werden).  Auf dieser Basis werden wieder
Ähnlichkeitsmaße zwischen dem Probetext und den Vergleichstexten der 40
TRIZ-Methoden berechnet.

In der englischen Version (auskommentiert) wird der Google News Vector als
Vergleich verwendet.  Dieser Zugang bleibt unverständlich.

## Notes

2: zigarettenpackung
27: teebeutel windel etc tetrapack, wegwerf zigaretten anzünder (feuer), 

## Linksammlung

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

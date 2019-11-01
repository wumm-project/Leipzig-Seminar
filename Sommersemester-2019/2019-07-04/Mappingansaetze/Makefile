#

help:
	@echo "    install"
	@echo "			Install python requirements."
	@echo "    load"
	@echo "			Download Data"
	@echo "    train"
	@echo "			Train a new W2V model on data"
	@echo "    tfidf"
	@echo "			compare texts by term frequency - inverse document frequency"
	@echo "    wordnet"
	@echo "			compare texts using wordnet"
	@echo "    word2vec"
	@echo "			compate texts using W2V"

install:
	python3 -m pip install -r requirements.txt

load:
	cd models
	wget https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz

train:
	@echo "not implemented yet"
	python3 word2vec.py

tfidf:
	python3 tfidf.py

wordnet:
	@echo "not implemented yet"

word2vec:
	python3 word2vec.py

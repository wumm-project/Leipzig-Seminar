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
	@echo "    word2vec"
	@echo "			compate texts using W2V"

install:
	python3 -m pip install -r requirements.txt

load:
	cd models
	wget https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz

train:
	python3 word2vec.py

tfidf:
	python3 tfidf.py

word2vec:
	python3 word2vec.py

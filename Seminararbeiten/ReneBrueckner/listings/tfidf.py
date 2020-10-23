def tfidf(text, compareset, stopwords):
    vect = TfidfVectorizer(min_df = 1, stop_words = stopwords)
    tfidf = vect.fit_transform([text] + compareset)
    return((tfidf * tfidf.T).A[0][1:])

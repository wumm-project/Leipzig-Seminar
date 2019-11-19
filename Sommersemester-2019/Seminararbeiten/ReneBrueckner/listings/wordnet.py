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

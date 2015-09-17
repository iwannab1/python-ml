from gensim import corpora, models, similarities

def main():
    corpus = corpora.BleiCorpus('./data/ap/ap.dat', './data/ap/vocab.txt')
    model = models.LdaModel(corpus, num_topics=100, id2word=corpus.id2word)
    topics = [model[c] for c in corpus]
    print(topics[0])

if __name__ == "__main__":
    main()

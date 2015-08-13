import re
import math
from functools import reduce

def main():
    # 1
    training_sentence = input()
    training_model = create_BOW(training_sentence)

    # 2
    testing_sentence = input()
    testing_model = create_BOW(testing_sentence)

    # 3
    alpha = float(input())

    print(calculate_doc_prob(training_model, testing_model, alpha))


def calculate_doc_prob(training_model, testing_model, alpha):
    # Implement likelihood function here...
    train_dic = training_model[0]
    train_list = training_model[1]
    N = reduce(lambda x, y: (x + y), train_list)
    d = len(train_dic)

    p = 0
    logprob = 0
    for word in testing_model[0]:
        if word in training_model[0]:
            p = train_list[train_dic[word]]
        times = testing_model[1][testing_model[0][word]]
        logprob += math.log(((p+alpha) / (N + d*alpha))) * times
        p = 0

    return logprob

def create_BOW(sentence):
    bow_dict = {}
    bow = []

    sentence = sentence.lower()
    sentence = replace_non_alphabetic_chars_to_space(sentence)
    words = sentence.split(' ')
    for token in words:
        if len(token) < 1: continue
        if token not in bow_dict:
            new_idx = len(bow)
            bow.append(0)
            bow_dict[token] = new_idx
        bow[bow_dict[token]] += 1

    return bow_dict, bow

def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()

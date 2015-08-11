import re
import collections

def main():
    sentence = input()
    BOW_dict, BOW = create_BOW(sentence)

    print(BOW_dict)
    print(BOW)


def hasKey(words_bags, key):
    if key in words_bags:
        return True
    else:
        return False


def create_BOW(sentence):
    # Exercise
    bow_dict = collections.OrderedDict()
    bow = []
    sentence = replace_non_alphabetic_chars_to_space(sentence.lower())
    arr = sentence.split(" ")
    idx = 0
    for s in arr:
        if len(s) >= 1:
            if hasKey(bow_dict,s):
                pos = list(bow_dict.keys()).index(s)
                bow[pos] += 1
            else:
                bow_dict[s] = idx
                idx += 1
                bow.append(1)
    return dict(bow_dict), bow


def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()

__author__ = 'iwannab1'

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np


def main():

    (features, fnames, target, tnames) = loaddata()


def dividebyplength(features, target, tnames):
    plength = features[:,2]
    labels = tnames[target]
    is_setosa = (labels == 'setosa')
    max_setosa = plength[is_setosa].max()
    min_non_setosa = plength[~is_setosa].min()



def loaddata():
    data = load_iris()
    features = data['data']
    features_names = data['feature_names']
    target = data['target']
    target_names = data['target_names']
    return features, features_names, target, target_names

if __name__ == "__main__":
    main()
import numpy as np


class WordStatistics:
    def __init__(self, cache=True):
        self.cache = cache

    def train(self, data):
        raise NotYetImplemented()

    def predict(self, data):
        raise NotYetImplemented()

    def save(self, model_path):
        raise NotYetImplemented()

    def read(self, model_path):
        raise NotYetImplemented()

    def choice(self, x, p, size=1):
        return np.random.choice(len(x), size, p=p)
import numpy as np


class RandomVariable():

    def __init__(self, sample):
        self.sample = sample
    
    def mean(self):
        return np.sum(self.sample)/np.size(self.sample)
    
    def getAsNumpyArray(self):
        return self.sample
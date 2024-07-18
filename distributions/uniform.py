import numpy as np
from random_variable.random_variable import RandomVariable


class UniformDistribution:

    def __init__(self, randomNumberGenerator):
        self.randomNumberGenerator = randomNumberGenerator
    
    def getNext(self):
        return self.randomNumberGenerator.getNext() / self.randomNumberGenerator.getM()

    def getSample(self, size):
        sampleArray = np.zeros(size)

        for k in range(size):
            sampleArray[k] = UniformDistribution.getNext(self)
        
        return RandomVariable(sampleArray)
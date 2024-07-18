import numpy as np
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


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
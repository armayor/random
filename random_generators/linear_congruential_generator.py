import numpy as np

class LinearCongruentialGenerator:
    """Generates random numbers using a Linear Congruential Generator
    
    $ x_i = (ax_{i+1} + c) \mod m $
    
    where $ i = 1,2,3,... $,
          $ 0 \leq a, c, x_0 < m $
          $ m \in \mathbb{N} $
          $ a, c, x_0 \in \mathbb{N} \cup \{0\} $

    Attributes:
        seed (int): x_0
        a    (int): a
        c    (int): c
        m    (int): m

    Methods:
        getNext(): returns a random integer number
        getSeed(): returns the x_0 being used
        getA()   : returns the a being used
        getC()   : returns the c being used
        getA()   : returns the m being used
    """

    def __init__(self, seed = 123456789, a = 1664525, c = 1013904223, m = 2**32):
        self.seed = seed
        self.a    = a
        self.c    = c
        self.m    = m

    def getNext(self):
        """Returns an integer random number"""
        x = (self.a * self.seed + self.c) % self.m
        self.seed = x
        return x

    def getSeed(self):
        """Returns the x_0 being used"""
        return self.seed
    
    def getA(self):
        """Returns the a being used"""
        return self.a
    
    def getC(self):
        """Returns the c being used"""
        return self.c
    
    def getM(self):
        """Returns the m being used"""
        return self.m

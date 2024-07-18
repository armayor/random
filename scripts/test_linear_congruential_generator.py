import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from random_generators.linear_congruential_generator import LinearCongruentialGenerator
from distributions.uniform import UniformDistribution


randomNumberGenerator = LinearCongruentialGenerator()
uniform = UniformDistribution(randomNumberGenerator)

print(uniform.getSample(20).mean())

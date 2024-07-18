
from random_generators.linear_congruential_generator import LinearCongruentialGenerator
from distributions.uniform import UniformDistribution


randomNumberGenerator = LinearCongruentialGenerator()
uniform = UniformDistribution(randomNumberGenerator)

print(uniform.getSample(20).mean())


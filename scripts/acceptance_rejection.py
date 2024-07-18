import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import qmc


sampleSize = 100000
uniformSample = np.random.uniform(0,1,sampleSize)

def van_der_corput_sequence(n, base=2):
    """Generate the first n terms of the van der Corput sequence with the given base."""
    sequence = []
    for i in range(1, n + 1):
        vdc = 0
        denom = 1
        num = i
        while num:
            denom *= base
            num, remainder = divmod(num, base)
            vdc += remainder / denom
        sequence.append(vdc)
    return np.array(sequence)

uniformSample = van_der_corput_sequence(sampleSize)
x = []
y = []

for k in  range(sampleSize):
    if k%2 == 0:
        x.append(uniformSample[k])
    else:
        y.append(uniformSample[k])

u = np.array(x)
v = np.array(y)


def f(x):
    return 1/np.sqrt(2*np.pi) * np.exp( - 1/2 * x **2 )

def g(x):
    return 1/2 * np.exp( - np.abs(x))


def quantileFunctionY(x):
    return - np.sign( 2 * x - 1) * np.log( 1 - np.sign(x) * np.abs( 2 * x - 1 ))





C = np.sqrt( 2 * np.e / np.pi )
z =  quantileFunctionY(v)
accepted = 0

fDistributedPoints = []
for i in range(50000):
    if u[i] <= f(z[i]) / (C * g(z[i])):
        accepted += 1
        fDistributedPoints.append(z[i])


print(f"Media = {np.mean(fDistributedPoints)} y sigma = {np.sqrt(np.var(fDistributedPoints))}")
print(f"Probabilidad de aceptar punto = {accepted/50000}")
print(f"1/C = {1/C}")

plt.hist(fDistributedPoints, bins= 30)
plt.show()
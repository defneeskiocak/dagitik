import random
import numpy
import matplotlib.pyplot as plt
mu1 = -2
varyans1 = random.uniform(0.5, 1.5)
mu2 = 2
varyans2 = random.uniform(0.5, 1.5)

a = [int(round(numpy.random.normal(mu1, varyans1, 1), 0))]
for x in range(1, 10000, 1):
    a.append(int(round(numpy.random.normal(mu1, varyans1, 1), 0)))

b = [int(round(numpy.random.normal(mu2, varyans2, 1), 0))]
for x in range(1, 10000, 1):
    b.append(int(round(numpy.random.normal(mu2, varyans2, 1), 0)))

histA = [0] * 41
histB = [0] * 41

countA = 0
countB = 0

for n in range(0, len(a), 1):
    histA[(a[n]+20)] += 1
    countA += 1

for n in range(0, len(b), 1):
    histB[(b[n]+20)] += 1
    countB += 1

for n in range(0, len(histA), 1):
    histA[n] = float(histA[n])/float(countA)

for n in range(0, len(histB), 1):
    histB[n] = float(histB[n])/float(countB)

indexA = 0
indexB = 0

for n in range(0, len(histA), 1):
    if histA[n] == 0:
        indexA += 1
    else:
        break

for n in range(0, len(histB), 1):
    if histB[n] == 0:
        indexB += 1
    else:
        break


plt.bar(range(-20, 21), histA)
plt.show()
plt.bar(range(-20, 21), histB)
plt.show()

sumDist = 0

for n in range(0, 40, 1):
    if (histA[indexA] < histB[indexB]) and histA[indexA] != 0:
        sumDist += histA[indexA]*abs(indexB-indexA)
        histB[indexB] -= histA[indexA]
        histA[indexA] = 0
        indexA += 1
    elif (histA[indexA] > histB[indexB]) and histB[indexB] != 0:
        sumDist += histB[indexB]*abs(indexB-indexA)
        histA[indexA] -= histB[indexB]
        histB[indexB] = 0
        indexB += 1
    elif (histA[indexA] == histB[indexB]) and histA[indexA] != 0 and histB[indexB] != 0:
        sumDist += histB[indexB]*abs(indexB-indexA)
        histA[indexA] = 0
        histB[indexB] = 0
        indexA += 1
        indexB += 1

print "sumDist:", (sumDist)


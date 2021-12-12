import matplotlib.pyplot as plt

baseLine = [1,2,3,4,5,6,7,8,9,10]
firstLine = [1,2,3,4,5,6,7,8,9,10]
secondLine = [11,12,13,14,15,16,17,18,19,20]

plt.plot(baseLine, firstLine, c='red', alpha=0.5)
plt.plot(baseLine, secondLine, c='blue', alpha=0.5)

plt.fill_between(baseLine, firstLine, secondLine, facecolor='blue', alpha=0.1)
plt.show()
import matplotlib.pyplot as plt

from randomWalk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

pointNumbers = list(range(rw.num_points))
# plt.scatter(rw.xValues, rw.yValues, s=15)
plt.scatter(
    rw.xValues,
    rw.yValues,
    c=pointNumbers,
    cmap=plt.cm.Blues,
    edgecolors='none',
    s=5)

plt.scatter(0,0, c='green', s=20)
plt.scatter(rw.xValues[-1],rw.yValues[-1], c='red', s=20)

plt.show()

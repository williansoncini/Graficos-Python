import matplotlib.pyplot as plt
from randomWalk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

pointNumbers = list(range(rw.num_points))
plt.scatter(
    rw.xValues,
    rw.yValues,
    c=pointNumbers,
    cmap=plt.cm.Blues,
    edgecolors='none',
    s=1)

# plt.figure(dpi=128, figsize=(10,6))
plt.show()

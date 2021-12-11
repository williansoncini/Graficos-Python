import matplotlib.pyplot as plt

# xValues = [1,2,3,4,5]
xValues = list(range(1,1001))
# yValues = [1,4,9,16,25]
yValues = [x**2 for x in xValues]

# plt.scatter(xValues,yValues, c=(0,0,0.8),edgecolors='none',s=40)
plt.scatter(
    xValues,
    yValues, 
    c=yValues,
    cmap=plt.cm.Blues,
    edgecolors='none',
    s=40)

plt.title("Square numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0,1100,0,1100000])
plt.savefig('squaresPlot.png', bbox_inches='tight')
plt.show()
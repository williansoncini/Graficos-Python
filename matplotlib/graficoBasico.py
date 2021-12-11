import matplotlib.pyplot as plt

inputValues = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(inputValues,squares, linewidth=5)

plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square value", fontsize=14)

plt.tick_params(axis="both", labelsize=14)
plt.show()
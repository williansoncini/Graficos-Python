from dice import Dice
import pygal

dice = Dice()

results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

frequencies = []
for value in range(1,dice.numSides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."

hist._x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.x_labels = [1,2,3,4,5,6]
hist.add('D6', frequencies)

hist.render_to_file('diceVisual.svg')
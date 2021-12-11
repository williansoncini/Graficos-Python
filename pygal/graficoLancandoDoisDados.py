import pygal
from dice import Dice

firstDice = Dice()
secondDice = Dice()

results = []
for row_num in range(1000):
    result = firstDice.roll() + secondDice.roll()
    results.append(result)

frequencies = []
max_result = firstDice.numSides + secondDice.numSides
for value in  range(2,max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Results of rolling two D6 dice 100 times.'
hist.x_labels = [2,3,4,5,6,7,8,9,10,11,12]
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dualDice.svg')

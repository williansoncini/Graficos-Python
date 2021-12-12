from csv import reader
from os.path import realpath
from matplotlib import pyplot as plt
from datetime import datetime

fileName ="sitka_weather_2018_full.csv"
pathFile = realpath('data/csv/'+fileName)

with open(pathFile) as file:
    csvFile = reader(file)
    header = next(csvFile)
    
    highs = []
    mins = []
    dates = []
    for row in csvFile:
        try:
            high = float(row[8])
        except ValueError:
            high = 0
        else:
            highs.append(high)

        try:
            min = float(row[9])
        except ValueError:
            min = 0
        else:
            mins.append(min)

        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))

plt.style.use('seaborn')
fig = plt.figure()

plt.plot(dates[:20],highs[:20], c='red')
plt.plot(dates[:20],mins[:20], c='blue')
plt.fill_between(dates[:20],highs[:20],mins[:20], facecolor='blue', alpha=0.1)

plt.xlabel('', fontsize=16)
plt.title('Max and Min temperature.')
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

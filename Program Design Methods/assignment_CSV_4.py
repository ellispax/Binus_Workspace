

import matplotlib.pyplot as plt


import csv

filename = open("C:/Users/Ellis_Pax/Desktop/binus Academics/programming/jude assignments/class ting/csv files/activity.csv", "r")
csvReader = csv.reader(filename)


def getPerInterval(filename, reader):
    next(reader)
    stepsPerInterval = [0]*288
    totalDays = 61
    acc = 0
    while True:
        try:
            step = next(reader)[0]
            stepsPerInterval[acc] += int(step) if step != "NA" else 0
            acc += 1
            if acc == 288:
                acc = 0
        except StopIteration:
            break
    weekdayAverage = []
    weekendAverage = []
    dayCounter = 1
    for steps in stepsPerInterval:
        if dayCounter in [6, 7]:
            weekendAverage.append(steps/totalDays)
        else:
            weekdayAverage.append(steps/totalDays)
        dayCounter += 1
        if dayCounter == 8:
            dayCounter = 1
    filename.seek(0)
    return weekdayAverage, weekendAverage


def makePlot(weekday, weekend):
    xday = [x+1 for x in range(len(weekday))]
    xend = [x+1 for x in range(len(weekend))]
    fig, axs = plt.subplots(2)
    axs[0].set_title("Weekday")
    axs[0].plot(xday, weekday)
    axs[1].set_title("Weekend")
    axs[1].plot(xend, weekend)
    plt.tight_layout()
    plt.show()


makePlot(*getPerInterval(filename, csvReader))
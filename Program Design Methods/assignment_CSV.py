import csv

import matplotlib.pyplot as plt
import statistics

filename = open('C:/Users/Ellis_Pax/Desktop/binus Academics/programming/jude assignments/class ting/csv files/activity.csv', "r")
csvReader = csv.reader(filename)

def get_steps(filename, reader):
    next(reader)
    steps = []
    counter = 0
    step_day = 0
    while True:
         try:
            counter += 1
            step = next(reader)[0]
            step_day += int(step) if step != "NA" else 0
            if counter % 288 == 0:
                steps.append(step_day)
                step_day = 0
         except StopIteration:
            break
    filename.seek(0)
    return steps

def get_mean_median(filename, reader):
    next(reader)
    day_mean = []
    day_median = []
    counter = 0
    step_day = []
    
    while True:
        try:
            counter = counter + 1
            step = next(reader)[0]
            step_day.append(int(step) if step != "NA" else 0)
            if counter % 288 == 0:
                step_day.sort()
                day_median.append(statistics.median(step_day))
                day_mean.append(statistics.mean(step_day))
                step_day = []
        except StopIteration:
            break
    filename.seek(0)
    return day_median, day_mean

def makePlot(steps, median, mean):
    x = [x+1 for x in range(len(steps))]
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Activity')
    ax1.set_title("Steps")
    ax1.plot(x, steps)
    ax2.set_title("Median")
    ax2.plot(x, median)
    ax3.set_title("Mean")
    ax3.plot(x, mean)
    plt.tight_layout()
    plt.show()


steps = get_steps(filename, csvReader)
median, mean = get_mean_median(filename, csvReader)
# print(mean)

makePlot(steps, median, mean)
    
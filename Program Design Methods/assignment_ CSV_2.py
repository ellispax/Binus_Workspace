import csv

import matplotlib.pyplot as plt


filename = open("C:/Users/Ellis_Pax/Desktop/binus Academics/programming/jude assignments/class ting/csv files/activity.csv", "r")
csvReader = csv.reader(filename)

def get_interval(filename, reader):
    next(reader)
    interval_steps = [0]*288
    total_days = 61
    counter = 0
    while True:
        try:
            counter  += 1
            step = next(reader)
            interval_steps[counter] += int(step) if step != "NA" else 0
           
            if counter == 288:
                counter = 0
        except StopIteration:
            break
    interval_steps_avg = []
    for steps in interval_steps:
        interval_steps_avg.append(steps/total_days)
    filename.seek(0)
    return interval_steps, interval_steps_avg

def plotme(interval, interval_avg):
    x = [x + 1 for  x in range(len(interval))]
    fig, axs = plt.subplots(2)
    axs[0].set_title("Daily Activity Pattern")
    axs[0].plot(x, interval)
    axs[1].set_title("Interval Average")
    axs[1].plot(x, interval_avg)
    plt.tight_layout()
    plt.show()
    
plotme(*get_interval(filename, csvReader))

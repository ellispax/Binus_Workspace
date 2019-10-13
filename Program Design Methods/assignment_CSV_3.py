import re
import csv
import pygal
import statistics

filename = open("C:/Users/Ellis_Pax/Desktop/binus Academics/programming/jude assignments/class ting/csv files/activity.csv", "r")
csvReader = csv.reader(filename)

def find_NA(filename, reader):
    next(reader)
    NA = 0
    
    while True:
        try:
            if "NA" == next(reader)[0]:
                NA += 1
        except StopIteration:
            break
    filename.seek(0)
    return NA

def get_median_mean(filename, reader):
    next(reader)
    median = []
    mean = []
    step_today = []
    counter = 0
    
    while True:
        try:
            counter += 1
            step = next(reader)[0]
            step_today.append(int(step) if step != "NA" else 0)
            if counter % 288 == 0:
                step_today.sort()
                median.append(statistics.median(step_today))
                mean.append(statistics.mean(step_today))
                step_today = []
        except StopIteration:
            break
    filename.seek(0)
    return median, mean

def csv_replacer(filename, find, replace):
    data = filename.read()
    csv = re.sub(find, replace, data)
    filename.seek(0)
    return csv

def write_csv(filename, data):
    try:
        with open(filename, "w") as file_obj:
            file_obj.write(data)
        return True
    except Exception:
        return False


def histogram(median, mean):
    histogram = pygal.Bar()
    histogram.title = "Daily Activity"
    days = [str(x + 1) for x in range(len(mean))]
    for index, day in enumerate(days):
        histogram.add(day, mean[index])
    histogram.render_in_browser()
    
print(f"NA in the filename: {find_NA(filename, csvReader)}")
newCSV = csv_replacer(filename, "NA", "0")
print("File written successfully") if write_csv(
    "activity_fixed.csv", newCSV) else print("Something's wrong")
histogram(*get_median_mean(filename, csvReader))
    
            
    
        
            
    
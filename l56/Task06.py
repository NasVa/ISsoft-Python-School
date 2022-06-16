import csv
import sortings
import time
import json
import copy

data = []
id_and_marks = {}
res_nums = []
methods = []
statistics = {}
nums = []

def output_satistics():
    path = "Statistics.csv"
    csv.register_dialect("dial", delimiter = "-")
    with open(path, 'w', newline = "") as inputFile:
        writer = csv.writer(inputFile, "dial")
        for key, value in statistics.items():
            writer.writerow([key, value])

def create_functions_dict():
    global methods, statistics
    methods = [i for i in dir(sortings) if 'Sort' in i]
    statistics = dict.fromkeys(methods, 0)

def read_file():
    global data, nums
    path = "Input.json"
    with open(path, 'r') as f:
        data = json.load(f)
    try:
        for i in data:
            id_and_marks[i["ID"]] = sum(i["Marks"]) // len(i["Marks"])
            nums = list(id_and_marks.values())
    except TypeError:
        return("Incomparable types of elements")


def sorts():
    for i in statistics:
        start = time.perf_counter_ns()
        res_nums.append(getattr(sortings, i)(copy.copy(nums)))
        result = time.perf_counter_ns() - start
        statistics[i] = result / 1000000000
    print(statistics)
    print(res_nums)

def write_file():
    path = "Output.json"
    global nums, id_and_marks, data
    with open(path, 'w') as f:
        for i in nums:
           for j in id_and_marks:
               if id_and_marks[j] == i:
                   for i in data:
                       if i["ID"] == j:
                           elem = i
                           break
                   json.dump(elem, f)
                   del id_and_marks[j]
                   break

create_functions_dict()
read_file()
sorts()
write_file()
output_satistics()
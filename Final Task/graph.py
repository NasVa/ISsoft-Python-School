import csv 

cities = [['a', 'f', 14, 3],
          ['a', 'g', 12, 6],
          ['a', 'd', 10, 1],
          ['f', 'd', 9, 2],
          ['g', 'd', 3, 1],
          ['f', 'b', 5, 4],
          ['d', 'e', 1, 8],
          ['b', 'e', 11, 3],
          ['g', 'c', 13, 2],
          ['c', 'b', 15, 1],
          ['e', 'h', 5, 3]]

def write_file(nums, path = "map.csv"):
    csv.register_dialect("dial", delimiter = ",")
    with open(path, 'w', newline = "") as inputFile:
        writer = csv.writer(inputFile, "dial")
        for i in nums:
            writer.writerow(j for j in i)

def read_file(path = "map.csv"):
    info = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        info = [i for i in reader]
    return info

def take_cities(info):
        cities = []
        for i in info:
            for j in range(2):
                if not i[j] in cities:
                    cities.append(i[j])
        return cities

class Node:
    ''' Represent city on the map.'''

    def __init__(self, name):
        self.name = name
        self.threads =[]

class Thread:
    ''' Represent road on the map.'''

    def __init__(self, next, prev, complexity, distance):
        self.next = next
        self.prev = prev
        self.complexity = int(complexity)
        self.distance = int(distance) 

    def get_target(self, start):
        return self.next if start == self.prev.name else self.prev


class Graph:
    ''' Represent map.'''

    def __init__(self):
        self.cities = []
        self.threads = []
        info = read_file()
        self.cities_list = take_cities(info)
        for city in self.cities_list:
            self.cities.append(Node(city))
        for row in info:
            thread = Thread(self.cities[self.cities_list.index(row[0])], self.cities[self.cities_list.index(row[1])], row[2], row[3])
            self.threads.append(thread)
            self.cities[self.cities_list.index(row[0])].threads.append(thread)
            self.cities[self.cities_list.index(row[1])].threads.append(thread)

    def get_city(self, name):
        for i in self.cities:
            if i.name == name:
                return i
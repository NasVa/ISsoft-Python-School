import csv
import carPark
import graph

min_path = []    
min_path_price = 9999999
start_point = None
target_point = None
target_points = []

def is_target_points_done(cur_path):
    for i in target_points:
        if not target_points in cur_path:
            return False
    return True

def is_target(cur_path):
    if cur_path[-1] != target_point:
        return False
    else:
        return is_target_points_done(cur_path)
   
min_path = 0

def is_necessary_path(path, indices):
    for i in range(1, len(indices)):
        for city in path[indices[i-1]+1:indices[i]]:
            if city in target_points:
                break       # цикл содержит цель
        else:
            return False
        if "".join(path).count("".join(path[indices[i-1]+1:indices[i]])) > 1:
            return False # содержит хороший цикл несколько раз
    return True

def is_contains_cycle(cur_path):
    indices = []
    for i in cur_path:
        if cur_path.count(i) > 1: # один город проехали несколько раз
            indices = [j for j in range(len(cur_path)) if cur_path[j] == i] # список номеров вхождений 
            if not is_necessary_path(cur_path, indices):
                return True
    if not len(indices):
        return False
    



def find_path(cur_path, cur_price):
    '''Find minimum fuel price path.'''

    global min_path_price
    if len(cur_path) >= len(target_points) + 2:
        if is_target(cur_path):
            return cur_path #good_path

    if not len(cur_path): #start
        cur_path.append(start_point)
    for thread in graph.get_city(cur_path[-1]).threads:
        if len(thread.get_target(graph.get_city(cur_path[-1])).threads) == 1: #тупик
            if thread.get_target(graph.get_city(cur_path[-1])) not in target_points:
                return [[], 99999999999] #bad_path
            else:
                if tread.get_target(get_city(cur_path[-1])) in cur_path:
                    return [cur_path, cur_price]
        copy_path = cur_path.copy()
        next = thread.get_target(graph.get_city(cur_path[-1]).name).name
        copy_path.append(thread.get_target(graph.get_city(cur_path[-1]).name).name)
        print(copy_path)
        if is_contains_cycle(copy_path):
            if graph.get_city(cur_path[-1]).threads[-1] == thread:
                return [[], 99999999999] #bad_path
            else:
                continue
        result = find_path(copy_path, cur_price + (thread.distance * car.fuel_consumption / 100 * thread.complexity / car.passability_coefficient))
        if len(cur_path) >= len(target_points) + 2:
            if is_target(cur_path):
                if result[1] < min_path_price:
                    min_path = result[0]
                    min_path_price = result[1]
        

graph.write_file(graph.cities)
graph = graph.Graph()
carPark.CarFactory.add_car_type('LittleCar', 3, 10)
carPark.CarFactory.add_car_type('Truck', 2, 12)
carPark.CarFactory.add_car_type('Bus', 1, 15)
carPark.CarFactory.add_car_type('SUV', 6, 18)

car_type = input(f"Enter car of type: {carPark.CarFactory.get_car_types()}\n")
car = carPark.CarFactory.create_car(car_type)
#car = carPark.CarFactory.create_car("Truck")
#start_point = 'a'
#target_point = 'b'
#target_points = ['f', 'e', 'c']
print(f"Cities: {graph.cities_list}")
start_point = input(f"Enter the start point: ")
target_point = input(f"Enter the target point: ")
while True:
    res = input("Enter intermediate cities (Enter - stop): ")
    if res:
        target_points.append(res)
    else:
        break
path = find_path([], 0)
if len(path[0]) > 0 :
    print(path)
else:
    print("Path is not found.")
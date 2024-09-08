from distances import *

#Greedy algorithm to determine the optimal ordering of a trucks package's
#O(n^2) runtime
def optimized_route(truck, current_location, sorted_truck, sorted_truck_idx):
    
    if not len(truck):
        return truck
    next_location = 0
    shortest_distance = 50.0
    for package in truck:
        d = int(package.location)
        if get_current_distance(current_location, d) <= shortest_distance:
            shortest_distance = get_current_distance(current_location, d)
            next_location = d
    for package in truck:
        d = int(package.location)
        if get_current_distance(current_location, d) == shortest_distance:
                    sorted_truck.append(package)
                    sorted_truck_idx.append(d)
                    truck.pop(truck.index(package))
                    current_location = next_location
                    optimized_route(truck, current_location, sorted_truck, sorted_truck_idx)
    return sorted_truck, sorted_truck_idx

import math
from itertools import permutations

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on Earth using the Haversine formula.
    """
    R = 6371  # Radius of the Earth in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance

def tsp(locations):
    """
    Solve the Traveling Salesman Problem for the given locations.
    Returns the optimized route and the total distance.
    """
    n = len(locations)
    best_route = None
    min_distance = float('inf')

    for permutation in permutations(range(1, n)):
        route = [0] + list(permutation)  # Start from the first location
        distance = 0

        for i in range(n-1):
            curr_loc = locations[route[i]]
            next_loc = locations[route[i+1]]
            distance += haversine(curr_loc['latitude'], curr_loc['longitude'], next_loc['latitude'], next_loc['longitude'])

        # Add the distance from the last city back to the starting city
        distance += haversine(locations[route[-1]]['latitude'], locations[route[-1]]['longitude'],
                              locations[0]['latitude'], locations[0]['longitude'])

        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

locations = {
    0: {'latitude': 23.8728568, 'longitude': 90.3984184, 'address': 'Uttara Branch'},  # Starting location
    1: {'latitude': 23.8513998, 'longitude': 90.3944536, 'address': 'City Bank Airport'},
    2: {'latitude': 23.8330429, 'longitude': 90.4092871, 'address': 'City Bank Nikunja'},
    3: {'latitude': 23.8679743, 'longitude': 90.3840879, 'address': 'City Bank Beside Uttara Diagnostic'},
    4: {'latitude': 23.8248293, 'longitude': 90.3551134, 'address': 'City Bank Mirpur 12'},
    5: {'latitude': 23.827149, 'longitude': 90.4106238, 'address': 'City Bank Le Meridien'},
    6: {'latitude': 23.8629078, 'longitude': 90.3816318, 'address': 'City Bank Shaheed Sarani'},
    7: {'latitude': 23.8673789, 'longitude': 90.429412, 'address': 'City Bank Narayanganj'},
    8: {'latitude': 23.8248938, 'longitude': 90.3549467, 'address': 'City Bank Pallabi'},
    9: {'latitude': 23.813316, 'longitude': 90.4147498, 'address': 'City Bank JFP'}
}

best_route, min_distance = tsp(locations)

print("Best Route:")
for index in best_route:
    print("\nLocation index:", index)
    print("Latitude:", locations[index]['latitude'])
    print("Longitude:", locations[index]['longitude'])
    print("Address:", locations[index]['address'])

print("\nTotal Distance:", min_distance)

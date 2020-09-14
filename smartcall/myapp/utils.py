# Vendor
from itertools import permutations
# Local
from .city_routes import CITY_ROUTES


def find_path_dijkstra(start_city: str, cities_to_visit: list):
    """Поиск кратчайшего пути по Дийкстра"""
    cities_to_visit = list.copy(cities_to_visit)
    total_distance = 0
    visited_cities = [start_city, ]
    current_city = start_city

    while len(cities_to_visit) > 0:
        ds = [city for city in CITY_ROUTES[current_city].items()
              if city[0] in cities_to_visit]
        found_city = min(ds, key=lambda x: x[1])
        current_city = found_city[0]
        visited_cities.append(found_city[0])
        total_distance += found_city[1]

        if len(cities_to_visit) == 1 and cities_to_visit[0] == start_city:
            break

        cities_to_visit.remove(current_city)
        if len(cities_to_visit) == 0:
            cities_to_visit.append(start_city)

    return total_distance, visited_cities


def calculate_direct_path(path: list) -> int:
    """Высчитываем расстояние для конкретного пути"""
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += CITY_ROUTES[path[i]][path[i + 1]]
    return total_distance


def find_path_bf(start_city: str, cities_to_visit: list):
    """Метод перебора для городов"""
    cities_to_visit = list.copy(cities_to_visit)
    min_distance, optimal_path = 0, []

    for i in permutations(cities_to_visit):
        path = [start_city, *i, start_city]
        calculated_distance = calculate_direct_path(path)
        if min_distance == 0 or min_distance > calculated_distance:
            min_distance = calculated_distance
            optimal_path = path

    return min_distance, optimal_path

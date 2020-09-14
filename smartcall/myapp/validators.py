# Vendor
from graphql import GraphQLError
# Local
from .city_routes import CITY_ROUTES


def validate_short_path(start_city: str, cities_to_visit: list):
    """Проверяем валидность введенных данных"""
    allowed_cities = list(CITY_ROUTES.keys())

    if start_city not in allowed_cities:
        raise GraphQLError(f'Стартовый город не в списке доступных городов. '
                           f'Список доступных городов: {str(allowed_cities)}')

    # Убираем дупликаты из городов
    cities_to_visit = list(dict.fromkeys(cities_to_visit))
    for city in cities_to_visit:
        if city not in allowed_cities:
            raise GraphQLError(f'Город - {city} не в списке доступных городов. '
                               f'Список доступных городов: '
                               f'{str(allowed_cities)}')

    try:
        cities_to_visit.remove(start_city)
    except ValueError:
        pass

    return start_city, cities_to_visit

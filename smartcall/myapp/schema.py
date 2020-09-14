# Vendor
from graphene import ObjectType, String, Schema, Int, List, Field
# Local
from .validators import validate_short_path
from . import utils


class ShortPath(ObjectType):
    total_distance = Int()
    path = List(String)


class Query(ObjectType):
    """Main Controller"""
    short_path = Field(
        ShortPath,
        start_city=String(),
        cities_to_visit=List(String),
    )

    def resolve_short_path(self, context, start_city, cities_to_visit):
        start_city, cities_to_visit = \
            validate_short_path(start_city, cities_to_visit)

        # Выбор алгоритма поиска по количеству городов,
        # для просчета большого кол-ва городов исп-ся метод Дийкстры
        # для небольшого кол-ва - метод перебора, этот метод будет являться
        # 100% верным
        if len(cities_to_visit) > 8:
            total_distance, path = \
                utils.find_path_dijkstra(start_city, cities_to_visit)
        else:
            total_distance, path = \
                utils.find_path_bf(start_city, cities_to_visit)
        return {
            'total_distance': total_distance,
            'path': path
        }


schema = Schema(query=Query, auto_camelcase=False)

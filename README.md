# SmartCall

### URL по которому находится проект:

https://arcane-oasis-76777.herokuapp.com/graphql/

### Пример запроса:

```
{
  short_path(start_city: "Астана", cities_to_visit: ["Алматы", "Уральск", "Шымкент", "Усть-Каменогорск", "Тараз", "Павлодар"]) {
    total_distance
    path
  }
}
```

### Пример ответа:
```
{
  "data": {
    "short_path": {
      "total_distance": 6729,
      "path": [
        "Астана",
        "Уральск",
        "Шымкент",
        "Тараз",
        "Алматы",
        "Усть-Каменогорск",
        "Павлодар",
        "Астана"
      ]
    }
  }
}
```

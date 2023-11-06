city_count = int(input("Введите количество городов: "))
cities = []

for _ in range(city_count):
    city = input("Введите название города: ")
    cities.append(city)

print("Список городов:", cities)

unique = set(cities)
duplicate = city_count - len(unique)

print("Количество городов с дублирующимися названиями:", duplicate)
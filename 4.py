def olympiad():
    algebra = set(input().split())
    geometry = set(input().split())
    trigonometry = set(input().split())

    common_students = algebra.intersection(geometry, trigonometry)

    if common_students:
        sorted_students = sorted(common_students)
        print(' '.join(sorted_students))
    else:
        print("Все три задачи никто не решил")


olympiad()

# Ввод:
# Иванов Петров Сидоров Михайлов
# Иванов Михайлов
# Сидоров Михайлов
# Вывод: Михайлов
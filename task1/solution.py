
def strict(func):
    def wrapper(*args, **kwargs):
        # результат выполняемой функции
        result = func(*args, **kwargs)
        # аннотации типов
        annotations = func.__annotations__
        # кортеж всех объектов функции
        arg = (*args, result)
        # получаем список bool-значений на соответствие типа и типа, полученного при аннотации
        check = all(map(lambda x: x[0] == type(x[1]), list(zip(annotations.values(), arg))))

        if check:
            return result
        else:
            raise TypeError
    return wrapper


# @strict
# def sum_two(a: int, b: int) -> int:
#     return a + b
#
# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError

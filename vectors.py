def myltiply_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Векторы должны быть одной длины.")

    # Проверка, что все элементы векторов - числа
    for v in vector1 + vector2:  # Объединяем два списка в один
        if not isinstance(v, (int, float)):  # Проверяем, является ли тип элемента int или float
            raise ValueError("Все элементы векторов должны быть числами.")

    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]

    return result


def multiply_by_scalar(vector, scalar):
    # Проверка, что скаляр - число
    if not isinstance(scalar, (int, float)):
        raise ValueError("Скаляр должен быть числом.")

    # Проверка, что все элементы вектора - числа
    for v in vector:
        if not isinstance(v, (int, float)):
            raise ValueError("Все элементы вектора должны быть числами.")

    result = []
    for i in range(len(vector)):
        result.append(vector[i] * scalar)

    return result

import numpy as np
from math import factorial, sqrt

# 2. Создание векторов x и y
x = np.arange(-10, 6)
y = np.arange(-5, 11)

# 3. Создание нового вектора z с чередованием элементов из x и y
z = np.zeros(len(x) + len(y), dtype=int)
z[::2] = x
z[1::2] = y
z_sorted = np.sort(z)

print(f"Вектор x: {x}")
print(f"Вектор y: {y}")
print(f"Вектор z (чередующийся): {z}")
print(f"Отсортированный вектор z: {z_sorted}")

# 4. Функции для вычисления разных норм вектора
def l1_norm(v):
    return np.sum(np.abs(v))  # Манхэттенская норма

def l2_norm(v):
    return np.sqrt(np.sum(v**2))  # Евклидова норма

def l_inf_norm(v):
    return np.max(np.abs(v))  # Чебышёвская норма

# Нахождение норм векторов x, y, z
l1_x = l1_norm(x)
l2_x = l2_norm(x)
l_inf_x = l_inf_norm(x)

l1_y = l1_norm(y)
l2_y = l2_norm(y)
l_inf_y = l_inf_norm(y)

l1_z = l1_norm(z)
l2_z = l2_norm(z)
l_inf_z = l_inf_norm(z)

print(f"Нормы вектора x: L1 = {l1_x}, L2 = {l2_x}, L∞ = {l_inf_x}")
print(f"Нормы вектора y: L1 = {l1_y}, L2 = {l2_y}, L∞ = {l_inf_y}")
print(f"Нормы вектора z: L1 = {l1_z}, L2 = {l2_z}, L∞ = {l_inf_z}")

# 5. Создание матрицы A и вычисление суммы по строкам и столбцам
A = np.arange(1, 101).reshape(10, 10)

sum_by_columns = np.sum(A, axis=0)
sum_by_rows = np.sum(A, axis=1)


# Умножение матрицы A на векторы суммы по столбцам и строкам
product_columns = np.dot(A, sum_by_columns)
product_rows = np.dot(A.T, sum_by_rows)

# Исключение последних 5 строк и столбцов из матрицы A
B = A[:5, :5]

print(f"Матрица A:\n{A}")
print(f"Сумма по столбцам: {sum_by_columns}")
print(f"Сумма по строкам: {sum_by_rows}")
print(f"Произведение матрицы A на вектор суммы по столбцам: {product_columns}")
print(f"Произведение матрицы A на вектор суммы по строкам: {product_rows}")
print(f"Матрица B (без последних 5 строк и столбцов):\n{B}")

# 6. Функция для вычисления факториала числа
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = 5  # Пример использования
print(f"Факториал {n}: {factorial_iterative(n)}")

# 7. Создание вектора из 5 элементов с клавиатуры и нахождение мин, макс и суммы
vector = np.array([int(input(f"Введите элемент {i+1} для вектора: ")) for i in range(5)])

min_element = np.min(vector)
max_element = np.max(vector)
sum_elements = np.sum(vector)

print(f"Введенный вектор: {vector}")
print(f"Минимальный элемент: {min_element}")
print(f"Максимальный элемент: {max_element}")
print(f"Сумма элементов: {sum_elements}")

# 7. Нахождение новой нормы введенного вектора
l1_vector = l1_norm(vector)
l2_vector = l2_norm(vector)
l_inf_vector = l_inf_norm(vector)

print(f"Нормы введенного вектора: L1 = {l1_vector}, L2 = {l2_vector}, L∞ = {l_inf_vector}")

# 7. Добавление весов и пересчет норм
weights = np.array([float(input(f"Введите вес для элемента {i+1}: ")) for i in range(5)])
weighted_vector = vector * weights

l1_weighted = l1_norm(weighted_vector)
l2_weighted = l2_norm(weighted_vector)
l_inf_weighted = l_inf_norm(weighted_vector)

print(f"Взвешенный вектор: {weighted_vector}")
print(f"Нормы взвешенного вектора: L1 = {l1_weighted}, L2 = {l2_weighted}, L∞ = {l_inf_weighted}")

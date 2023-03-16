import numpy as np

def gauss(a, x):
    for i in range(n):   # Преобразуем матрицу a(под диагональю 0, на диагонали могут быть не только 1)
        for j in range(i + 1, n):
            l = a[j][i] / a[i][i]      
            a[j] = a[j] - l * a[i]
            
    for i in range(n - 1, -1, -1):    # Заполняем матрицу x с конца
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]
        if x[i] == 0:
            x[i] = x[i]
        else:
            x[i] = x[i] / a[i][i]
            
A = [[81,-45,45],
    [-45,50,-15],
    [45,-15,38]]

b = [531,-460,193]
n = 3

print(A)
print(b)

L = np.zeros((n, n)) # Массив размера n * n из 0 для коэффициентов матрицы L
L_t = np.zeros((n, n)) # Массив размера n * n из 0 для коэффициентов матрицы, полученной при транспонировании L
x = np.zeros(n) # Массив размера 1 * n из 0 для ответ при решении L_t*x = y
y = np.zeros(n) # Массив размера 1 * n из 0 для ответ при решении Ly = b
a1 = np.zeros((n, n + 1)) # Массив размера n * (n + 1) из 0 для коэффициентов расширенной матрицы
a2 = np.zeros((n, n + 1)) # Массив размера n * (n + 1) из 0 для коэффициентов расширенной матрицы

    
L = np.linalg.cholesky(A) # Выполняем разложение Холецкого
L_t = np.transpose(L) # Транспонируем матрицу L

print('Матрица L, полученная при разложении Холецкого:')
print(L)
print('')

print('Матрица L_t, полученная при транспонировании матрицы L:')
print(L_t)
print('')

for i in range(n): # Создание расширенной матрицы из L и b
    for j in range(n + 1):
        if j < n:
            a1[i][j] = L[i][j]
        else:
            a1[i][j] = b[i]
      
gauss(a1, y) # По методу Гаусса находим y

for i in range(n): # Создание расширенной матрицы из L_t и y
    for j in range(n + 1):
        if j < n:
            a2[i][j] = L_t[i][j]
        else:
            a2[i][j] = y[i]
      
gauss(a2, x) # По методу Гаусса находим x

print('Решение:') # Вывод решения
for i in range(n):
    print('x' + str(i + 1) + ' = ' + str(x[i]))
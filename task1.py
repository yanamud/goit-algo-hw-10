import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize items", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість Лимонаду
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість Фруктового соку

# Функція цілі (Максимізація кількості)
model +=  A + B, "Items"

# Додавання обмежень
model += 2 * A + 1 * B <= 100  # Обмеження для води
model += 1 * A  <= 50  # Обмеження для цукру
model += 1 * A  <= 30  # Обмеження для лимонного соку
model += 2 * B <= 40  # Обмеження для фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти 'Лимонаду':", A.varValue, 'од.')
print("Виробляти 'Фруктового соку':", B.varValue, 'од.')
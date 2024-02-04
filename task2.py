import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import scipy.integrate as integrate

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа по осі Х
b = 2  # Верхня межа по осі Х
y_min = 0 # Нижня межа по осі У
y_max = 4 # Верхня межа по осі У

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')


# Додавання меж інтегрування та назви графіка
ax.axhline(y=y_min, color='k', linestyle="--")
ax.axhline(y=y_max, color='k', linestyle="--")
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


# Обчислення інтеграла
result, error = spi.quad(f, a, b)

def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return area


mc_result = monte_carlo_integrate(f, a, b, y_min, y_max, 1000000)

print("Розрахунок інтегралу з використанням функції 'quad': ", result)
print("Розрахунок інтегралу з використанням методу Монте-Карло: ", mc_result)
print("Оцінка абсолютної помилки: ", error)
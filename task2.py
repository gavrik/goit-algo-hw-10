import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as sci

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def build_plot(points, points_inside):
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    _, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)
    ax.scatter(
        [point[0] for point in points], 
        [point[1] for point in points ], 
        color = 'red')
    ax.scatter(
        [pi[0] for pi in points_inside],
        [pi[1] for pi in points_inside],
        color = 'green'
    )

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
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b) + ' для ' + str(len(points)) + ' точок')
    plt.grid()
    plt.show()

def is_inside(a, b, x, y):
    return y <= f(x)

def generate_random_dots(a, b, ndot = 1000):
    points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(ndot)]
    #print(points)
    points_inside = [point for point in points if is_inside(2,4,point[0],point[1])]
    #print(points_inside)
    return points, points_inside

def calculate_area(p, pi, a, b):
    return (pi/p) * (a * b)

if __name__ == "__main__":
    for ndot in [10,100,1000,10000,100000]:
        points, points_inside = generate_random_dots(2,4,ndot)
        print("Площа з використанням {} точок: {}".format(ndot, calculate_area(len(points), len(points_inside), 2, 4)))
        build_plot(points, points_inside)
    print("Теоретична площа: ", sci.quad(f,0,2)[0])

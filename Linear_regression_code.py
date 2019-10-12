import random
import matplotlib.pyplot as plt
import numpy

x_value = []
y_value = []


def find_xy():
    m_value = 0.5
    b_value = 5

    for i in range(20):
        x_value.append(random.randint(1, 1000))

    for i in x_value:
        y_value.append(i*m_value+b_value)
    plt.scatter(x_value, y_value)
    plt.show()


find_xy()


def intercept(x_bar, y_bar, b1):
    my_intercept = y_bar - (b1 * x_bar)
    return my_intercept


def find_means(x, y):
    mean_x = sum(x_value) / len(x_value)
    mean_y = sum(y_value) / len(y_value)

    num = 0
    den = 0

    x_len = len(x_value)
    for i in range(x_len):
        num += (x_value[i] - mean_x) * (y_value[i] - mean_y)
        den += (x_value[i] - mean_x)**2
    b1_value = num / den
    return b1_value, mean_x, mean_y


b1, x_bar, y_bar = find_means(x_value, y_value)
b0 = intercept(x_bar, y_bar, b1)
print(b1)
















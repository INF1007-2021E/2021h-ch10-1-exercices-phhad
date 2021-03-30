#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import math
import matplotlib.pyplot as plt

# TODO: Définissez vos fonctions ici (il en manque quelques unes)


def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, 64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    cartesian_coordinates = np.array([[4, 5, 2],[6, 8, 9]])
    result = np.ones_like(cartesian_coordinates)
    print(cartesian_coordinates)
    for i in range(3):
        rayon = math.sqrt((cartesian_coordinates[0,i] ** 2) + (cartesian_coordinates[1,i]** 2))
        angle = math.atan(cartesian_coordinates[1,i] / cartesian_coordinates[0,i])
        result[0,i] = rayon
        result[1,i] = angle
    print(result)


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values - number).argmin

    return

def graph():
    x = np.linspace(-1, 1, 250)
    y = x**2 * np.sin(1/x**2) + x
    plt.scatter(x, y)
    plt.show()

def Monte_Carlo(iteration: int=5000)
    """""
    x = np.linspace(0, 1, 5000)
    y = np.linspace(0, 1, 5000)
    if x > 1 and y > 1:
        return np.array[x,y]
    else:
        return np.array[x,y]

    plt.scatter(x, y)
    plt.show()
"""""
    xlist_inside = []
    xlist_out= []
    ylist_inside = []
    ylist_out = []
    for i in range(iteration):
        x = np.random.random()
        y = np.random.random()
        if np.sqrt(x**2 + y**2) <= 1:
            xlist_inside.append(x)
            ylist_inside.append(y)
        else:
            xlist_out.append(x)
            ylist_out.append(y)
    plt.scatter(xlist_inside, ylist_inside, label = "inside")
    plt.scatter(xlist_out, ylist_out, label = "outside")
    plt.legend()
    plt.show()

    return float(len(xlist_inside) / iteration*4)
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(Monte_Carlo())

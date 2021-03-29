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
    values = np.ndarray([3,2,5])
    number = 1,2
    for i in range(3):
        s

    return 0

def graph():


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    pass

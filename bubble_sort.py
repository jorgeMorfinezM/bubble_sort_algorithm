# -*- coding: utf-8 -*-

"""Algoritmo de Ordenamiento

Se puede definir un algoritmo de ordenamiento de datos
en una lista con estos datos de forma ascendente o
descendente

Recuerda que en Python podemos intercambiar variables
de forma sencilla: a, b = b, a
"""


def bubble_sort(list_data):
    # Obtenemos la longitud del listado
    list_size = len(list_data)

    for i in range(list_size):
        # inside the cycle, we go through it again. But now until the penultimate element
        for current_index in range(list_size - 1):
            next_element_index = current_index + 1
            # If the current is major that next...
            # Note: for an inverse  sort, change the '>' to '<'
            if list_data[current_index] > list_data[next_element_index]:
                # ... interchange the elements
                list_data[next_element_index], list_data[current_index] = \
                    list_data[current_index], list_data[next_element_index]
    # Do not return anything because the array was modified.


"""
Tests
"""
my_array = [3, 4, 1, 2, 3, 7, 55, 34, 43, 3, 1]
print("Original Array: ", my_array)

bubble_sort(my_array)

print("Sorted Array: ", my_array)

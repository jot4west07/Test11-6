# printear sin salto de linea: print("Mensaje a mostrar", end=" ") por defecto end= /n (el salto de linea)
# se puede cambiar por un espacio (" ") o lo que se desee

# lista_de_elementos = [1, 20, 5, 67, 3, 4, -1]

# #! insertar con posicion
# lista_de_elementos.insert(2, 99)
# #! insertar sin posicion
# lista_de_elementos.append(123)

# #! eliminar un elemento de la lista (suponiendo valores unicos y dato simple)
# try:
#     lista_de_elementos.remove(101)
# except ValueError:
#     print('el elemento a eliminar no esta en la lista')
# if 67 in lista_de_elementos:
#     print('eliminar elemento')
#     lista_de_elementos.remove(67)
# else:
#     print('el elemento a eliminar no esta en la lista')

# #! tamanio
# print(len(lista_de_elementos))

# #! ordenar elementos simples
# lista_de_elementos.sort()
# Una clasificación ascendente simple es muy fácil: simplemente llame a la función sorted(). Retorna una nueva lista ordenada: sorted([5, 2, 3, 1, 4]) retorna una nueva lista ordenada [1, 2, 3, 4, 5]. La funcion .sort() ordena a la misma lista sin crear una nueva.
# Otra diferencia es que el método list.sort() solo aplica para las listas. En contraste, la función sorted() acepta cualquier iterable: sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
#                           [1, 2, 3, 4, 5]
  

# #! busqueda elementos simples
# try:
#     print('posicion', lista_de_elementos.index(20)) index() busca el argumento pasado ej: index("precio") y devuele su posicion como un entero ej: 3
# except ValueError:
#     print('el elemento que busca no esta en la lista')

# #! barrido
# print("Listado")
# for elemento in lista_de_elementos:
#     print(elemento)

# personajes_star_wars = [
#     {'nombre': 'Luke Skywalker', 'especie': 'Humano', 'altura': 172},
#     {'nombre': 'Princesa Leia', 'especie': 'Humano', 'altura': 150},
#     {'nombre': 'Han Solo', 'especie': 'Humano', 'altura': 180},
#     {'nombre': 'Darth Vader', 'especie': 'Humano', 'altura': 202},
#     {'nombre': 'Yoda', 'especie': 'Desconocida', 'altura': 66},
#     {'nombre': 'Obi-Wan Kenobi', 'especie': 'Humano', 'altura': 182},
#     {'nombre': 'Chewbacca', 'especie': 'Wookiee', 'altura': 228},
#     {'nombre': 'R2-D2', 'especie': 'Droide', 'altura': 96},
#     {'nombre': 'C-3PO', 'especie': 'Droide', 'altura': 167},
#     {'nombre': 'Padmé Amidala', 'especie': 'Humano', 'altura': 165}
# ]

# nuevo_personaje = {'nombre': 'Boba Fett', 'especie': 'Humano', 'altura': 178}
#! insertar con posicion
# personajes_star_wars.insert(8, nuevo_personaje)
#! insertar sin posicion
# nuevo_personaje_2 = {'nombre': 'Mace Windu', 'especie': 'Humano', 'altura': 190}
# personajes_star_wars.append(nuevo_personaje_2)

#! tamanio
# print(len(personajes_star_wars))

#! criterios de orden
def by_name(item):
    return item['name']

def by_temp(item):
    return item['temp']

def by_hegiht(item):
    return item['altura']

def by_house(item):
    return item['casa_comic']+item['nombre']

def by_species(item):
    return item['species']
#! ordenar elementos simples
# personajes_star_wars.sort(key=by_name)

#! busqueda elementos simples
# buscado = 'Yoda'
# criterio = 'nombre'

def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

# print(f'Yoda esta en la posicion {search(personajes_star_wars, criterio, buscado)}')

#! eliminar un elemento de la lista
def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

# eliminar = 'R2-D2'
# result_delete = remove(personajes_star_wars, criterio, eliminar)
# print(f'Eliminar {eliminar} resultado: {result_delete}')
#! barrido
def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values): # enumerate() devuelve una tupla (posicion, elemento)
        print(index, elemento)
    print()

def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento['nombre']) # elemento['nombre'] nombre es la key en el diccionario
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(elemento['sublist']):
            print('    ', second_index, second_element)
    print()

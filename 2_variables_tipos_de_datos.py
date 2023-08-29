# Texto
texto: str = "Hello World"
print(type(texto))

# Numeric
numero_entero: int = 10
print(type(numero_entero))

numero_decimal: float = 10
print(type(numero_decimal))

numero_complejo: complex = complex(10)
print(type(numero_complejo))

# Secuencia

listas_1: list = []  # No recomendable
print(type(listas_1))

listas_2: list = list()
print(type(listas_1))

# Agregar elementos a la lista
listas_2.append(1)
listas_2.append('dos')
listas_2.append(3)
listas_2.append(1)

print(listas_2)
print(listas_2[1])
listas_2[1] = 12

# Remover elementos
print('Eliminando')

del listas_2[0]  # Elimina
print(listas_2)

item_uno = listas_2.pop(1)  # Retorna y elimina
print(listas_2)
print('Item 1: ', item_uno)

# Tuplas
tupla_numeros: tuple = ((('R', 'G', 'B'), (1, 3, 0)), (hex(123), 2), (3, 4))
print(type(tupla_numeros))
print(tupla_numeros)

# Range

rango_de_uno_en_uno_desde_uno_hasta_diez = range(1, 11, 1)
# rango_de_uno_en_uno_desde_uno_hasta_diez = range(10)

print(type(rango_de_uno_en_uno_desde_uno_hasta_diez))

rango_de_dos_en_dos_desde_cuatro_hasta_diez = range(4, 10, 2)

for i in rango_de_uno_en_uno_desde_uno_hasta_diez:
    print(i, end=',')
print()
saludo_peruano = 'Habla causa pe'
for letra in saludo_peruano:
    print(letra)

for letra in reversed(saludo_peruano):
    print(letra)

# Diccionarios

diccionario_espaniol: dict = {'Key': 'Value',
                              'KKey': {
                                  'KList': [{'clave':'valorKlist'}, 'a'] }
                              }
print(type(diccionario_espaniol))

print(diccionario_espaniol['KKey']['KList'][0]['clave'])
diccionario_espaniol['KKey']['KList'][0]['clave'] = 100
print(diccionario_espaniol['KKey']['KList'][0]['clave'])
del diccionario_espaniol['KKey']['KList'][0]['clave']
print(diccionario_espaniol)

# Sets
set_numerico :set = set()
set_numerico.add(1)
set_numerico.add(1)
print(type(set_numerico))
set_numerico.add(1)
set_numerico.add(1)
set_numerico.add(2)
set_numerico.add(1)
print(set_numerico)

lista_numeros_repetidos :list = list()
lista_numeros_repetidos.append(3)
lista_numeros_repetidos.append(2)
lista_numeros_repetidos.append(3)
lista_numeros_repetidos.append(2)
lista_numeros_repetidos.append(1)

print(lista_numeros_repetidos)

set_from_list :set = set(lista_numeros_repetidos)
print(set_from_list)

# Booleanos
ella_me_ama = False # :(
ella_me_ama = True  # :D

print(not ella_me_ama)
print(type(ella_me_ama))

# None

nietchze = None

# _

(_ , b) = ('2021', 2022)
print(_, b)

# operators

a = 1
b = 2
suma                = a + b
resta               = a - b
multipliacion       = a * b
division            = a / b
resto               = a % b
potencia            = a ** b
division_enteros    = a // b # redondea

# Asignacion y operación
a += 1
a = a + 1

a -= 1
a = a + 1


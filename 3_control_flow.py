# Operador de asignacion
my_var:str = 'texto'
# Operadores de comparacion
mayor: bool = 3 > 2
mayor_igual: bool = 1 >= 2

menor: bool = 1 < 2
menor_igual: bool = 1 <= 2

# Operadores booleanos (and, or, not)

and_operator :bool = mayor and mayor # & -> true
print(and_operator)

or_operator :bool = mayor or mayor # |
print(or_operator)

not_operator :bool = not True # !
print(not_operator)


# If statements (if, else, elif)

http_status_code :int = 201

if (http_status_code == 200):
    print('Es 200!')

if (http_status_code == 200):
    print('Es 200!')
else:
    print('Lanzar excepcion')

if (http_status_code == 200):
    print('Es 200!')
elif (http_status_code == 201):
    print('Es 201!')
else:
    print('Lanzar excepcion')

# Ternarios
print('*'*12)
http_status_code:int = 200

#if (http_status_code == 200):
#    print('Es 200!')

mensaje = 'Es 200' if (http_status_code == 200) else 'Es otro valor'
print(mensaje)

# Switch (match, case, _)
print('*'*12)
http_status_code :int = 1000
_ = 1000
match(http_status_code):
    case 200:
      print('Es switch 200')
    case 400:
        print('Es switch 400')
    case 201:
        print('Es switch 201')
    case _:
        print('default')

# While, break, continue
print('*'*30)

anios = 2000
while(anios <= 2023):
    print('Año: {}'.format(anios))
    if (anios == 2019):
        break
    anios+=1

print('despues del while (break)')

anios = 2000
while(anios <= 2023):
    anios+=1
    if (anios == 2019):
        continue
    print('Año: {}'.format(anios))

print('despues del while (continue)')

# For, for else
print('*'*21)

saludo_peruano = 'AZ'
for letra in saludo_peruano:
    print(letra)

for letra in range(1, 10+1, 1):
    print(letra)


# def, args, return, name ands position
def multiplicar(a:float, b:float) -> float:
    resultado:float = a * b
    return resultado

resultado = multiplicar(1 , 10)
resultado = multiplicar(b=10, a=1)
print('Resultado: {}'.format(resultado))

# Scopes (local, global)

print('*'*30)
def sumar(a, b):
    resultado_scope_local = a + b
    return resultado_scope_local

resultado_scope_global = sumar(1, 3)

# Global statement
def restar(a, b):
    global resultado_scope_local_resta
    resultado_scope_local_resta = a - b

restar(1, 2)
resultado_scope_local_resta *= 2


# Lambdas (funciones anonimas o sin nombre)
lambda_sumar = lambda a , b : a + b
resultado_suma_lambda = lambda_sumar(1, 2)


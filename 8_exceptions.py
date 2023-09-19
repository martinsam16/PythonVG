def validar_dni(dni:str)->bool:
    valido = dni.isdigit() and len(dni) == 8
    if not(valido):
        raise ValueError("DNI no es válido ❌")

# Sin Excepciones
#dni_ingresado = input("Ingresar DNI: ")
#if  (validar_dni(dni_ingresado)):
#    print("Registrado!")
#else:
#    print("Error en validacion")

# Con Excepciones
#try:
#    dni_ingresado = int(input("Ingresar DNI: "))
#except:
#    print("Except")
#finally: # opcional
#    print("si o si")

# Validacion arrojando excepcion
dni_ingresado = input("Ingresar DNI: ")
validar_dni(dni_ingresado)
print("Registrado!")

# Validacion arrojando excepcion
#dni_ingresado = input("Ingresar DNI: ")
#try:
#    validar_dni(dni_ingresado)
#    print("Registrado!")
#except:
#    print("Algo salió mal")





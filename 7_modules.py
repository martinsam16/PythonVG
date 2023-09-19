# Importar toda la libreria
import aritmetic_module

print(aritmetic_module.sumar(3, 1))
print(aritmetic_module.restar(3, 1))

# Importar solo que necesitamos
from aritmetic_module import sumar

print(sumar(1, 2))

#
import aritmetic_module
import operations_module

print(aritmetic_module.sumar(3, 1))
print(operations_module.sumar(3, 1))

# as = alias
from aritmetic_module import sumar as sumar_aritmetic_module
from operations_module import sumar as sumar_operations_module

# a = 1
# a = 2

print(sumar_aritmetic_module(3, 1))
print(sumar_operations_module(3, 1))

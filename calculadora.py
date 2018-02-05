#!/usr/bin/python3

import sys


try:
    funcion = str(sys.argv[1])
    operando1 = float(sys.argv[2])
    operando2 = float(sys.argv[3])
except IndexError:
    sys.exit("Introduce python calculadora.py funcion operando1 operando2")
except ValueError:
    sys.exit("Introduzca operandos válidos: enteros o float con punto decimal")
if funcion == "sumar":
    res = operando1 + operando2
elif funcion == "restar":
    res = operando1 - operando2
elif funcion == "multiplicar":
    res = operando1 * operando2
elif funcion == "dividir":
    try:    
        res = operando1 / operando2
    except ZeroDivisionError:
        sys.exit("No se puede dividir entre 0.")   
else:
    print("Operaciones permitidas: sumar, restar, multiplicar, dividir")
    res = None
print(res)

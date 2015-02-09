#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

#if len(sys.argv[0:]) != 4:
#    print "Introduce python calculadora.py funcion operando1 operando2 "
try:
    funcion = sys.argv[1]
    operando1 = float(sys.argv[2])
    operando2 = float(sys.argv[3])
    

    if funcion == "sumar":
        res = operando1 + operando2
    elif funcion == "restar":
        res = operando1 - operando2
    elif funcion == "multiplicar":
        res = operando1 * operando2
    elif funcion == "dividir":
        res = operando1 / operando2
    else:
        print "Operaciones permitidas: sumar, restar, multiplicar, dividir"
        res = None
    print res

except IndexError:
    print "Introduce python calculadora.py funcion operando1 operando2"
    sys.exit()
except ValueError:
    print "Introduzca operandos válidos: enteros o float con punto decimal"
    sys.exit()
except ZeroDivisionError:
    print "No se puede dividir entre 0."
    sys.exit()

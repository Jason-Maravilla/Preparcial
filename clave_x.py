import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
num1 = 2
num2 = 4


def suma():
    result = num1 + num2
    return result


"""
***************************************************************
@@ ejercicio 2 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*5 = 40
"""


# start-->
num1 = 2
num2 = 4
num3 = 5


def multiplicacion():
    result = num1 * num2 * num3
    return result


"""
***************************************************************
@@ ejercicio 3 @@
un metodo python que haga la suma de los numeros de la lista
numerosLista = [2,5,4,6,9,12]
"""


# start-->


def sumarLista():
    numerosLista = [2, 5, 4, 6, 9, 12]
    result = 0
    for numeros in numerosLista:
        result += numeros
    return result


"""
***************************************************************
@@ ejercicio 4 @@
colocar este proyecto en github
colocar aca debajo la url
enviar la url al correo balbino_a@hotmail.com
"""


# github url-->
def getGithubUrl():
    return "https://github.com/Jason-Maravilla/Preparcial.git"

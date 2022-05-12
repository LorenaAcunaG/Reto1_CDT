#Reto1: cálculo de intereses de un CDT

import abc
from posixpath import dirname

# variables fijas
porcentaje_interes = 0.03
porcentaje_penalidad = 0.02

# variables de entrada
id_usuario = input('Escriba el número de identificación del cliente a consultar: ')
dinero_invertido = int(input('Escriba la cantitad de dinero invertida por el cliente: '))
tiempo_cdt = int(input('Escriba la cantidad de tiempo que lleva el cliente con el CDT en meses: '))

# definición de función CDT para cálculo de valor total a entregar al cliente
def CDT(a, b, c, d):
    if tiempo_cdt > 2:
        valor_intereses = (a * b * c)/12
        valor_total = a + valor_intereses
               
    else:
        valor_perdido = a * d
        valor_total = a - valor_perdido

    return valor_total

print ('Para el usuario:',id_usuario,'la cantidad de dinero a recibir, según el monto inicial de:',dinero_invertido,'para un tiempo de:',tiempo_cdt,'meses es:',CDT(dinero_invertido, porcentaje_interes, 
tiempo_cdt, porcentaje_penalidad),'pesos')
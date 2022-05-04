#Reto1: cálculo de intereses de un CDT

porcentaje_interes = 0.03
porcentaje_penalidad = 0.02

# variables de entrada
id_usuario = input('Escriba el número de identificación del cliente a consultar: ')
dinero_invertido = int(input('Escriba la cantitad de dinero invertida por el cliente: '))
tiempo_cdt = int(input('Escriba la cantidad de tiempo que lleva el cliente con el CDT en meses: '))

def CDT():
    if tiempo_cdt > 2:
        valor_intereses = (dinero_invertido * porcentaje_interes * tiempo_cdt)/12
        valor_total = valor_intereses + dinero_invertido
               
    else:
        valor_perdido = dinero_invertido * porcentaje_penalidad
        valor_total = dinero_invertido - valor_perdido

    return valor_total

print ('Para el usuario:',id_usuario,'la cantidad de dienro a recibir, según el monto inicial de:',dinero_invertido,'para un tiempo de:',tiempo_cdt,'meses es:',CDT(),'pesos')
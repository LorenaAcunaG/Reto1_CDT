listaContable= [                     
[6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],         
[6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],                    
[6591, ("7812", 2, 11.99), ("9652",11,18.99)], 
] 


'''Requerimiento. Para el desarrollo de esta implementación, el programador debe permitir introducir un registro de ordenes desde una lista de tuplas y a través de la función “map”, “reduce” y “lambda” desarrollar las funciones necesarias para el siguiente calculo:
• Sumar el total de cada tupla de cada lista
• Sumar los totales de todas las tuplas de toda la lista
• Suma el incremento si la compra no llega a un mínima de 600.000 pesos, en este caso, se incrementa 25.000 pesos al total de la compra.

La factura <número> tiene un total en pesos de <cantidad>'''

def ordenes(rutinaContable):
    from functools import reduce
    listaOrden = list(map(lambda x: x[0],rutinaContable))
    listaTuplas = list(map(lambda x: x[1:],rutinaContable))

    cadena = []
    for i in listaTuplas:
        totalTupla1 = list(map(lambda x: x[1]*x[2],i))
        totalOrden1 = reduce(lambda x,y:x+y, totalTupla1)
        cadena.append(totalOrden1)
    
    def incremento(a):
        if a<600000:
            return a+25000
        else:
            return a
    
    total = list(map(incremento,cadena))
    textoFinal = ''
    contador = 0
    for i, j in zip(listaOrden, total):        
        texto = f"La factura {i} "+ "tiene un total en pesos de {:,.2f}".format(j)
        contador += 1
        if contador < len(total):
            textoFinal += texto +"\n"
        else:
            textoFinal += texto
        
    print('------------------------ Inicio Registro diario ---------------------------------')
    print (textoFinal)
    print('-------------------------- Fin Registro diario ----------------------------------')
    

ordenes(listaContable)
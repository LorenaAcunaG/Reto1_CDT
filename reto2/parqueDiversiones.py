
# Parque de diversiones "AVENTURAS EXTREMAS"
id_cliente = 1
nombre = "Lorena"
edad = 8
primer_ingreso = True
 
 
usuario = {
    "id_cliente":id_cliente,
    "nombre":nombre,
    "edad":edad,
    "primer_ingreso":primer_ingreso}

def cliente (informacion:dict):

    nombre = informacion["nombre"]
    edad = informacion["edad"]
    primer_ingreso = informacion["primer_ingreso"]
        
    if edad>18:
        apto = True
        atraccion = "X-Treme"
        if primer_ingreso == True:
            descuento = 20000*0.05
            total_boleta = 20000 - descuento
        else:
            total_boleta = 20000
    elif edad>=15 and edad<=18:
        apto = True
        atraccion = "Carros chocones"
        if primer_ingreso == True:
            descuento = 5000*0.07
            total_boleta = 5000 - descuento
        else:
            total_boleta = 5000

    elif edad>=7 and edad<15:
        apto = True
        atraccion = "Sillas voladoras"
        if primer_ingreso == True:
            descuento = 10000*0.05
            total_boleta = 10000 - descuento
        else:
            total_boleta = 10000
    else:
        apto = False
        atraccion = "N/A"
        total_boleta = "N/A"

    atraccion_ok = {
        "nombre":nombre,
        "edad":edad,
        "atraccion":atraccion,
        "apto":apto,
        "primer_ingreso":primer_ingreso,
        "total_boleta":total_boleta
         }

    return atraccion_ok

print (cliente(usuario))


# Parque de diversiones "AVENTURAS EXTREMAS"
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


dic1={"id_cliente":1,"nombre":"Johana Fernandez","edad":20,"primer_ingreso":True}
dic2={"id_cliente":1,"nombre":"Johana Fernandez","edad":20,"primer_ingreso":False}
dic3={"id_cliente":2,"nombre":"Gloria Suarez","edad":3,"primer_ingreso":True}
dic4={"id_cliente":3,"nombre":"Tatiana Suarez","edad":17,"primer_ingreso":True}
dic5={"id_cliente":3,"nombre":"Tatiana Suarez","edad":17,"primer_ingreso":False}
dic6={"id_cliente":4,"nombre":"Tatiana Ruiz","edad":8,"primer_ingreso":True}
dic7={"id_cliente":4,"nombre":"Tatiana Ruiz","edad":8,"primer_ingreso":False}

print (cliente(dic1))
print (cliente(dic2))
print (cliente(dic3))
print (cliente(dic4))
print (cliente(dic5))
print (cliente(dic6))
print (cliente(dic7))
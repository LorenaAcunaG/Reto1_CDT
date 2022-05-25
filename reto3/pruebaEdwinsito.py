listaTuplas = [
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]

def AutoPartes (ventas: list):
    dicVentas={}
    j=1
    for i in ventas:
        dicVentas[f"venta{j}"]=i
        j+=1
    return dicVentas
    
def consultaRegistro(ventas, idProducto):
    respuestaFinal=""
    comprobador = False
    for i in ventas.values():
        if idProducto==i[0]:                     
            resultado=f"Producto consultado : {i[0]}  Descripción  {i[1]}  #Parte  {i[2]}  Cantidad vendida  {i[3]}  Stock  {i[4]}  Comprador {i[5]}  Documento  {i[6]}  Fecha Venta  {i[7]}"
            comprobador =True
            respuestaFinal+= resultado+"\n"
  
    if comprobador==True:
        print(respuestaFinal)
    else:
        print("No hay registro de venta de ese producto")

(consultaRegistro(AutoPartes(listaTuplas), 2001))
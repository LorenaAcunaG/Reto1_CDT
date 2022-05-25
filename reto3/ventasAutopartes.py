def AutoPartes (ventas: list):

    dicVentas={}
    j=1
    for i in ventas:
        dicVentas[f"venta{j}"]=i
        j+=1
    return dicVentas
    
def consultaRegistro(ventas, idProducto):
    textoFinal=""
    for i in ventas.values():
        if idProducto==i[0]:                     
            resultado=f"Producto consultado : {i[0]}  Descripción  {i[1]}  #Parte  {i[2]}  Cantidad vendida  {i[3]}  Stock  {i[4]}  Comprador {i[5]}  Documento  {i[6]}  Fecha Venta  {i[7]}"
            textoFinal += resultado+"\n"
  
    if textoFinal!="":
        print(textoFinal)
    else:
        print("No hay registro de venta de ese producto")

consultaRegistro(AutoPartes([
    (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
    (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]), 9852)
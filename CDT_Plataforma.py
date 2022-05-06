#Reto1: cálculo de intereses de un CDT
# definición de función CDT para cálculo de valor total a entregar al cliente
def CDT(usuario: str, capital: int, tiempo: int):
    if tiempo > 2:
        valor_intereses = (capital * 0.03 * tiempo)/12
        valor_total = capital + valor_intereses
               
    else:
        valor_perdido = capital * 0.02
        valor_total = capital - valor_perdido

    return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}")


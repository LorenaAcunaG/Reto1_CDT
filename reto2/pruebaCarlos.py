def cliente (informacion:dict)-> dict:


    dictionary = {
        "nombre":informacion["nombre"],
        "edad" : informacion["edad"],
        "atraccion" : "N/A",
        "apto" : False,
        "primer_ingreso" : informacion["primer_ingreso"],
        "total_boleta" : "N/A",
    }

    #X-treme

    if informacion["edad"]>18:
        boleta = (20000)
        dictionary["apto"]= True

        if informacion["primer_ingreso"]==True:
            
            dictionary["atraccion"] = "X-Treme"
            dictionary["total_boleta"] = boleta - (boleta*0.05)
            return dictionary
        else:
            
            dictionary["atraccion"] = "X-Treme"
            dictionary["total_boleta"] = boleta 
            return dictionary
    
    
    if informacion["edad"] >= 15 and informacion["edad"] <=18:
        boleta = (5000)
        dictionary["apto"]= True

        if informacion["primer_ingreso"]==True:
            
            dictionary["atraccion"] = "Carroschocones"
            dictionary["total_boleta"] = boleta - (boleta*0.07)
            return dictionary
        else:
            
            dictionary["atraccion"] = "Carroschocones"
            dictionary["total_boleta"] = boleta 
            return dictionary
    

    if informacion["edad"] >= 7 and informacion["edad"] < 15:
        boleta = (10000)
        dictionary["apto"]= True

        if informacion["primer_ingreso"]==True:
            
            dictionary["atraccion"] = "Sillas voladoras"
            dictionary["total_boleta"] = boleta - (boleta*0.05)
            return dictionary
        else:
            
            dictionary["atraccion"] = "Sillas voladoras"
            dictionary["total_boleta"] = boleta 
            return dictionary
    

    return dictionary
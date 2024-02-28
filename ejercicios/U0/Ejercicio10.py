def mayorYmenor(tabla):
    mayor = menor = tabla[0]
    for cadena in tabla:
        if len(cadena) > len(mayor):
            mayor = cadena
        elif len(cadena) < len(menor):
            menor = cadena

    print("String con mayor longitud:", mayor)
    print("String con menor longitud:", menor)

tabla_de_strings = ["Juan", "Jorge", "Roberto", "Ana", "Pepe"]
mayorYmenor(tabla_de_strings)
def indexContains(tabla, cadena):
    if cadena in tabla:
        print("'",cadena, "' esta en la posición", tabla.index(cadena))
    else:
        print(-1)

indexContains(['juan', 'jorge', 'liam', 'alex', 'gorka'], '')
indexContains(['juan', 'jorge', 'liam', 'alex', 'gorka'], 'liam')
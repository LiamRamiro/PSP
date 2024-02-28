def salario():
    salarios = [[700, 900, 1300], [1000, 950, 1080], [1300, 930, 1200]]
    empleados = ['Javier María', 'Antonio Muñoz', 'Isabel Allende']

    for i in range(len(empleados)):
        total = sum(salarios[i])
        print(empleados[i], '->', ' + '.join(map(str, salarios[i])), '=', total, '€')

salario()
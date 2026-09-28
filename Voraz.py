def voraz(monto):
    denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05]
    cantidades = []

    monto = int(monto * 100)

    for denominacion in denominaciones:
        valor = int(denominacion * 100)
        cantidad = monto // valor
        cantidades.append(cantidad)
        monto = monto % valor

    return cantidades


monto = 179.45

respuesta = voraz(monto)

denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05]

for posicion in range(len(denominaciones)):
    if respuesta[posicion] > 0:
        print(respuesta[posicion], "de S/", denominaciones[posicion])
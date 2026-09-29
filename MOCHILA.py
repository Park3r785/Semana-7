class Caja:
    def __init__(self, nombre, peso, precio):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio

    def precio_por_kg(self):
        return self.precio / self.peso


def mochila(cajas, capacidad):

    # Ordenar de mayor a menor precio por kg
    for posicion_caja in range(len(cajas)):
        for siguiente_caja in range(posicion_caja + 1, len(cajas)):

            if cajas[posicion_caja].precio_por_kg() < cajas[siguiente_caja].precio_por_kg():

                aux = cajas[posicion_caja]
                cajas[posicion_caja] = cajas[siguiente_caja]
                cajas[siguiente_caja] = aux

    peso_total = 0
    ganancia_total = 0

    print("\nCajas seleccionadas:")

    # Método voraz
    for caja in cajas:

        if peso_total + caja.peso <= capacidad:

            peso_llevado = caja.peso
            ganancia = caja.precio
            porcentaje = 100

        else:

            peso_disponible = capacidad - peso_total

            porcentaje = (peso_disponible / caja.peso) * 100
            peso_llevado = peso_disponible
            ganancia = caja.precio * (porcentaje / 100)

        peso_total = peso_total + peso_llevado
        ganancia_total = ganancia_total + ganancia

        print(f"Caja {caja.nombre}: {porcentaje:.1f}% - "
              f"{peso_llevado:.2f} kg - S/ {ganancia:.2f}")

        if peso_total == capacidad:
            break

    print()
    print(f"Peso total: {peso_total:.2f} kg")
    print(f"Ganancia total: S/ {ganancia_total:.2f}")


cajas = [
    Caja("A", 10, 4),
    Caja("B", 4, 3),
    Caja("C", 7, 3),
    Caja("D", 5, 2),
    Caja("E", 3, 1),
    Caja("F", 3, 2),
    Caja("G", 2, 1.8),
    Caja("H", 3, 3)
]

# Pedir el peso máximo
m = float(input("Ingrese el peso máximo de la mochila (kg): "))

mochila(cajas, m)
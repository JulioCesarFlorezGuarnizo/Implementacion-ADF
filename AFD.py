

import sys


class AFD:
    def __init__(self):
        # Definición formal de la 5-tupla
        self.Q = {"q0", "q1", "qd"}
        self.Sigma = {"0", "1"}
        self.q0 = "q0"
        self.F = {"q1"}

        # Función de transición δ : Q × Σ → Q
        self.delta = {
            ("q0", "0"): "q1",
            ("q0", "1"): "qd",
            ("q1", "0"): "q1",
            ("q1", "1"): "q1",
            ("qd", "0"): "qd",
            ("qd", "1"): "qd",
        }

    def procesar(self, cadena):
        estado_actual = self.q0

        if cadena == "":
            return False  # ε no pertenece al lenguaje

        for simbolo in cadena:
            if simbolo not in self.Sigma:
                return False  # símbolo fuera del alfabeto

            estado_actual = self.delta[(estado_actual, simbolo)]

        return estado_actual in self.F


def main():
    if len(sys.argv) != 2:
        print("Uso: python afd.py <archivo.txt>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]

    try:
        with open(nombre_archivo, "r") as archivo:
            afd = AFD()

            for linea in archivo:
                cadena = linea.strip()

                if cadena == "":
                    continue

                if afd.procesar(cadena):
                    print(f"{cadena} : ACEPTA")
                else:
                    print(f"{cadena} : NO ACEPTA")

    except FileNotFoundError:
        print("Error: archivo no encontrado.")
        sys.exit(1)


if __name__ == "__main__":
    main()

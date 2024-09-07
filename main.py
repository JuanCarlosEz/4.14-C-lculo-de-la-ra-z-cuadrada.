class RaizCuadrada:
    def __init__(self, numero, tolerancia=1e-6):

        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        self.numero = numero
        self.tolerancia = tolerancia

    def calcular(self):

        x = self.numero / 2.0


        while True:
            nuevo_x = (x + self.numero / x)/2
            if abs(nuevo_x - x) < self.tolerancia:
                break
            x = nuevo_x

        return nuevo_x


try:
    numero = float(input("Ingrese el número del cual quiere calcular la raíz cuadrada: "))

    raiz = RaizCuadrada(numero)

    resultado = raiz.calcular()
    print(f"La raíz cuadrada aproximada de {numero} es: {resultado:}")

except ValueError as e:
    print(e)

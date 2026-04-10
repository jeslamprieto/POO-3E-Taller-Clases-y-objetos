## Clase TarjetaCredito
class TarjetaCredito:
    def __init__(self, numero):
        self.numero = numero

    @staticmethod
    def validar_tarjeta(numero):
        digits = [int(d) for d in str(numero)]
        digits.reverse()
        for i in range(1, len(digits), 2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0

tarjeta1 = TarjetaCredito(4532015112830366)
tarjeta2 = TarjetaCredito(1234567890123456)

print(f"Tarjeta 4532015112830366 es valida: {TarjetaCredito.validar_tarjeta(tarjeta1.numero)}")
print(f"Tarjeta 1234567890123456 es valida: {TarjetaCredito.validar_tarjeta(tarjeta2.numero)}")
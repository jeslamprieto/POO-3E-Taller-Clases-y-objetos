## Clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            raise ValueError("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            raise ValueError("Fondos insuficientes o monto invalido.")

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular


## Clase CuentaAhorro
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, interes_anual=0):
        super().__init__(titular, saldo_inicial)
        self.__interes_anual = interes_anual

    def get_interes(self):
        return self.__interes_anual

    def aplicar_interes(self):
        interes = self.consultar_saldo() * (self.__interes_anual / 100)
        self.depositar(interes)
        print(f"Interes aplicado. Nuevo saldo: ${self.consultar_saldo():.2f}")


cuenta = CuentaAhorro("Pepito", 1000, 5)

print(f"Titular: {cuenta.consultar_titular()}")
print(f"Saldo inicial: ${cuenta.consultar_saldo()}")
print(f"Interes anual: {cuenta.get_interes()}%")

cuenta.aplicar_interes()

cuenta.depositar(500)
print(f"Saldo despues de depositar $500: ${cuenta.consultar_saldo()}")

cuenta.retirar(200)
print(f"Saldo despues de retirar $200: ${cuenta.consultar_saldo()}")
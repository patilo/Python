# cuenta.py

class CuentaBancaria:
    """Clase que modela una cuenta bancaria con saldo y operaciones básicas."""

    # CONSTRUCTOR: Define el estado inicial del objeto
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        # Atributo privado: el saldo es el estado que el objeto mantiene
        self._saldo = saldo_inicial
        print(f"Cuenta creada para {self.titular} con saldo inicial: ${self._saldo:,.2f}")

    # MÉTODO: Consulta de Saldo
    def consultar_saldo(self):
        """Devuelve el saldo actual de la cuenta."""
        return self._saldo

    # MÉTODO: Depósito
    def depositar(self, cantidad):
        """Añade una cantidad al saldo."""
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito de ${cantidad:,.2f} realizado. Nuevo saldo: ${self._saldo:,.2f}")
            return True
        else:
            print("Error: La cantidad a depositar debe ser positiva.")
            return False

    # MÉTODO: Retiro
    def retirar(self, cantidad):
        """Resta una cantidad al saldo, verificando fondos."""
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser positiva.")
            return False
        if cantidad > self._saldo:
            print("Error: Fondos insuficientes para realizar el retiro.")
            return False

        # Actualiza el estado del objeto
        self._saldo -= cantidad
        print(f"Retiro de ${cantidad:,.2f} realizado. Nuevo saldo: ${self._saldo:,.2f}")
        return True

    # MÉTODO: Transferencia
    def transferir(self, otra_cuenta, cantidad):
        """Transfiere dinero a otra instancia de CuentaBancaria."""
        if cantidad <= 0:
            print("Error de Transferencia: La cantidad debe ser positiva.")
            return False

        # 1. Intentar Retirar de esta cuenta
        if self.retirar(cantidad):
            # 2. Si el retiro es exitoso, depositar en la otra cuenta
            otra_cuenta.depositar(cantidad)
            print(f"Transferencia de ${cantidad:,.2f} a la cuenta de {otra_cuenta.titular} exitosa.")
            return True
        else:
            print("Transferencia fallida: Fondos insuficientes o error en el retiro.")
            # El retiro ya imprime el mensaje de error apropiado
            return False
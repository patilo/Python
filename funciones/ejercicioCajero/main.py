# main.py

# Importamos la clase CuentaBancaria para poder crear objetos
from cuenta import CuentaBancaria


def main():
    print("🏦 CAJERO AUTOMÁTICO 🏦")
    print("--------------------------------------")

    # 1. CREACIÓN DE OBJETOS (Instancias de la Clase)
    mi_cuenta = CuentaBancaria("Alice Smith", 500.00)
    cuenta_destino = CuentaBancaria("Bob Johnson", 100.00)

    print("\n--- 1. CONSULTA INICIAL ---")
    # Llamamos al método de consulta
    saldo_alice = mi_cuenta.consultar_saldo()
    print(f"El saldo de Alice es: ${saldo_alice:,.2f}")
    print(f"El saldo de Bob es: ${cuenta_destino.consultar_saldo():,.2f}")

    print("\n--- 2. DEPÓSITO ---")
    mi_cuenta.depositar(250.75)  # Aumenta el estado de mi_cuenta

    print("\n--- 3. RETIRO ---")
    mi_cuenta.retirar(100.00)  # Reduce el estado de mi_cuenta
    mi_cuenta.retirar(800.00)  # Intento de retiro fallido (fondos insuficientes)

    print("\n--- 4. TRANSFERENCIA ---")
    # Transferir 300.75 de Alice a Bob
    mi_cuenta.transferir(cuenta_destino, 300.75)

    print("\n--- 5. CONSULTA FINAL ---")
    # Verificación final de los saldos después de todas las operaciones
    print(f"Saldo FINAL de Alice: ${mi_cuenta.consultar_saldo():,.2f}")
    print(f"Saldo FINAL de Bob: ${cuenta_destino.consultar_saldo():,.2f}")


if __name__ == "__main__":
    main()
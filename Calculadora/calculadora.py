"""Calculadora modular.

Este script usa los submódulos `Suma.suma` y `Resta.resta`.
Proporciona un menú interactivo para elegir operación, pedir dos
números y mostrar el resultado.
"""

from Suma.suma import sumar
from Resta.resta import restar


def pedir_numero(prompt: str) -> float:
	while True:
		try:
			texto = input(prompt).strip()
			return float(texto)
		except ValueError:
			print("Entrada no válida. Por favor ingresa un número.")


def mostrar_menu() -> None:
	print("\n=== Calculadora ===")
	print("1) Sumar")
	print("2) Restar")
	print("0) Salir")


def main() -> None:
	while True:
		mostrar_menu()
		opcion = input("Elige una opción: ").strip()

		if opcion == "0":
			print("Saliendo. ¡Hasta luego!")
			break

		if opcion not in {"1", "2"}:
			print("Opción no válida. Intenta de nuevo.")
			continue

		a = pedir_numero("Ingrese el primer número: ")
		b = pedir_numero("Ingrese el segundo número: ")

		if opcion == "1":
			resultado = sumar(a, b)
			oper = "sumar"
		else:
			resultado = restar(a, b)
			oper = "restar"

		print(f"Resultado de {oper}({a}, {b}) = {resultado}")


if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print("\nInterrumpido. Saliendo.")

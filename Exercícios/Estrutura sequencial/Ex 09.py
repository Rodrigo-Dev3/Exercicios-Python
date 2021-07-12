"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

numero1 = int(input("Digite o primeiro número -> "))
numero2 = int(input("Digite o segundo número -> "))
numero3 = float(input("Digite o terceiro número -> "))

print(f"O produto do dobro do primeiro com metade do segundo é -> {(numero1 * 2) * (numero2 / 2)}")

print(f"A soma do triplo do primeiro com o terceiro é -> {(numero1 * 3) + numero3}")

print(f"O terceiro elevado ao cubo é -> {numero3 ** 3}")

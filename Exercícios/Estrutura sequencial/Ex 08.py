"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

cel = float(input("Digite o valor em graus Celcius para a conversão: "))

far = cel * 1.8 + 32

print(f"{cel}ºC é o equivalente a {far:.2f} graus Fahrenheit.")
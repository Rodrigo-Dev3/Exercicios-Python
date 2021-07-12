"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

salarioHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas  = int(input("Quantas horas você trabalhou neste mês? "))

salarioMes = salarioHora * horasTrabalhadas

print(f"Você receberá um salário de R$ {salarioMes} neste mês.")
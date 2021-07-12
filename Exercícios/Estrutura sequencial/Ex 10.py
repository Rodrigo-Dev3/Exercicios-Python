"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

IMC = Peso ÷ (Altura × Altura)"""

altura = float(input("Digite a sua altura -> "))

pergunta = str(input("Digite o seu sexo (H/M) -> "))
if pergunta in 'Hh':
    pesoIdealH  = (72.7 * altura) - 58
    print(f"O seu peso idela é -> {pesoIdealH:.2f}")

elif pergunta in 'Mm':
    pesoIdealM = (62.1 * altura) - 44.7
    print(f"O seu peso idel é -> {pesoIdealM:.2f}")

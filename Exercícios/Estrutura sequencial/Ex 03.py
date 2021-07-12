"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

nota1 = float(input("Digite a primeira nota do aluno --> "))
nota2 = float(input("Digite a segunda nota do aluno --> "))
nota3 = float(input("Digite a terceira nota do aluno --> "))

media = (nota1 + nota2 + nota3) / 3

print(f"A media do aluno é {media:.2f}")

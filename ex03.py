"""Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias."""

ano = int(input("Digite a tua idade: "))
mes = int(input("Digite o mês em nasceste: "))
dia = int(input("Digite o teu dia de nascimento: "))

idade_dias = (ano * 365) + (mes * 30) + dia
print("A idade dessa pessoa em dias é:", idade_dias)

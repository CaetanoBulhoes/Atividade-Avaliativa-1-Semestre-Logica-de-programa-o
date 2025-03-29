# 14. Escreva um programa que receba o valor do salário de um funcionário e o valor do salário mínimo. Calcule e mostre quantos salários mínimos ganha esse funcionário.

salario = float(input("Digite seu salário:"))
valor_salário_minimo = float(1509)

quantidade = salario / valor_salário_minimo 

print(f"Seu salário é de R${salario :.2f}, isso equivale a {quantidade :.1f} salarios minimos.")
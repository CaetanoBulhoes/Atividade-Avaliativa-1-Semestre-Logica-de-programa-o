# 15. Escreva um algoritmo que receba o salário de um funcionário, calcule e imprima o valor do imposto de renda a ser pago, sabendo que o imposto equivale a 5% do salário.

salario = float(input("Digite seu salário:"))

imposto = salario * 0.05

desconto = salario - imposto

print(f"O imposto irá descontar R${imposto} do seu salário, ficando com R${desconto} no final. ")

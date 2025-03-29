# 19. Sabe-se que o quilowatt de energia custa 2% do salário mínimo. Escreva um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência. Calcule e imprima:
# • o valor, em reais, de cada quilowatt;
# • o valor, em reais, a ser pago por essa residência;
# • o novo valor à ser pago por essa residência, se for dado um desconto de 15%.

salario = 1.518
QuantidadeKw = int(input("Digite quantos quilowatts foram utilizados esse mês: "))

kw = salario * 0.02

valor = kw * QuantidadeKw

valordesconto = valor * 0.15

print("*" * 60)
print(f"Cada Quilowatt equivale: R${kw:.2f}")
print(f"O valor a ser pago será: R${valor:.2f}")
print(f"Caso receba um desconto de 15%, o novo valor será: R${valordesconto:.2f}")
print("*" * 60)

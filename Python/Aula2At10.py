# 10. Escreva um programa para calcular a média de quatro números.

quantidade = 4
soma = 0

for cont in range (quantidade):
    num = float(input("Digite um númer: "))
    num += 0
    soma += num

media = soma / quantidade

print(f"A média dos 4 números são: {media}")

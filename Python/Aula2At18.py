# 18. Escreva um algoritmo que receba o valor de um produto, e para cada R$ 100,00 dê um desconto de 0,05%.

valor = float(input("Digite o preço total: "))

if valor < 100:
    print(f"Você vai pagar R${valor:.2f}!")

elif valor >= 100:
    divisão =int(valor / 100)
    desconto = 0.05 * divisão
    desconto_preco = desconto * valor
    desconto_total = valor - desconto_preco

    print(f"Você recebeu um desconto de {desconto * 100:.0f}% nas suas compras.\nTendo agora que pagar R${desconto_total:.2f}!")



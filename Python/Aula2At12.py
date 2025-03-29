# 12. Elabore um programa para calcular e mostrar o valor da conversão de uma quantia em dólares para reais. Crie variáveis para guardar o valor da cotação do dólar do dia, o valor em dólares e o valor do resultado da conversão. Use a fórmula:
# quantiaEmReais = quantiaEmDolares * cotacaoDoDolar

dolar = float(input("Digite a quantia em dolarés:"))
real = 5.65

conversão = dolar * real

print(f"O valor de US${dolar:.2f} em reais é: R${conversão:.2f}!")
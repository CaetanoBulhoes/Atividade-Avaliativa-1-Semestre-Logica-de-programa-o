# 11. Elabore um programa que calcule e mostre a taxa de consumo em km/l que um carro tem em um deslocamento. Devem ser criadas variáveis para a distância percorrida (em kilômetros), a quantidade de litros consumidos e o valor da taxa de consumo (em km/l). O cálculo é feito pela fórmula:
# taxaDeConsumo = distancia / litros

distancia = float(input("Digite a distância percorrida:"))
litros = float(input("Digite a quantidade gasta em litros:"))

if litros > distancia:
    print("Isso não pode acontecer")

else:
 TaxaDeConsumo = distancia / litros

 print(f"A taxa foi de: {TaxaDeConsumo :.2f} Km/L ")
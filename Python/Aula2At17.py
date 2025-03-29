# 17. Um trem se locomove há 150 km/h, e funciona por 20 horas por dia. A cada 2.000 km ele deve parar 6 horas para manutenção. Cada manutenção custa R$ 2.000,00 e a cada 3 dias é cobrada uma taxa de R$ 5.000,00 de uso da ferrovia. Escreva em um algoritmo que receba o número de dias e escreva na tela um relatório, com o número de kilômetros percorridos e manutenções realizadas, assim como o custo total.

dias = int(input("Digite o número de dias: "))
horas = int(dias * 24) 

km = float(150 * horas )

parada = int(km / 2000)

taxa = int(72 / horas)

manutencao = 0
taxa_dinheiro = 0

if km < 2000:
    print("Não tem despesa")
    
elif km >= 2000:
    manutencao = parada * 2000

if horas < 72:
        print("Não tem taxa")
        
elif horas >= 72: 
        taxa_dinheiro = float(taxa * 5000)

total = float (manutencao + taxa_dinheiro)

print(f"{"*" * 50} Relatório {"*" * 50}\n")
print(f"Dias: {dias}")
print(f"Kilometros percorridos: {km:.0f} Km")
print(f"Manuntenção realizadas: {parada}")
print(f"Gastos totais: R${total:.2f}\n")

print("*" * 111)

# 5. Faça um programa que:
# a) Obtenha o valor para a variável HT (horas trabalhadas no mês)
# b) Obtenha o valor para a variável VH (valor hora trabalhada)
# c) Obtenha o valor para a variável PD (percentual de desconto)
# d) Calcule o salário bruto SB HT VH
# e) Calcule o total de desconto TD ==( 100 )*SB
# f) Calcule o salário líquido SL SB TD
# g) Apresente os valores de Horas trabalhadas, Salário Bruto, Desconto, Salário Liquido.

HT = float(input("Digite quantas horas foram trabalhadas:"))
VH = float(input("Digite o valor de hora trabalhada:"))
PD = float(input("DIgite o percentual de desconto:"))

SB =  HT * VH
TD = (PD/100) * SB
SL = SB - TD

print("*" * 60)
print(f"Horas trabalhadas: {HT} horas\nSalário bruto: R${SB:.2f}\nDesconto: R${TD:.2f}\nSalário Liquido: R${SL:.2f}")
print("*" * 60)
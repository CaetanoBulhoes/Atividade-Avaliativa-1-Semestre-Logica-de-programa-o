Algoritmo "semnome"

//Faça um algoritmo que:
//a) Obtenha o valor para a variável HT (horas trabalhadas no mês)
//b) Obtenha o valor para a variável VH (valor hora trabalhada)
//c) Obtenha o valor para a variável PD (percentual de desconto)
//d) Calcule o salário bruto SB HT VH
//e) Calcule o total de desconto TD ==( 100 )*SB
//f) Calcule o salário líquido SL SB TD
g) Apresente os valores de Horas trabalhadas, Salário Bruto, Desconto, Salário Liquido.
Var

HT: real
VH: real
PD: real
SB: real
TD: real
SL: real

Inicio
escreva("Escrava quantas horas trabalhou este mês: ")
leia(HT)
escreval()
escreva("Escreva quanto vale cada hora trabalhada: ")
leia(VH)
escreval()
escreva("Escreva o percentual de desconto: ")
leia(PD)
escreval()

SB<- HT * VH
TD<- (PD/100) * SB
SL<- SB - TD

escreval
escreva("Horas Trabalhadas: ")
escreval(HT)
escreva("Salário Bruto: R$")
escreval(SB)
escreva("Desconto no seu salário: R$")
escreval(TD)
escreva("Salário Liquido: R$")
escreval(SL)


Fimalgoritmo
Algoritmo "semnome"

//Fa�a um algoritmo que:
//a) Obtenha o valor para a vari�vel HT (horas trabalhadas no m�s)
//b) Obtenha o valor para a vari�vel VH (valor hora trabalhada)
//c) Obtenha o valor para a vari�vel PD (percentual de desconto)
//d) Calcule o sal�rio bruto SB HT VH
//e) Calcule o total de desconto TD ==( 100 )*SB
//f) Calcule o sal�rio l�quido SL SB TD
g) Apresente os valores de Horas trabalhadas, Sal�rio Bruto, Desconto, Sal�rio Liquido.
Var

HT: real
VH: real
PD: real
SB: real
TD: real
SL: real

Inicio
escreva("Escrava quantas horas trabalhou este m�s: ")
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
escreva("Sal�rio Bruto: R$")
escreval(SB)
escreva("Desconto no seu sal�rio: R$")
escreval(TD)
escreva("Sal�rio Liquido: R$")
escreval(SL)


Fimalgoritmo
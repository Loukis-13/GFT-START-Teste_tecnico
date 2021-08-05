from modulos import *

print(f'Pares = {pares()}', end='\n\n')

h = Hospedagem(100)
h.print_valor()

h_VIP = HospedagemVIP(100, 50)
h_VIP.print_valor()
print()

print(dia_aniversario("05/08/2020"))
print(dia_aniversario("05/15/2021"))
print()

investimento = Investimento(1000, 4)
print(investimento.calcular_lucro(2))

investimento_com_IR = InvestimentoComIR(4000, 1.2)
print(investimento_com_IR.calcular_lucro(17))

investimento_sem_IR = InvestimentoSemIR(2000, 0.7)
print(investimento_sem_IR.calcular_lucro(10))
print()

# demostração de uso da documentação
# descomenta para ver

# help(pares)
# help(Hospedagem)
# help(Investimento)
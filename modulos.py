"""
  variaveis formatadas para seguir o padrao de python
"""


# Primeiro teste
def pares() -> int:
  ''' função que lê um valor inteiro (este número tem que conter 4 dígitos) e retorna a quantidade de dígitos "pares" '''

  # repete até que valor valido seja inserido
  while True:
    # recebe uma entrada na forma de string
    num = input("Digita um número com 4 digitos: ")

    # verifica se 'num' possui 4 digitos e se é numérico
    # casa um seja falso o programa volta para o inicio
    # e o input é repetido até que sejam verdadeiros
    if (len(num)!=4 or not num.isnumeric):
      print("O número deve ser de 1000 a 9999\n")
      continue

    # variavel para contar os valores pares
    pares = 0

    # forEach em num 
    for i in num:
      # transforma 'i' em int e verifica se é par
      if int(i)%2==0:
        # incrementa 'pares caso seja par'
        pares+=1
    
    # quebra o loop e retorna o valor da variavel 'par'
    return pares


# segundo teste
class Hospedagem:
  ''' classe de Hospedagem '''

  # instancia a classe
  def __init__(self: object, valor: float) -> None:
    self.valor=valor

  # imprime o valor do atributo 'valor' da instancia
  def print_valor(self: object) -> None:
    print(self.valor)


class HospedagemVIP(Hospedagem):
  ''' classe de hospedagem VIP '''
  # instancia a classe
  def __init__(self: object, valor: float, valor_adicional: float) -> None:
    # instancia a classe superior herdada
    super().__init__(valor)
    self.valor_adicional = valor_adicional

  # imprime a soma de 'valor' e 'valor_adicional'
  def print_valor(self: object) -> None:
    print(self.valor + self.valor_adicional)


# terceiro teste
def dia_aniversario(data: str) -> str:
  """ 
    Funçãão que recebe um data de aníversario e retorna uma string dizendo se ela é valida

    data: str recebida em formato 'dd/mm/aaaa'
  """

  d, m, a = map(int, data.split("/"))

  if (d < 0 or d > 31):
    return "Não é válido, dia incorreto"

  if (m < 0 or m > 12):
    return "Data inválida, mês incorreto"

  if (a != 2020):
    return "Data inválida, ano incorreto"

  return "Data válida"


# quarto teste
class Investimento:
  ''' classe de investimento '''

  # instancia a classe
  def __init__(self: object, valor_inicial:float, juros_mensais: float) -> None:
    self.valor_inicial=valor_inicial
    self.juros_mensais=juros_mensais/100

  # calcula o lucro com base na formula fornecida
  def calcular_lucro(self: object, meses: int) -> float:
    return (self.valor_inicial * (1+self.juros_mensais)**meses) - self.valor_inicial

class InvestimentoComIR(Investimento):
  ''' classe de investimento com imposto de renda '''

  # chama o metodo da classe superior e faz o desconto com base no número de meses passado
  def calcular_lucro(self: object, meses: int) -> float:
    lucro_bruto = super().calcular_lucro(meses)
    if meses<6:
      return lucro_bruto - lucro_bruto * .225
    elif meses<12:
      return lucro_bruto - lucro_bruto * .2
    elif meses<24:
      return lucro_bruto - lucro_bruto * .175
    else:
      return lucro_bruto - lucro_bruto * .15

class InvestimentoSemIR(Investimento):
  ''' classe de investimento sem imposto de renda '''

  # chama o metodo da classe superior e retorna o valor de tal
  # caso o investimento incial seja maior que 1000
  # se não retorna 0
  def calcular_lucro(self: object, meses: int) -> float:
    if self.valor_inicial<100:
      print("O valor Inicial não pode ser menor que R$1000")
      return 0

    return super().calcular_lucro(meses)
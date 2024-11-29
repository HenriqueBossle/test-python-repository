"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor A para A.M. e P para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar."""

def conversao(hora24, min24):
    if hora24 == 0:
        hora12 == 12
        """periodo == 'A'"""
    elif 1 <= hora24 < 12:
        hora12 = hora24
        """periodo == 'A'"""
    elif hora24 == 12:
        hora12 == 12
        """periodo == 'P'"""
    else:
        hora12 = hora24 - 12
        """periodo == 'P'"""
    return hora12, min24,
  
while True:
        hora24 = int(input('Digite um horário: '))
        """ min24 = int(input('Digite os minutos: '))"""
        horaem12 = conversao(hora24)
        print(horaem12)



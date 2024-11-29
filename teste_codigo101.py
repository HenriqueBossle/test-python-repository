"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor A para A.M. e P para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar."""

def converte_hora(hora24, minuto24):
    """Converte o horário de 24 horas para 12 horas."""
    if hora24 == 0:
        hora12 = 12
        periodo = 'A'
    elif 1 <= hora24 < 12:
        hora12 = hora24
        periodo = 'A'
    elif hora24 == 12:
        hora12 = 12
        periodo = 'P'
    else:
        hora12 = hora24 - 12
        periodo = 'P'
    return hora12, minuto24, periodo

def exibe_hora(hora12, minuto12, periodo):
    """Exibe o horário no formato de 12 horas com A.M./P.M."""
    periodo_str = 'A.M.' if periodo == 'A' else 'P.M.'
    print(f"{hora12}:{minuto12:02d} {periodo_str}")

def main():
    """Função principal que executa o loop para receber entradas e exibir a conversão."""
    while True:
        try:
            hora24 = int(input("Digite a hora (0-23): "))
            minuto24 = int(input("Digite os minutos (0-59): "))
            if 0 <= hora24 <= 23 and 0 <= minuto24 <= 59:
                hora12, minuto12, periodo = converte_hora(hora24, minuto24)
                exibe_hora(hora12, minuto12, periodo)
            else:
                print("Por favor, insira valores válidos para hora (0-23) e minutos (0-59).")
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros para hora e minutos.")
        
        repetir = input("Deseja converter outro horário? (s/n): ")
        if repetir.lower() != 's':
            break

# Executa o programa principal
main()


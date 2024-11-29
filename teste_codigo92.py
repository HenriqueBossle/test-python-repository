import requests
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

print(requisicao)

dic_requisicao = requisicao.json()

#rint(dic_requisicao)

taxa_dolar_real = float(dic_requisicao["USDBRL"]["bid"])
taxa_euro_real = float(dic_requisicao["EURBRL"]["bid"])

while True:
    print("Menu de conversão:")
    print("a - Converter de real para dólar")
    print("b - Converter de dólar para real")
    print("c - Converter de real para euro")
    print("d - Converter de euro para real")
    print("e - Sair")

    opcao = input("Escolha uma opção (a-e): ")
    if opcao == 'a':
        valor = float(input("Digite o valor em reais: "))
        resultado = round(valor / taxa_dolar_real, 6)
        print("Valor em dólares:", resultado)
    elif opcao == 'b':
        valor = float(input("Digite o valor em dólares: "))
        resultado = round(valor * taxa_dolar_real, 6)
        print("Valor em reais:", resultado)
    elif opcao == 'c':
        valor = float(input("Digite o valor em reais: "))
        resultado = round(valor / taxa_euro_real, 6)
        print("Valor em euros:", resultado)
    elif opcao == 'd':
        valor = float(input("Digite o valor em euros: "))
        resultado = round(valor * taxa_euro_real, 6)
        print("Valor em reais:", resultado)
    elif opcao == 'e':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Escolha novamente.")

    input("Pressione ENTER para continuar...")
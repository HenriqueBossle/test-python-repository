#Inverter uma string
def inverter_string(string):
    string_invertida = string[::-1]
    return string_invertida


teste = input('Digite uma palavra: ')
print("%s" % inverter_string(teste))
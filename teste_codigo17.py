"""Uma pessoa pesa 65kg e mede 1,70m. Qual é o seu índice de massa corporal (IMC)? Considere a
fórmula IMC = peso / altura²."""

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura**2

if imc < 28:
    print('Você está no peso ideal')
elif imc > 28.01 and imc < 33:
    print('Você está acima do peso')
else:
    print('Você está obeso')


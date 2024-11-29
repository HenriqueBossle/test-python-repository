"""Calcula a resistência elétrica de um chuveiro ligado a uma ddp informada pelo usuraio e, que produz uma corrente informada pelo usúario"""

u = int(input('Digite a ddp: '))
i = int(input('Digite a corrente: '))

r = u/i

print(r)
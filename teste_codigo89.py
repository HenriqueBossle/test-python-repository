
contador = 0
while contador <= 100:
    contador += 1

    if contador == 6:
      print('Eliminei o 6')
      continue

    if contador >= 10 and contador <=89:
      print(f'Eliminei o {contador}')
      continue
     
    print(contador)
    if contador == 90:
       break
 
print('End')
    


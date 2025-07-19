"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(10)
numeros_start_stop = range(5, 10)
numeros_start_stop_step = range(5, 10, 2)

print(f'\nRange de numeros de 0 a 10:\n{numeros}')
print(f'\nRange de numeros com definição de onde começa(start) e onde termina a contagem(stop):\n{numeros_start_stop}')
print(f'\nRange de numeros com definição de onde começa(start), onde termina(stop)\n'\
      f'e de quanto em quanto a contagem esta sendo feita(step):\n{numeros_start_stop_step}\n') 

#temos que a variavel numero criada no for arnazena os valores do range que esta realizando a contagem de 2 em 2
for numero in numeros_start_stop_step: 
      print(numero)
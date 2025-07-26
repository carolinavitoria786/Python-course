"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
    
#-------Explicação-de-qual-a-lógica-do-for-------#

#for letra in texto:
#    print(letra)

texto = 'Carol' #iterável que possui os elementos
iterador = iter(texto) #iterator 

while True:
    try:
        letra = next(iterador) #retorna o proximo valor da variável que possui os elementos
        print(letra)
    except StopIteration:
        break
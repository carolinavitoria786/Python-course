""""
Fatiamento de strings
 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p][::]
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:]) #omitir o numrero final(f) diz ao programa para ler até o final.
print(variavel[:4]) #omitir o numrero inicial(i) diz ao programa para ler desde o inicio até o indice solicitado porem o python sempre retornara um indice antes do solicitado.
print(len(variavel))
print(variavel[0:9:1])
print(variavel[-1:-10:-1])
print(variavel[0:9:2])
print(variavel[-1:-10:-2])

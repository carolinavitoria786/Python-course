# Operadores de comparação (relacionais)
# OP      Significado     Exemplo (True)
# >       maior             2 > 1
# >=      maior ou igual    2 >= 2
# <       menor             1 < 2
# <=      menor ou igual    2 <= 2
# ==      igual           'a' == 'a'
# !=      diferente       'a' != 'b'

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor} é maior ou igual ao {segundo_valor}')
elif primeiro_valor <= segundo_valor:
    print(f'{segundo_valor} é maior ou igual ao {primeiro_valor}')
else:
    print('entrada incorreta')
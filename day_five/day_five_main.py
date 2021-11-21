from day_five_data import lista


def divisao(letra, inicio, fim):
    quant = len(range(inicio, fim))
    if letra == 'F' or letra == 'L':
        return inicio, (inicio + int(quant / 2))
    if letra == 'B' or letra == 'R':
        return (inicio + int(quant / 2) + 1), fim


def get_fila(code):
    inicio = 0
    fim = 127
    for l in code:
        inicio, fim = divisao(l, inicio, fim)
    return inicio


def get_coluna(code):
    inicio = 0
    fim = 7
    for l in code:
        inicio, fim = divisao(l, inicio, fim)
    return inicio


def achar_lugar(code):
    codigo_fila = ''
    codigo_coluna = ''
    for n in range(7):
        codigo_fila = codigo_fila + code[n]
    for i in range(7, 10):
        codigo_coluna = codigo_coluna + code[i]
    fila = get_fila(codigo_fila)
    coluna = get_coluna(codigo_coluna)
    return fila, coluna


def get_id(fila, coluna):
    return (fila * 8) + coluna


print('--------------------------------------------PART ONE--------------------------------------------')
id_maior = 0
for codigo in lista:
    fila, coluna = achar_lugar(codigo)
    id = get_id(fila, coluna)
    if id > id_maior:
        id_maior = id
print(id_maior)

print('--------------------------------------------PART TWO--------------------------------------------')
aviao = []
for codigo in lista:
    fila, coluna = achar_lugar(codigo)
    acento = (fila, coluna)
    aviao.append(acento)
for l in range(127):
    for c in range(7):
        if (l, c) in aviao:
            print(l, c, True)
        else:
            print(l, c, False)

print(get_id(81, 1))

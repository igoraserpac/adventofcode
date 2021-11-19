cont = 0


def conferir_dados(dicionario):
    global cont
    if 'byr' in dicionario:
        if 'iyr' in dicionario:
            if 'eyr' in dicionario:
                if 'hgt' in dicionario:
                    if 'hcl' in dicionario:
                        if 'ecl' in dicionario:
                            if 'pid' in dicionario:
                                cont += 1


def separar_linha(linha):
    return linha.split(' ')


lista_dicionarios = []
with open('day_four_data_file.txt', 'r', encoding='UTF-8') as data:
    dicionario = {}
    for linha in data:
        lista = separar_linha(linha)

        if lista == ['\n']:
            lista_dicionarios.append(dicionario)
            dicionario = {}
        if lista != ['\n']:
            for dado in lista:
                chave, valor = dado.split(':')
                novo_valor = {chave: valor}
                dicionario.update(novo_valor)
for dicio in lista_dicionarios:
    conferir_dados(dicio)
    print(dicio)
    print(cont)

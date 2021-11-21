cont = 0


def conferir_byr(valor):
    if len(valor) != 4:
        return False
    else:
        valor = int(valor)
        if 1920 <= valor <= 2002:
            return True
        else:
            return False


def conferir_iyr(valor):
    if len(valor) != 4:
        return False
    else:
        valor = int(valor)
        if 2010 <= valor <= 2020:
            return True
        else:
            return False


def conferir_eyr(valor):
    if len(valor) != 4:
        return False
    else:
        valor = int(valor)
        if 2020 <= valor <= 2030:
            return True
        else:
            return False


def conferir_hgt(valor):
    if valor.endswith('cm'):
        valor = int(valor.split('c')[0])
        if 150 <= valor <= 193:
            return True
        else:
            return False
    elif valor.endswith('in'):
        valor = int(valor.split('i')[0])
        if 59 <= valor <= 76:
            return True
        else:
            return False


def conferir_hcl(valor):
    invalid = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if len(valor) != 7:
        return False
    else:
        if not valor.startswith('#'):
            return False
        else:
            for n in invalid:
                if n in valor:
                    return False
            return True


def conferir_ecl(valor):
    aceitos = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if valor in aceitos:
        return True
    else:
        return False


def conferir_pid(valor):
    if len(valor) == 9:
        try:
            valor = int(valor)
        except:
            return False
        return True
    else:
        return False


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

print('--------------------------------------------PART ONE--------------------------------------------')
print(cont)
print('--------------------------------------------PART TWO--------------------------------------------')

contador = 0
contador_final = 0
for dicio in lista_dicionarios:
    for chave in dicio:
        if '\n' in dicio[chave]:
            dicio[chave] = dicio[chave].replace('\n', '')

        if chave == 'byr':
            if conferir_byr(dicio[chave]):
                contador += 1

        if chave == 'iyr':
            if conferir_iyr(dicio[chave]):
                contador += 1

        if chave == 'eyr':
            if conferir_eyr(dicio[chave]):
                contador += 1

        if chave == 'hgt':
            if conferir_hgt(dicio[chave]):
                contador += 1

        if chave == 'hcl':
            if conferir_hcl(dicio[chave]):
                contador += 1

        if chave == 'ecl':
            if conferir_ecl(dicio[chave]):
                contador += 1

        if chave == 'pid':
            if conferir_pid(dicio[chave]):
                contador += 1

    if contador == 7:
        contador_final += 1
    contador = 0

print(contador_final)



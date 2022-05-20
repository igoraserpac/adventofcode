file_name = 'day_seven_data.txt'

with open(file_name, 'r') as f:
    data = f.read().splitlines()
    dic = {}
    for n in data:
        rule = n.split(' contain ')
        can_carry = rule[1]
        dic[rule[0]] = can_carry

unpacked = {}
for k, v in dic.items():
    bag = ' '.join(k.split()[:-1])
    content = v.split(', ')
    for color in content:
        if color[-1] == '.':
            content[content.index(color)] = color[:-1]
    unpacked[bag] = content

endbags = []
for k, v in unpacked.items():
    dicionario = {}
    if 'no other bags' in v:
        endbags.append(k)
    else:
        tupla1 = tuple([int(n[0]) for n in v])
        tupla2 = tuple([f'{" ".join(n.split()[1:-1])}' for n in v])
        for _ in range(len(tupla1)):
            dicionario[tupla2[_]] = tupla1[_]
        print(dicionario)
        unpacked[k] = dicionario

colors = []
for k, v in dic.items():
    if 'shiny gold' in v:
        colors.append(' '.join(k.split()[:-1]))

for cor in colors:
    for k, v in dic.items():
        if cor in v and ' '.join(k.split()[:-1]) not in colors:
            colors.append(' '.join(k.split()[:-1]))

print(f'parte 1: {len(colors)}')


cont = 0


def contar(cor):
    global cont
    if 'no other bags' in unpacked[cor]:
        cont += 1
    else:
        lista = []
        for bolsa, quant in unpacked[cor].items():
            for n in range(quant):
                lista.append(bolsa)
        for b in lista:
            contar(b)
        cont += 1
    return cont - 1


print(f"Parte 2: {contar('shiny gold')}")

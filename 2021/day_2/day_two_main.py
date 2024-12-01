"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we
can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the
Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted
database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde 1-3 b: cdefg 2-9 c: ccccccccc Each line gives the password policy and then the password. The password
policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For
example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b,
but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits
of their respective policies.

How many passwords are valid according to their policies?

"""

from day_two_data import dicionario as data


def condicional_mult(min, max, letra, senha):
    numero = senha.count(letra)
    if min <= numero <= max:
        return True
    else:
        return False


def condicional_index(min, max, letra, senha):

    if senha[min-1] == letra:
        if senha[max-1] != letra:
            return True
        return False
    elif senha[max-1] == letra:
        return True
    else:
        return False


aux1 = 0
aux2 = 0
for key in data:
    min_cond, resto = key.split('-')
    max_cond, letra = resto.split()
    min_cond = int(min_cond)
    max_cond = int(max_cond)
    senhas = data[key]
    for senha in senhas:
        if condicional_mult(min_cond, max_cond, letra, senha):
            aux1 += 1
    for senha in senhas:
        if condicional_index(min_cond, max_cond, letra, senha):
            aux2 += 1


print('--------------------------------------------PART ONE--------------------------------------------')
print(aux1)
print('--------------------------------------------PART TWO--------------------------------------------')
print(aux2)

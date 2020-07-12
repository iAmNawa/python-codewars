# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.

# Your task is to change the letters with diacritics:

#ą -> a,
#ć -> c,
#ę -> e,
#ł -> l,
#ń -> n,
#ó -> o,
#ś -> s,
#ź -> z,
#ż -> z

def correct_polish_letters(st):
    final = []
    for elem in st:
        if elem == 'ą':
            final.append('a')
        elif elem == 'ć':
            final.append('c')
        elif elem == 'ę':
            final.append('e')
        elif elem == 'ł':
            final.append('l')
        elif elem == 'ń':
            final.append('n')
        elif elem == 'ó':
            final.append('o')
        elif elem == 'ś':
            final.append('s')
        elif elem == 'ź':
            final.append('z')
        elif elem == 'ż':
            final.append('z')
        else:
            final.append(elem)
    return ''.join(final)

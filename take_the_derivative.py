def derive(coefficient, exponent):
    multiplied = coefficient * exponent
    multiplied_string = str(multiplied) + 'x^' + str(exponent -1)
    return multiplied_string

derive(8,7)

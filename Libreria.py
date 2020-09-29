from fractions import Fraction

def drill3_2__2(splits, blancos, Psplits, Pblancos):
    b = n_splits(splits,blancos,Psplits,Pblancos)
    c = multiplicar_matrices(b, b)

    return c



def n_splits(splits, blancos, Psplits, Pblancos):

    rango = splits+blancos

    matrix = []
    for i in range(rango+1):
        a = []
        for j in range(rango+1):
            a.append(0)
        matrix.append(a)

    for r in range(len(matrix)):
        matrix[r][0] = Psplits[r]
        p = r+1
        for t in range(len(matrix[r])):
            if p < len(matrix[r]) and r < splits:
                matrix[t][p] = Pblancos[r][t]
                if t > splits:
                    matrix[t][t] = 1
    return matrix

def multiplicar_matrices(a, b):
    producto = []
    for i in range(len(a)):
        multi = []
        for j in range(len(b[0])):
            suma = 0
            for x in range(len(a[i])):
                r = a[i][x]
                f = b[x][j]
                suma += Fraction(r) * Fraction(f)
            multi.append("{}/{}".format(suma.numerator,suma.denominator))
        producto.append(multi)
    return producto
'''
Descripcion: Calcula el factorial de un numero

Estructura: [fac] = fact(x)

Parametros: x (numero utilizado para calcular el factorial)

'''


def fact(x):
    if x >= 0:
        fac = 1
        for i in range(1, x + 1):
            fac = fac * i
        return fac
    else:
        return "error"


'''
Descripcion: Calcula la multiplicacion entre dos numeros

Estructura: [a*b] = mult_t(a, b)

Parametros: a (numero 1), b (numero 2)

'''


def mult_t(a, b):
    return a * b


'''
Descripcion: Calcula la suma entre dos numeros

Estructura: [a+b] = sum_t(a, b)

Parametros: a (numero 1), b (numero 2)

'''


def sum_t(a, b):
    return a + b


'''
Descripcion: Calcula la resta entre dos numeros

Estructura: [a-b] = resta_t(a, b)

Parametros: a (numero 1), b (numero 2)

'''


def resta_t(a, b):
    return a - b


'''
Descripcion: Calcula el inverso de un numero por medio de un metodo iterativo

Estructura: [x] = div_t(a)

Parametros: a (numero)

'''


def div_t(a):
    if a > 0:
        eps = 2.22044604925e-16

        tol = 10e-8
        iterMax = 2500

        x0 = 0

        if fact(0) > a and a <= fact(20):
            x0 = eps ** 2
        elif fact(20) > a and a <= fact(40):
            x0 = eps ** 4
        elif fact(40) > a and a <= fact(60):
            x0 = eps ** 8
        elif fact(60) > a and a <= fact(80):
            x0 = eps ** 11
        elif fact(60) > a and a <= fact(80):
            x0 = eps ** 11
        elif fact(80) > a and a < fact(100):
            x0 = eps ** 15
        else:
            x0 = 0

        x = x0

        for i in range(1, iterMax):
            xprev = x
            x = x * (2 - a * x)
            if abs(x - xprev) < tol * abs(x):
                break

        return x

    else:

        return "error"


# div_t(2)


'''
Descripcion: Calcula la division entre dos numeros

Estructura: [a/b] = division_t(a, b)

Parametros: a (numero 1), b (numero 2)

'''


def division_t(a, b):
    return a * div_t(b)


'''
Descripcion: Calcula la potencia de euler con un exponente dado

Estructura: [x] = exp_t(a)

Parametros: a (exponente)

'''


def exp_t(a):
    tol = 10e-8
    iterMax = 2500
    a_sig = a
    a = abs(a)

    x = 1
    for i in range(1, iterMax):
        xprev = x
        x += (a ** i) * div_t(fact(i))
        if abs(x - xprev) < tol * abs(x):
            break

    if a_sig < 0:
        return div_t(x)

    print("exp", x)
    return x


# exp_t(2)

'''
Descripcion: Calcula el seno de un numero dado

Estructura: [x] = sin_t(a)

Parametros: a (numero)

'''


def sin_t(a):
    tol = 10e-8
    iterMax = 2500
    a_sign = a
    a = abs(a)
    x = a
    for i in range(1, iterMax):
        xprev = x
        x += ((-1) ** i) * (a ** (2 * i + 1)) * div_t(fact(2 * i + 1))
        if abs(x - xprev) < tol * abs(x):
            break

    if a_sign < 0:
        x = -x

    print("sen", x)
    return x


# sin_t(1)

'''
Descripcion: Calcula el coseno de un numero dado

Estructura: [x] = cos_t(a)

Parametros: a (numero)

'''


def cos_t(a):
    tol = 10e-8
    iterMax = 2500
    a = abs(a)
    x = 1
    for i in range(1, iterMax):
        xprev = x
        x += ((-1) ** i) * (a ** (2 * i)) * div_t(fact(2 * i))
        if abs(x - xprev) < tol * abs(x):
            break

    print("cos", x)
    return x


# cos_t(1)

'''
Descripcion: Calcula la tangente de un numero dado

Estructura: [x] = tan_t(a)

Parametros: a (numero)

'''


def tan_t(a):
    cos_a = cos_t(a)
    sen_a = sin_t(a)

    if cos_a != 0:
        x = sen_a * div_t(cos_a)

        print("tan", x)
        return x

    else:
        return "error"


# tan_t(1)

'''
Descripcion: Calcula el logaritmo natural de un numero dado

Estructura: [x] = ln_t(a)

Parametros: a (numero)

'''


def ln_t(a):
    if a > 0:
        tol = 10e-8
        iterMax = 2500

        x = (2 * (a - 1) * div_t(a + 1))
        for i in range(1, iterMax):
            xprev = x
            x += (2 * (a - 1) * div_t((a + 1))) * (1 * div_t((2 * i + 1))) * ((a - 1) * div_t((a + 1))) ** (2 * i)

            if abs(x - xprev) < tol * abs(x):
                break

        print("ln", x)
        return x

    else:
        return "error"


# ln_t(5)


'''
Descripcion: Calcula el logaritmo en base b de un numero dado

Estructura: [x] = log_t(a, b)

Parametros: a (numero), b (base del logaritmo)

'''


def log_t(a, b):
    if a > 0 and b > 0:

        x = (ln_t(a)) * div_t(ln_t(b))
        print("log", x)
        return x

    else:
        return "error"


# log_t(10000,10)


# fact_t(4)


'''
Descripcion: Calcula la potencia de exponente b de un numero dado

Estructura: [x] = power_t(a, b)

Parametros: a (numero), b (exponente)

'''


def power_t(a, b):
    x = 1
    tol = 10e-8
    iterMax = 2500
    c = b
    b = abs(b)
    if a == 0:
        return 0
    for i in range(1, iterMax):
        xprev = x
        x += ((b ** i) * (ln_t(a)) ** i) * div_t(fact(i))
        if abs(x - xprev) < tol * abs(x):
            break

    if c < 0:
        x = div_t(x)

    print("power", x)
    return x


# power_t(2, -4)


'''
Descripcion: Calcula el seno hiperbolico de un numero dado

Estructura: [x] = sinh_t(a)

Parametros: a (numero)

'''


def sinh_t(a):
    tol = 10e-8
    iterMax = 2500
    a_sign = a
    a = abs(a)
    x = a
    for i in range(1, iterMax):
        xprev = x
        x += (a ** (2 * i + 1)) * div_t(fact(2 * i + 1))
        if abs(x - xprev) < tol * abs(x):
            break

    if a_sign < 0:
        x = -x

    print("sinh", x)
    return x


# sinh_t(6)

'''
Descripcion: Calcula el coseno hiperbolico de un numero dado

Estructura: [x] = cosh_t(a)

Parametros: a (numero)

'''


def cosh_t(a):
    tol = 10e-8
    iterMax = 2500
    a_sign = a
    a = abs(a)
    x = 1
    for i in range(1, iterMax):
        xprev = x
        x += (a ** (2 * i)) * div_t(fact(2 * i))
        if abs(x - xprev) < tol * abs(x):
            break

    if a_sign < 0:
        x = -x

    print("cosh", x)
    return x


# cosh_t(6)

'''
Descripcion: Calcula la tangente hiperbolico de un numero dado

Estructura: [x] = tanh_t(a)

Parametros: a (numero)

'''


def tanh_t(a):
    cosh_a = cosh_t(a)
    senh_a = sinh_t(a)

    if (cosh_a != 0):

        x = senh_a * div_t(cosh_a)

        print("tanh", x)
        return x
    else:
        return "error"


# tanh_t(4)


'''
Descripcion: Calcula la raiz cuadrada de un numero dado

Estructura: [x] = sqrt_t(a)

Parametros: a (numero)

'''


def sqrt_t(a):
    tol = 10e-8
    iterMax = 2500
    x = a * div_t(2)
    if a > 0:
        for i in range(1, iterMax):
            xprev = x
            x = x - ((x ** 2 - a) * div_t(2 * x ** (2 - 1)))
            if abs(x - xprev) < tol * abs(x):
                break
        print("sqr", x)
        return x

    elif a == 0:
        return 0

    else:
        return "error"


'''
Descripcion: Calcula la raiz de indice b de un numero dado

Estructura: [x] = root_t(a, b)

Parametros: a (numero), b (indice)

'''


def root_t(a, b):
    tol = 10e-8
    iterMax = 2500
    x = a * div_t(2)
    if a > 0 and b != 0:
        if b > 0:
            for i in range(1, iterMax):
                xprev = x
                x = x - ((x ** b - a) * div_t(b * x ** (b - 1)))
                if abs(x - xprev) < tol * abs(x):
                    break
            print("root", x)
            return x
        if b < 0:
            print("root", x)
            return power_t(a, b)
    elif a == 0:
        return 0

    else:

        return "error"


root_t(0, 2)

'''
Descripcion: Calcula el arcoseno de un numero dado

Estructura: [x] = asin_t(a)

Parametros: a (numero)

'''


def asin_t(a):
    tol = 10e-8
    iterMax = 2500
    a_sign = a
    a = abs(a)
    x = a
    if a <= 1:
        for i in range(1, iterMax):
            xprev = x
            x += (a ** (2 * i + 1)) * (fact(2 * i) * div_t((4 ** i) * (fact(i) ** 2) * (2 * i + 1)))
            if abs(x - xprev) < tol * abs(x):
                break

        if a_sign < 0:
            x = -x

        print("asin", x)
        return x

    else:
        return "error"


asin_t(0.5)

'''
Descripcion: Calcula el arcocoseno de un numero dado

Estructura: [x] = acos_t(a)

Parametros: a (numero)

'''


def acos_t(a):
    tol = 10e-8
    iterMax = 2500
    pi = 3.141592653589793
    a = abs(a)
    x = a
    if a <= 1:
        for i in range(1, iterMax):
            xprev = x
            x += (a ** (2 * i + 1)) * (fact(2 * i) * div_t((4 ** i) * (fact(i) ** 2) * (2 * i + 1)))
            if abs(x - xprev) < tol * abs(x):
                break

        x = pi * div_t(2) - x

        print("acos", x)
        return x

    else:
        return "error"


acos_t(0.5)

'''
Descripcion: Calcula la arcotangente de un numero dado

Estructura: [x] = atan_t(a)

Parametros: a (numero)

'''


def atan_t(a):
    tol = 10e-8
    iterMax = 2500

    if a >= -1 and a <= 1:
        x = a
        for i in range(1, iterMax):
            xprev = x
            x += ((-1) ** i) * (a ** (2 * i + 1)) * div_t(2 * i + 1)
            if abs(x - xprev) < tol * abs(x):
                break

        print("atan", x)
        return x

    elif a > 1:
        pi = 3.141592653589793
        x = div_t(a)
        for i in range(1, iterMax):
            xprev = x
            x += ((-1) ** i) * div_t((2 * i + 1) * (a ** (2 * i + 1)))
            if abs(x - xprev) < tol * abs(x):
                break
        x = pi * div_t(2) - x

        print("atan", x)
        return x

    elif a < -1:
        pi = 3.141592653589793
        x = div_t(a)
        for i in range(1, iterMax):
            xprev = x
            x += ((-1) ** i) * div_t((2 * i + 1) * a ** (2 * i + 1))
            if abs(x - xprev) < tol * abs(x):
                break
        x = -pi * div_t(2) - x

        print("atan", x)
        return x

    else:
        return "error"


atan_t(0.5)

'''
Descripcion: Calcula la cosecante de un numero dado

Estructura: [x] = csc_t(a)

Parametros: a (numero)

'''


def csc_t(a):
    if sin_t(a) != 0:
        print("csc", div_t(sin_t(a)))
        return div_t(sin_t(a))
    else:
        return "error"


csc_t(3)

'''
Descripcion: Calcula la secante de un numero dado

Estructura: [x] = sec_t(a)

Parametros: a (numero)

'''


def sec_t(a):
    if cos_t(a) != 0:
        print("sec", div_t(cos_t(a)))
        return div_t(cos_t(a))
    else:
        return "error"


sec_t(0.4)

'''
Descripcion: Calcula la cotangente de un numero dado

Estructura: [x] = cot_t(a)

Parametros: a (numero)

'''


def cot_t(a):
    if tan_t(a) != 0:
        print("cot", div_t(tan_t(a)))
        return div_t(tan_t(a))
    else:
        return "error"


cot_t(0.5)


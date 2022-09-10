def fact(x):
    fac = 1
    for i in range(1, x + 1):
        fac = fac * i
    return fac


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
        print("Dicha division no es posible para numeros reales")
        return "inf"


# div_t(2)


def exp_t(a):
    tol = 10e-8
    iterMax = 2500

    x = 1
    for i in range(1, iterMax):
        xprev = x
        x += (a ** i) * div_t(fact(i))
        if abs(x - xprev) < tol * abs(x):
            break

    print("exp", x)
    return x


# exp_t(2)


# SENO
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


def tan_t(a):
    cos_a = cos_t(a)
    sen_a = sin_t(a)
    x = sen_a * div_t(cos_a)

    print("tan", x)
    return x


# tan_t(1)

# LOGARITMO NATURAL
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

# LOGARITMO BASE A
def log_t(a, b):
    if a > 0 and b > 0:

        x = (ln_t(a)) * div_t(ln_t(b))
        print("log", x)
        return x

    else:
        return "error"


# log_t(10000,10)


#####################################

def power_t(a, b):
    x = 1

    for i in range(1, abs(b) + 1):
        x *= a

    if b < 0:
        x = div_t(x)

    print("power", x)
    return x


# power_t(2, -4)

####################################

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


def tanh_t(a):
    cosh_a = cosh_t(a)
    senh_a = sinh_t(a)
    x = senh_a * div_t(cosh_a)

    print("tanh", x)
    return x


# tanh_t(4)


def root_t(a, b):
    tol = 10e-8
    iterMax = 2500
    x = a * div_t(2)
    if a >= 0:

        for i in range(1, iterMax):
            xprev = x
            x = x - ((x ** b - a) * div_t(b * x ** (b - 1)))
            if abs(x - xprev) < tol * abs(x):
                break
        print("root", x)
        return x

    else:

        return "error"


# root_t(4, 2)


def asin_t(a):
    tol = 10e-8
    iterMax = 2500
    a_sign = a
    a = abs(a)
    x = a
    for i in range(1, iterMax):
        xprev = x
        x += (a ** (2 * i + 1)) * (fact(2 * i) * div_t((4 ** i) * (fact(i) ** 2) * (2 * i + 1)))
        if abs(x - xprev) < tol * abs(x):
            break

    if a_sign < 0:
        x = -x

    print("asin", x)
    return x


asin_t(0.5)


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


atan_t(0.5)


def csc_t(a):
    print("csc", div_t(sin_t(a)))
    return div_t(sin_t(a))


csc_t(3)


def sec_t(a):
    print("sec", div_t(cos_t(a)))
    return div_t(cos_t(a))


sec_t(0.4)


def cot_t(a):
    print("cot", div_t(tan_t(a)))
    return div_t(tan_t(a))


cot_t(0.5)

# arreglar atan y sec

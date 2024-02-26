import numpy as np

# Función para determinar f(x)
f_x = lambda x: (x ** 3) + (4 * x ** 2) - 10


# Función algoritmo de bisección
def bisection_error_abs(a, b, func, error):
    # Comprobación de condiciones iniciales
    if np.sign(func(a)) * np.sign(func(b)) == 1:
        print(f'En el intervalo [{a}, {b}] la función no tiene ceros.')
        return

    if func(a) == 0:
        print(f'Un cero de la función es {a}')
        return

    if func(b) == 0:
        print(f'Un cero de la función es {b}')
        return

    print("| i | a_i | b_i | p_n | fp_n | Error abs |")
    i = 1
    pn_1 = a
    # Bucle principal del método de bisección
    while True:

        fa, fb = func(a), func(b)
        p_n = (a + b) / 2
        fc = func(p_n)

        error_abs = abs(p_n - pn_1)

        print(f"| {i} | {a} | {b} | {p_n} | {fc} | {error_abs} ")

        # Actualiza los extremos del intervalo según el signo de la función en el punto medio
        if np.sign(fa) * np.sign(fc) == 1:
            a = p_n
        elif np.sign(fb) * np.sign(fc) == 1:
            b = p_n
        else:
            break

        if error_abs <= error:
            return

        pn_1 = p_n
        i += 1


# Llama a la función bisection_error_abs con los valores iniciales
bisection_error_abs(1, 2, f_x, 0.00001)

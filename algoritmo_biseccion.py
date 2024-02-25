import numpy as np

# Función para determinar f(x)
f_x = lambda x: x ** 3 - 7 * x ** 2 + 14 * x - 6


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

    print("| a_i | b_i | p_i | fp_i | Error abs | Error Rel |")

    # Bucle principal del método de bisección
    while True:
        fa, fb = func(a), func(b)
        p_i = (a + b) / 2
        fc = func(p_i)

        print(f"| {a} | {b} | {p_i} | {fc} |", end="")

        # Actualiza los extremos del intervalo según el signo de la función en el punto medio
        if np.sign(fa) * np.sign(fc) == 1:
            a = p_i
        elif np.sign(fb) * np.sign(fc) == 1:
            b = p_i
        else:
            break

        print(f"{abs((a + b) / 2 - p_i):,.10f} | {abs((a + b) / 2 - p_i) / abs((a + b) / 2):,.10f} |")

        # Condición de terminación del bucle
        if abs((a + b) / 2 - p_i) < error or abs((a + b) / 2 - p_i) / abs((a + b) / 2) < error:
            break


# Llama a la función bisection_error_abs con los valores iniciales
bisection_error_abs(0, 1, f_x, 0.01)

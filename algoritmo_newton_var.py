# Definir la función g(x) = x-f(x)/f'(x), f'(x) != 0 que se quiere evaluar
import math
import numpy as np

f_x = lambda x: x - math.cos(x)
df_x = lambda x: 1 + math.sin(x)
g_x = lambda x: x - (f_x(x) / df_x(x))


# Algoritmo Método de Newton
def newton_method(p_0, g_x, error, n):
    if df_x(p_0) == 0:
        print(f"La función g_x converge en el punto {p_0}")
        return

    p_n_1 = p_0
    p_n = g_x(p_0)

    i = 1
    print("Resultados Método de Newton")
    print("| i | p_{n-1} | p_n | error |")
    while abs(p_n - p_n_1) > error:
        print(f"| {i} | {p_n_1} | {p_n} | {abs(p_n - p_n_1)} |")
        p_n_1 = p_n
        p_n = g_x(p_n)
        i += 1
        if i >= n:
            return print(f"La función no converge a algún punto p, empezando por {p_0}")

    print(f"La aproximación es p = {p_n}")


# Algoritmo de la Secante
def secant_method(p_n_2, p_n_1, f_x, error, n):
    if f_x(p_n_2) == 0:
        print(f'La solución f(p) = 0 es {p_n_2}')
        return

    if f_x(p_n_1) == 0:
        print(f'La solución f(p) = 0 es {p_n_1}')
        return

    if f_x(p_n_2) - f_x(p_n_1) == 0:
        print(f'El método converge en los puntos {p_n_2}, {p_n_1}')
        return

    print("Resultados Método de la Secante")
    print("| i | p_{n-2} |  p_{n-1} | p_n | error |")

    q_n_2, q_n_1, i = (f_x(p_n_2), f_x(p_n_1), 0)
    p_n = p_n_1 - (q_n_1 * (p_n_1 - p_n_2)) / (q_n_1 - q_n_2)
    while abs(p_n - p_n_1) > error:

        print(f"| {i} | {p_n_2} | {p_n_1} | {p_n} | {abs(p_n - p_n_1)} |")

        if f_x(p_n_2) - f_x(p_n_1) == 0:
            print(f'El método converge en los puntos {p_n_2}, {p_n_1}')
            return

        if i > n:
            print(f'EL método ha pasado las n={n} iteraciones')
            return

        p_n_2, p_n_1 = (p_n_1, p_n)
        q_n_2, q_n_1 = (f_x(p_n_2), f_x(p_n_1))
        p_n = p_n_1 - (q_n_1 * (p_n_1 - p_n_2)) / (q_n_1 - q_n_2)

        i += 1

    print(f'la aproximación de p es {p_n}')


# Algoritmo del Punto Flaso
def false_position_method(p_n_2, p_n_1, f_x, error, n):
    if f_x(p_n_2) == 0:
        return print(f'La solución f(p) = 0 es {p_n_2}')

    if f_x(p_n_1) == 0:
        return print(f'La solución f(p) = 0 es {p_n_1}')

    if f_x(p_n_2) - f_x(p_n_1) == 0:
        return print(f'El método converge en los puntos {p_n_2}, {p_n_1}')

    if np.sign(f_x(p_n_2)) * np.sign(f_x(p_n_1)) == 1:
        return print(f'f({p_n_2}) * f({p_n_1}) es mayor que 0')

    print("Resultados Método del Punto Falso")
    print("| i | p_{n-2} |  p_{n-1} | p_n | error |")

    q_n_2, q_n_1, i = (f_x(p_n_2), f_x(p_n_1), 0)
    p_n = p_n_1 - (q_n_1 * (p_n_1 - p_n_2)) / (q_n_1 - q_n_2)
    while abs(p_n - p_n_1) > error:

        print(f"| {i} | {p_n_2} | {p_n_1} | {p_n} | {abs(p_n - p_n_1)} |")

        if f_x(p_n_2) - f_x(p_n_1) == 0:
            return print(f'El método converge en los puntos {p_n_2}, {p_n_1}')

        if i > n:
            return print(f'EL método ha pasado las n={n} iteraciones')

        if np.sign(f_x(p_n_1)) * np.sign(f_x(p_n)) == 1:
            return print(f'f({p_n_1}) * f({p_n}) es mayor que 0')

        # Actualiza los extremos del intervalo según el signo de la función
        if np.sign(f_x(p_n_1)) * np.sign(f_x(p_n)) == 1:
            p_n_1 = p_n
        elif np.sign(f_x(p_n_2)) * np.sign(f_x(p_n)) == 1:
            p_n_2 = p_n
        else:
            break

        q_n_2, q_n_1 = (f_x(p_n_2), f_x(p_n_1))
        p_n = p_n_1 - (q_n_1 * (p_n_1 - p_n_2)) / (q_n_1 - q_n_2)

        i += 1

    print(f'la aproximación de p es {p_n}')


newton_method(0, g_x, 0.00001, 20)
print("______________________________________________")
"""secant_method(math.pi / 4, 4, f_x, 0.00001, 20)
print("______________________________________________")
false_position_method(math.pi / 4, 4, f_x, 0.00001, 20)  """

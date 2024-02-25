# Definir la función g(x) = x que se quiere evaluar
import math

g_x = lambda x: x - x ** 3 - (4 * x ** 2) + 10


# Algoritmo Punto Fijo
def iteration_fixed_point(a, b, p_0, g_x, error):
    if g_x(a) < a or g_x(b) > b or g_x(a) > b or g_x(b) < a:
        print(f"La función g(x) no tiene punto fijo en ese intervalo, "
              f"dado que g({a}) = {g_x(a)} y g({b}) = {g_x(b)} ")
        return

    p_n = g_x(p_0)
    p_n_1 = p_0

    i = 1

    print("| i | p_{n-1} | p_n | error |")
    while abs(p_n - p_n_1) > error:
        print(f"| {i} | {p_n_1} | {p_n} | {abs(p_n - p_n_1)} |")
        p_n_1 = p_n
        p_n = g_x(p_n)
        i += 1
    return p_n


print(iteration_fixed_point(1, 2, 1.5, g_x, 0.000001))

def cuad(x):
    """Dado un número x, calcula x²"""
    return x * x # También podríamos haber hecho x ** 2
def modulo_vector(x, y):
    """Calcula el módulo de un vector 2D.
    Argumentos:
        x: (float|int) coordenada de las abscisas
        y: (float|int) coordenada de las ordenadas
    Devuelve: (float) el módulo del vector
    """
    return (x ** 2 + y ** 2) ** 0.5
print(help(modulo_vector))
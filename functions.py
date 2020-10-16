from numpy import linspace

def str_to_list(list_value: list):
    list_coeffs = list_value.replace(' ', '').split(',')
    return list(map(float, list_coeffs))

def Polynomial(P: list, x: list):
    """
    # Polynomial

    `P`: lista de constantes do polinônio.\n
    `x`: array de pontos.

    `return`: array com os valores do polinômio para o 
    limite de dados do array `x`.
    """
    return sum(c * x ** e for (e, c) in enumerate(P))

def generator_points(down_limit, upper_limit, n_points):
    """
    # Generator points
    
    `return`: numpy.array no intervalo informado.
    """
    return linspace(down_limit, upper_limit, n_points, endpoint=True)

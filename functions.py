from numpy import linspace, around

def exist_letters(string: str):
    """
    ### exist_letters

    Verifica e existem caracteres do tipo texto.

    `string`: texto de entrada

    """
    char_permited = [',', '-', '.', ' ']
    for char in char_permited:
        string = string.replace(char, '')
    return not all(char.isdigit() for char in string)

def str_to_list(text: str):
    """
    ### str_to_list

    Transforma uma string em uma lista numérica, 
    onde cada elemento é do tipo `float`.

    `text`: String que será transformada em uma lista. 
    """
    try:
	    list_coeffs = text.replace(' ', '').split(',')
	    return list(map(float, list_coeffs))
    except:
	    return []

def Polynomial(P: list, x: list):
    """
    # Polynomial

    `P`: lista de constantes do polinônio.\n
    `x`: array de pontos.

    `return`: array com os valores do polinômio para o 
    limite de dados do array `x`.
    """
    return sum(c * x ** e for (e, c) in enumerate(P))

def generator_points(down_limit, upper_limit, n_points, precision=4):
    """
    # Generator points
    
    `return`: numpy.array no intervalo informado.
    """
    return around(linspace(down_limit, upper_limit, n_points, endpoint=True), decimals=precision)

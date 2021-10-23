def primera_letra (lista_de_palabras):
    primeras_letras = []

    for palabras in lista_de_palabras:
        assert type(palabras) == str, f'{palabras} no es str'
        assert len(palabras) > 0, 'No se permiten str vacios'

        primera_letra.append(palabras[0])
    
    return primera_letra

    
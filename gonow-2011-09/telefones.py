# -*- encoding: utf-8 -*-

def _para_numero(letra):
    """Devolve o número correspondente a 
    letra ou a própria letra se não
    encontrar o valor"""

    letra = letra.upper()
    mapa = (
       ('ABC','2'), 
       ('DEF','3'),
       ('GHI','4'),
       ('JKL','5'),
       ('MNO','6'),
       ('PQRS','7'),
       ('TUV','8'),
       ('WXYZ','9'),
    )
    for letras, valor in mapa:
        if letra in letras:
            return valor
    return letra

def para_numeros(texto):
    """ Separa o texto em letras e 
    chama o metodo para_numero para cada
    letra
    """
    retorno = ''
    for letra in texto:
        retorno += _para_numero(letra)

    return retorno

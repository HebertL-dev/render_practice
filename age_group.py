def get_age_group(age):

    """
    Devuelve el grupo de edad basado en la edad en años dentro del intervalo 0..150
    de lo contrario, devuelve 'desconocido'.
    """

    if 0 <= age <= 12:
        return 'infancia'
    if 13<= age <=18:
        return 'adolescencia'
    if 19<= age <= 26:
        return 'juventud'
    if 27<= age <=59:
        return 'adultez'
    if 60<= age <=110:
        return 'vejez'
        # Completa esta función para que pase la prueba unitaria
    return 'desconocido'

def test_get_age_group():
    """prueba unitaria para get_age_group"""

    assert get_age_group(-1) == 'desconocido'
    assert get_age_group(0) == 'infancia'
    assert get_age_group(14) == 'adolescencia'
    assert get_age_group(15) == 'adolescencia'
    assert get_age_group(24) == 'juventud'
    assert get_age_group(25) == 'juventud'
    assert get_age_group(64) == 'vejez'
    assert get_age_group(65) == 'vejez'
    assert get_age_group(80) == 'vejez'
    assert get_age_group(150) == 'desconocido'

from sublista_suma_max import suma_maxima


def test_suma_maxima():
    casos = [
        ([1, -2, 3, 4, -9, 6], [3, 4]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8, -8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, -2, 3, -4, 5, -6, 7, -8, -8], [7]),
        ([-1, -8, -3, -2, -100, -8, -4], [-1]),
        ([5, -1, 2], [5, -1, 2]),
        ([4, -5, 4, -1, 2, -1, 2, -3], [4, -1, 2, -1, 2]),
        ([-1, -2, -3, -4, -5], [-1]),
    ]
    for caso, resultado in casos:
        assert suma_maxima(caso) == resultado


def test_suma_maxima_no():
    casos = [
        [-1, -1, -1, -1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, -1],
    ]
    for caso in casos:
        assert suma_maxima(caso) == []

def test_suma_maxima_vacio():
    assert suma_maxima([]) == []

def test_suma_maxima_uno():
    assert suma_maxima([8]) == [8]
    assert suma_maxima([-8]) == [-8]


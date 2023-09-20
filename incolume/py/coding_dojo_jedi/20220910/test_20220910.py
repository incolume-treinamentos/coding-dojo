from sys import version_info

import pytest
from dojo20220910 import weekday, weekday0, weekday1


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        (1, 'Domingo'),
        (2, 'Segunda'),
        (3, 'Terça'),
        (4, 'Quarta'),
        (5, 'Quinta'),
        (6, 'Sexta'),
        (7, 'Sábado'),
        (8, 'Valor inválido'),
        (9, 'Valor inválido'),
        (0, 'Valor inválido'),
    ),
)
def test_weekday0(entrance, expected):
    assert weekday0(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        (1, 'Domingo'),
        (2, 'Segunda'),
        (3, 'Terça'),
        (4, 'Quarta'),
        (5, 'Quinta'),
        (6, 'Sexta'),
        (7, 'Sábado'),
        (8, 'Valor inválido'),
        (9, 'Valor inválido'),
        (0, 'Valor inválido'),
    ),
)
def test_weekday1(entrance, expected):
    assert weekday1(entrance) == expected


@pytest.mark.skipif(
    version_info < (3, 10, 0),
    reason='This run only Python 3.10+',
)
@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        (1, 'Domingo'),
        (2, 'Segunda'),
        (3, 'Terça'),
        (4, 'Quarta'),
        (5, 'Quinta'),
        (6, 'Sexta'),
        (7, 'Sábado'),
        (8, 'Valor inválido'),
        (9, 'Valor inválido'),
        (0, 'Valor inválido'),
    ),
)
def test_weekday(entrance, expected):
    assert weekday(entrance) == expected

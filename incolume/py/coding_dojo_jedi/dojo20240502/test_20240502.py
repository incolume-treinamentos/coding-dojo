"""Dojo validação de CPF realizado em 02/05/2024."""

import pytest
from dojo import check_cpf, verify_cpf


class TestCheckCPF:
    """CheckCPF tests."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('000.000.001-91', True),
            ('000.000.002-72', True),
            ('000.000.003-53', True),
            ('000.000.000-00', False),
            ('123.456.789-12', False),
            ('529.982.247-25', True),
            ('777.777.777-77', False),
            (49691275228, True),
            (56681418104, True),
            ('777.777.777', False),
            ('', False),
        ],
    )
    def test_check_cpf(self, entrance, expected):
        """Test it."""
        assert check_cpf(entrance) == expected


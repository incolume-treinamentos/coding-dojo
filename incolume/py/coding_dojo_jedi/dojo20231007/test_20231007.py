"""Test para dojo 2023-10-07."""
import pytest

from . import max_sequence, max_sub_array_sum, subarray_max_sum


def test_max_sequence() -> None:
    """Test de max_sequence."""
    assert max_sequence([]) == 0


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ([-1, -2, -3, -4], 0),
        ([-10, -2, -3, -1], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
        ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 55),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([10, -11, 2, 3, 4, 5, -5, 6, 7, -50, 8, -7, 9], 22),
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
    ],
)
def test_max_sequence1(entrance, expected) -> None:
    """Test de max."""
    assert max_sequence(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ([-1, -2, -3, -4], 0),
        ([-10, -2, -3, -1], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
        ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 55),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([10, -11, 2, 3, 4, 5, -5, 6, 7, -50, 8, -7, 9], 22),
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
    ],
)
def test_subarray_max_sum(entrance, expected) -> None:
    """Test subarray_max_sum."""
    assert subarray_max_sum(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ([-1, -2, -3, -4], 0),
        ([-10, -2, -3, -1], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
        ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 55),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([10, -11, 2, 3, 4, 5, -5, 6, 7, -50, 8, -7, 9], 22),
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
    ],
)
def test_maxsubarraysum(entrance, expected) -> None:
    """Test max_sub_array_sum."""
    assert max_sub_array_sum(entrance) == expected

"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 5, -2),  # Restar un número mayor al primero (resultado negativo)
        (5, 0, 5),  # Restar cero
        (-3, -5, 2),  # Restar dos números negativos
        (5.5, 2.2, 3.3),  # Restar dos números decimales (float)
    ],
)
def test_sub_casos_especiales(a, b, expected):
    """Test para casos especiales de resta."""
    assert sub(a, b) == expected

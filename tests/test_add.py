"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (-5, -3, -8),  # Sumar dos números negativos
        (5, -3, 2),  # Sumar un número positivo y uno negativo
        (5, 0, 5),  # Sumar con cero
        (1.5, 2.3, 3.8),  # Sumar dos números decimales (float)
    ],
)
def test_add_casos_especiales(a, b, expected):
    """Test para casos especiales de suma."""
    assert add(a, b) == expected

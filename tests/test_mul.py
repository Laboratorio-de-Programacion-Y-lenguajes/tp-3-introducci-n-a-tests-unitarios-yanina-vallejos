"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 0, 0),  # Multiplicar por cero
        (-3, -4, 12),  # Multiplicar dos números negativos (resultado positivo)
        (5, -2, -10),  # Multiplicar un positivo y un negativo (resultado negativo)
        (7, 1, 7),  # Multiplicar por 1 (elemento neutro)
        (1.5, 2.0, 3.0),  # Multiplicar dos decimales (float)
    ],
)
def test_mul_casos_especiales(a, b, expected):
    """Test de multiplicación para casos especiales."""
    assert mul(a, b) == expected

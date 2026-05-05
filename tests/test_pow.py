"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 0, 1),  # Cualquier número elevado a 0
        (7, 1, 7),  # Número elevado a 1
        (-3, 4, 81),  # Base negativa con exponente par (resultado positivo)
        (9, 0.5, 3.0),  # Exponente decimal (raíz cuadrada)
    ],
)
def test_pow_casos_especiales(a, b, expected):
    """Test para casos especiales de potencia."""
    assert pow_(a, b) == expected

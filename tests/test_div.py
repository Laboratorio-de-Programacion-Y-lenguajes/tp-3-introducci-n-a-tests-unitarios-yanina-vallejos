"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
def test_div_resultado_decimal():
    """División que da resultado decimal (float): 5 / 2 = 2.5"""
    assert div(5, 2) == 2.5


def test_div_numeros_negativos():
    """División con números negativos: -10 / 2 = -5.0"""
    assert div(-10, 2) == -5.0


def test_div_por_cero():
    """División por cero debe lanzar ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---


def test_sqrt_cero():
    """Raíz de 0 debe dar 0.0."""
    assert sqrt(0) == 0.0


def test_sqrt_no_cuadrado_perfecto():
    """Raíz de un número no cuadrado perfecto debe dar resultado decimal."""
    assert sqrt(2) == pytest.approx(1.41421356, rel=1e-7)


def test_sqrt_negativo():
    """Raíz de un número negativo debe lanzar ValueError."""
    with pytest.raises(ValueError):
        sqrt(-4)

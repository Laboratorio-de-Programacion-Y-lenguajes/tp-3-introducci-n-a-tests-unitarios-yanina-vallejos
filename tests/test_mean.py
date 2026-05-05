"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
def test_mean_un_solo_elemento():
    """Lista con un solo elemento: [5] = 5.0"""
    assert mean([5]) == 5.0


def test_mean_numeros_negativos():
    """Lista con números negativos: [-2, -4, -6] = -4.0"""
    assert mean([-2, -4, -6]) == -4.0


def test_mean_numeros_decimales():
    """Lista con números decimales (float): [1.5, 2.5, 3.0] = 2.333...."""
    assert mean([1.5, 2.5, 3.0]) == pytest.approx(2.333333, rel=1e-5)


def test_mean_lista_vacia():
    """Lista vacía debe lanzar ValueError."""
    with pytest.raises(ValueError):
        mean([])

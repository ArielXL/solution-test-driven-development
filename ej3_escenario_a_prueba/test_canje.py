"""SOLUCIÓN Ej. 3 — el escenario convertido en prueba de aceptación parametrizada."""

import pytest

from canje import canjear_cafe


@pytest.mark.parametrize(
    "puntos, resultado, restantes",
    [
        (120, "aprobado", 70),
        (50, "aprobado", 0),
        (30, "rechazado", 30),
    ],
)
def test_canje_de_cafe(puntos, resultado, restantes):
    # Dado que el cliente tiene <puntos> puntos
    saldo = puntos
    # Cuando canjea un café de 50 puntos
    aprobado, quedan = canjear_cafe(saldo)
    # Entonces el canje es <resultado> y le quedan <restantes> puntos
    assert aprobado == (resultado == "aprobado")
    assert quedan == restantes

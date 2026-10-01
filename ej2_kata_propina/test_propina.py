"""SOLUCIÓN Ej. 2 — una prueba por regla del PO, en el orden en que se escribieron."""

import pytest

from propina import calcular_propina


# Vuelta 1 (regla 1) — rojo: ImportError. Verde: return subtotal * porcentaje / 100
def test_propina_es_porcentaje_del_subtotal():
    assert calcular_propina(100, 10) == 10


# Vuelta 2 (regla 2) — suele pasar a la primera: ¡OJO! si pasa sin cambiar código,
# la prueba no guía nada nuevo; se deja como documentación.
@pytest.mark.parametrize("porcentaje, esperada", [(0, 0), (10, 20), (15, 30), (20, 40)])
def test_porcentajes_permitidos(porcentaje, esperada):
    assert calcular_propina(200, porcentaje) == esperada


# Vuelta 3 (regla 3) — rojo: no lanza error. Verde: validar contra el conjunto permitido.
@pytest.mark.parametrize("porcentaje", [5, 25, -10])
def test_porcentaje_no_permitido_se_rechaza(porcentaje):
    with pytest.raises(ValueError):
        calcular_propina(100, porcentaje)


# Vuelta 4 (regla 4) — rojo: 12.345 != 12.35 aprox. Verde: round(..., 2)
def test_redondeo_a_dos_decimales():
    assert calcular_propina(82.30, 15) == 12.35

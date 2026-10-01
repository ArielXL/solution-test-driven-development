"""Ejercicio 1 — "Lee el rojo".

Corre:  python -m pytest ejercicios/ej1_lee_el_rojo -v

Contesta:
  a) ¿Cuántas pruebas pasan y cuántas fallan?
  b) En cada falla, ¿cuál era el valor ESPERADO y cuál el OBTENIDO?
  c) ¿El defecto está en la prueba o en el código? Justifica con la regla del PO.
  d) Corrige el código cambiando UNA sola línea y vuelve a correr hasta ver verde.
  e) Señala en este archivo: un caso de prueba, la suite y quién hace de arnés.
"""

import pytest

from puntos import calcular_puntos


def test_compra_de_cero_no_da_puntos():
    assert calcular_puntos(0) == 0


def test_menos_de_diez_pesos_no_da_puntos():
    assert calcular_puntos(9.99) == 0


def test_solo_cuentan_los_diez_completos():
    assert calcular_puntos(47) == 4


def test_cien_pesos_dan_diez_puntos():
    assert calcular_puntos(100) == 10


@pytest.mark.parametrize("total, esperados", [(10, 1), (20, 2), (35, 3)])
def test_tabla_de_ejemplos(total, esperados):
    assert calcular_puntos(total) == esperados

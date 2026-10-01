"""SOLUCIÓN Ej. 1 — se cambia UNA línea: round() redondeaba al más cercano;
la regla del PO pide solo los $10 COMPLETOS → división entera."""


def calcular_puntos(total):
    return int(total // 10)

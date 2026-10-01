"""SOLUCIÓN Ej. 2 — código final de la kata (tras 4-5 vueltas de TDD)."""

PORCENTAJES_PERMITIDOS = {0, 10, 15, 20}


def calcular_propina(subtotal, porcentaje):
    if porcentaje not in PORCENTAJES_PERMITIDOS:
        raise ValueError(f"Porcentaje no permitido: {porcentaje}")
    return round(subtotal * porcentaje / 100, 2)

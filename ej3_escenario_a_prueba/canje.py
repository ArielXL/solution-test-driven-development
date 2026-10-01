"""Canje de puntos de CaféYa (ya implementado por el equipo de desarrollo)."""

COSTO_CAFE = 50  # puntos


def canjear_cafe(puntos):
    """Regresa (aprobado, puntos_restantes)."""
    if puntos >= COSTO_CAFE:
        return True, puntos - COSTO_CAFE
    return False, puntos

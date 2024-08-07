from urllib.parse import urlencode
from bcraapi import get_from_bcra
import pandas as pd


def maestros_divisas() -> pd.DataFrame:
    """
    Método para obtener el listado de todas las monedas ISO vigentes, con su respectiva denominación.

    Returns:
        pd.DataFrame: DataFrame con el listado del BCRA.
    """
    return get_from_bcra("/estadisticascambiarias/v1.0/Maestros/Divisas")


def cotizaciones(fecha: str = None) -> pd.DataFrame:
    """
    Método para obtener el listado de todas las cotizaciones de divisas vigentes publicadas por el BCRA para una fecha (YYYY-MM-DD) determinada; de no ingresarse una fecha se devolverá la última cotización existente.

    Args:
        fecha (int): Corresponde a la fecha del dato a consultar, la misma deberá tener el formato **YYYY-MM-DD**.

    Returns:
        pd.DataFrame: DataFrame con los valores para la fecha seleccionada.
    """
    if fecha is None:
        return get_from_bcra(f"/estadisticascambiarias/v1.0/Cotizaciones")
    else:
        return get_from_bcra(f"/estadisticascambiarias/v1.0/Cotizaciones?fecha={fecha}")


def cotizaciones_moneda(moneda: str, **kwargs) -> pd.DataFrame:
    """
    Método para obtener la evolución de cotización de una moneda (ISO) en un rango de fechas particular, de no ingresarse los parámetros de fecha desde y fecha hasta se devolverá la última cotización existente.

    Args:
        moneda (str): Moneda ISO.

    Keyword Args:
        fecha_desde (str): Fecha en formato (YYYY-MM-DD)
        fecha_hasta (str): Fecha en formato (YYYY-MM-DD)
        limit (int): Cantidad máxima a devolver por solicitud. Debe ser mayor a 10 y menor a 1000
        offset (int): Excluye de la respuesta los N primeros elementos de las cotizaciones a devolver

    Returns:
        pd.DataFrame: DataFrame con el listado del BCRA.
    """
    if kwargs:
        return get_from_bcra(f"/estadisticascambiarias/v1.0/Cotizaciones/{moneda}")
    else:
        return get_from_bcra(f"/estadisticascambiarias/v1.0/Cotizaciones/{moneda}?{urlencode(kwargs)}")


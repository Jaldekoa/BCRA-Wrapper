from bcraapi import get_from_bcra
from urllib.parse import urlencode
import pandas as pd


def monetarias(id_variable=None, **kwargs) -> pd.DataFrame:
    """
    Método para obtener la lista de todas las estadísticas de Series y Principales Variables publicadas por el BCRA o los valores para la serie o principal variable en un rango de fechas.

    Args:
        id_variable (int): ID de la variable deseada.
        desde (str): Corresponde a la fecha de inicio del rango a consultar, la misma deberá tener el formato **YYYY-MM-DD**.
        hasta (str): Corresponde a la fecha de fin del rango a consultar, la misma deberá tener el formato **YYYY-MM-DD**.
        offset (int): Registros que debe descartar para el paginado.
        limit (int): Registros que retornará el servicio. El valor máximo es 3000.

    Returns:
        pd.DataFrame: DataFrame con las variables publicadas por el BCRA o los valores para la variable.
    """
    if id_variable is None:
        return get_from_bcra("/estadisticas/v3.0/Monetarias")
    else:
        return get_from_bcra(f"/estadisticas/v3.0/Monetarias/{id_variable}?{urlencode(kwargs)}")
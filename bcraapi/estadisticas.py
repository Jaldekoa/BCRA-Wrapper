from bcraapi import get_from_bcra
from typing import Union, Optional
import pandas as pd


def monetarias(**kwargs) -> pd.DataFrame:
    """
    Método para obtener la lista de todas las variables monetarias publicadas por el BCRA.

    Keyword Args:
        id_variable (int): ID de la variable deseada.
        categoria (str): El mismo indica la clasificación de la variable monetaria.
        periodicidad (str): Frecuencia que se generan la variable: Diaria (D), mensual (M) o trimestral (T o Q)
        moneda (str): Vale la pena aclarar que no se está hablando en códigos de monedas ISO. Moneda local (ML), moneda extranjera (ME), combinación de ambas (MEyML), pesos argentinos (ARS) o dólar (USD).
        tipo_serie (str): Corresponde a la caracterización económica de la variable.
        unidad_expresion (str): Corresponde a la unidad de medición de la variable económica
        offset (int): Registros que debe descartar para el paginado.
        limit (int): Registros que retornará el servicio. El valor máximo es 3000.
        
    Returns:
        pd.DataFrame: DataFrame con las variables publicadas por el BCRA o los valores para la variable.
    """
    return get_from_bcra("/estadisticas/v4.0/Monetarias", **kwargs)


def datos_monetarias(id_variable: Union[int, str], **kwargs) -> pd.DataFrame:
    """
    Método que obtener la evolución de los valores para la variable monetaria en un rango de fechas. Para un mejor rendimiento en la respuesta, se recomienda incluir el filtro de fechas desde y hasta en las consultas.
    
    Args:
        id_variable (int): ID de la variable deseada.
    
    Keyword Args:
        
        desde (str): Corresponde a la fecha de inicio del rango a consultar, la misma deberá tener el formato **YYYY-MM-DD**.
        hasta (str): Corresponde a la fecha de fin del rango a consultar, la misma deberá tener el formato **YYYY-MM-DD**.
        offset (int): Registros que debe descartar para el paginado.
        limit (int): Registros que retornará el servicio. El valor máximo es 3000.

    Returns:
        pd.DataFrame: DataFrame con las variables publicadas por el BCRA o los valores para la variable.
    """
    return get_from_bcra(f"/estadisticas/v4.0/Monetarias/{id_variable}", **kwargs)


def metodologia(id_variable: Optional[Union[int, str]] = None, **kwargs) -> pd.DataFrame:
    """
    Método para obtener las metodologías correspondientes a cada variable informada.

    Args:
        id_variable (int): ID de la variable deseada. Si no se informa se obtendrá todas las metodologías.

    Keyword Args:
        offset (int): Registros que debe descartar para el paginado.
        limit (int): Registros que retornará el servicio. El valor máximo es 3000.
    
    Returns:
        pd.DataFrame: DataFrame con la metodología correspondiente a la variable informada.
    """
    
    if id_variable is None:
        return get_from_bcra("/estadisticas/v4.0/metodologia", **kwargs)
    else:
        return get_from_bcra(f"/estadisticas/v4.0/metodologia/{id_variable}", **kwargs)

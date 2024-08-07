from bcraapi import get_from_bcra
import pandas as pd


def principales_variables() -> pd.DataFrame:
    """
    Método para obtener la lista de todas las variables publicadas por el BCRA.

    Returns:
        pd.DataFrame: DataFrame con las variables publicadas por el BCRA.
    """
    return get_from_bcra("/estadisticas/v2.0/principalesvariables")


def datos_variable(id_variable: int, desde: str, hasta: str) -> pd.DataFrame:
    """
    Método para obtener los valores para la variable y el rango de fechas indicadas.

    Args:
        id_variable (int): ID de la variable deseada, la misma se puede consultar mediante ``principales_variables()``.
        desde (str): Corresponde a la fecha de inicio del rango a consultar, la misma deberá tener el formato **YYYY-MM-DD**.
        hasta (str): Corresponde a la fecha de fin del rango a consultar, la misma deberá tener el formato **YYYY-MM-DD**.

    Returns:
        pd.DataFrame: DataFrame con los valores para la variable y el rango de fechas seleccionadas.
    """
    return get_from_bcra(f"/estadisticas/v2.0/datosvariable/{id_variable}/{desde}/{hasta}")

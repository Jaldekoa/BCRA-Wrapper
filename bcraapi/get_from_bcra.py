from .api_client import connect_to_bcra
import pandas as pd


def __parse_cols(df: pd.DataFrame) -> pd.DataFrame:
    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")
    if "valor" in df.columns:
        df["valor"] = df["valor"].str.replace(".", "").str.replace(",", ".").astype(float)
    return df


def principales_variables(**kwargs) -> pd.DataFrame:
    """
    Método para obtener la lista de todas las variables publicadas por el BCRA.

    Keyword Args:
        lang (str): Los idiomas configurados actualmente “es-AR” y “en-US”. De no informar dicho parámetro, la respuesta se realizará por defecto en “es-AR”.

    Returns:
        pd.DataFrame: DataFrame de pandas con las columnas idVariable, cdSerie, fecha y valor.
    """

    lang = kwargs.get("lang", None)
    json = connect_to_bcra(endpoint="principalesvariables", lang=lang)
    df = pd.DataFrame(json)
    df = __parse_cols(df)
    return df


def datos_variable(id_variable: int, desde: str, hasta: str, **kwargs) -> pd.DataFrame:
    """
    Método para obtener los valores para la variable y el rango de fechas indicadas.

    Args:
        id_variable (int): ID de la variable deseada, la misma se puede consultar por el endpoint “Obtener principales variables”.
        desde (str): Corresponde a la fecha de inicio del rango a consultar, la misma deberá tener el formato YYYY-MM-DD.
        hasta (str): Corresponde a la fecha de fin del rango a consultar, la misma deberá tener el formato YYYY-MM-DD.

    Keyword Args:
        lang (str): Los idiomas configurados actualmente “es-AR” y “en-US”. De no informar dicho parámetro, la respuesta se realizará por defecto en “es-AR”.

    Returns:
        pd.DataFrame: DataFrame de pandas con las columnas idVariable, fecha y valor.
    """

    lang = kwargs.get("lang", None)
    json = connect_to_bcra(endpoint=f"DatosVariable/{id_variable}/{desde}/{hasta}", lang=lang)
    df = pd.DataFrame(json)
    df = __parse_cols(df)
    return df

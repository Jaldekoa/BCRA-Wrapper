import pandas as pd
import requests
import os

base_url = "https://api.bcra.gob.ar"


def __connect_to_data(url: str, cert_path: str) -> pd.DataFrame:
    if cert_path is None:
        cert_path = os.path.join(os.path.dirname(__file__), "cert/bcra.gob.ar.crt")

    res = requests.get(url, verify=cert_path)
    json = res.json()

    if res.status_code == 200:
        return pd.DataFrame.from_dict(json["results"])
    else:
        raise Exception(f"Error {json['status']}. {'.'.join(json['errorMessages'])}")


def __parse_cols(df: pd.DataFrame) -> pd.DataFrame:
    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d")
    if "valor" in df.columns:
        df["valor"] = pd.to_numeric(df["valor"])
    return df


def datos_variable(id_variable: int, desde: str, hasta: str, cert_path: str = None) -> pd.DataFrame:
    """
    Método para obtener los valores para la variable y el rango de fechas indicadas.

    Args:
        id_variable (int): ID de la variable deseada, la misma se puede consultar por el endpoint “Obtener principales variables”.
        desde (str): Corresponde a la fecha de inicio del rango a consultar, la misma deberá tener el formato YYYY-MM-DD.
        hasta (str): Corresponde a la fecha de fin del rango a consultar, la misma deberá tener el formato YYYY-MM-DD.
        cert_path (str): Ruta del certificado SSL de conexión con BCRA. Por defecto se usa el incluído en el proyecto.
    Returns:
        pd.DataFrame: DataFrame de pandas con las columnas idVariable, fecha y valor.
    """
    df = __connect_to_data(url=f"{base_url}/estadisticas/v2.0/DatosVariable/{id_variable}/{desde}/{hasta}",
                           cert_path=cert_path)
    df = __parse_cols(df)
    return df


def principales_variables(cert_path: str = None) -> pd.DataFrame:
    """
    Método para obtener la lista de todas las variables publicadas por el BCRA.

    Args:
        cert_path (str): Ruta del certificado SSL de conexión con BCRA. Por defecto se usa el incluído en el proyecto.

    Returns:
        pd.DataFrame: DataFrame de pandas con las columnas idVariable, cdSerie, fecha y valor.
    """
    df = __connect_to_data(url=f"{base_url}/estadisticas/v2.0/principalesvariables", cert_path=cert_path)
    df = __parse_cols(df)
    return df

import pandas as pd
import requests

base_url = "https://api.bcra.gob.ar"


def datos_variable(id_variable: int, desde: str, hasta: str) -> pd.DataFrame:
    """
    Método para obtener los valores para la variable y el rango de fechas indicadas.

    Args:
        id_variable (int): ID de la variable deseada, la misma se puede consultar por el endpoint “Obtener principales variables”.
        desde (str): Corresponde a la fecha de inicio del rango a consultar, la misma deberá tener el formato YYYY-MM-DD.
        hasta (str): Corresponde a la fecha de fin del rango a consultar, la misma deberá tener el formato YYY-MM-DD.

    Returns:
        pd.DataFrame: DataFrame de pandas con las columnas idVariable, fecha y valor.
    """

    url = f"{base_url}/estadisticas/v1/DatosVariable/{id_variable}/{desde}/{hasta}"
    res = requests.get(url)
    json = res.json()

    if res.status_code == 200:
        df = pd.DataFrame.from_dict(json["results"])
        df["fecha"] = pd.to_datetime(df["fecha"],format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        df["valor"] = df["valor"].str.replace(".", "").str.replace(",", ".").astype(float)
        return df

    else:
        raise Exception(f"Error {json['status']}. {json['errorMessages'][0]}")


def principales_variables() -> pd.DataFrame:
    """
    Método para obtener la lista de todas las variables publicadas por el BCRA.

    Returns:
        pd.DataFrame: DataFrame de pandas con las columnas idVariable, cdSerie, fecha y valor.
    """

    url = f"{base_url}/estadisticas/v1/principalesvariables"
    res = requests.get(url, verify=False)
    json = res.json()

    if res.status_code == 200:
        df = pd.DataFrame.from_dict(json["results"])
        df["fecha"] = pd.to_datetime(df["fecha"], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        df["valor"] = df["valor"].str.replace(".", "").str.replace(",", ".").astype(float)
        return df

    else:
        raise Exception(f"Error {json['status']}. {json['errorMessages'][0]}")

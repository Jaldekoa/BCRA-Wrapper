import requests
import warnings


def __check_lang(lang: str = "es-AR"):
    if lang not in ["es-AR", "en-US"]:
        warnings.warn(f"'lang' must be 'es-AR' or 'en-US'. By default 'es-AR' will be used.", SyntaxWarning)
        return {"Accepted-Language": "es-AR"}
    else:
        return {"Accepted-Language": lang}


def connect_to_bcra(endpoint: str, lang: str = None) -> dict:
    """
    Conexión con la API de Banco Central de la República Argentina (BCRA).

    Args:
        endpoint (str): Endpoint de la API a la que realiza la petición.
        lang (str): Los idiomas configurados actualmente “es-AR” y “en-US”. De no informar dicho parámetro, la respuesta se realizará por defecto en “es-AR”.

    Returns:
        dict: JSON de respuesta.
    """

    base_url, header = "https://api.bcra.gob.ar/estadisticas/v1", __check_lang(lang)
    res = requests.get(f"{base_url}/{endpoint}", headers=header, verify=False)
    json = res.json()

    if res.status_code == 200:
        return json["results"]
    else:
        raise Exception(f"Error {json['status']}. {'.'.join(json['errorMessages'])}")

from typing import Union, Dict, List, Optional
from urllib.parse import urlencode
import pandas as pd
import requests
import urllib3
import os

__base_url = "https://api.bcra.gob.ar"

__cols_to_parse = {
    "idVariable": pd.to_numeric,
    "cdSerie": pd.to_numeric,
    "fecha": pd.to_datetime,
    "valor": pd.to_numeric,
    "fechaProcesamiento": pd.to_datetime,
    "codigoEntidad": pd.to_numeric,
    "numeroCuenta": pd.to_numeric,
    "primerFechaInformada": pd.to_datetime,
    "ultFechaInformada": pd.to_datetime,
    "ultValorInformado": pd.to_numeric,
    "id": pd.to_numeric,
    "tipoPase": pd.to_numeric,
    "tipoCotizacion": pd.to_numeric,
    "numeroCheque": pd.to_numeric,
    "sucursal": pd.to_numeric,
    "identificacion": pd.to_numeric,
    "situacion": pd.to_numeric,
    "monto": pd.to_numeric,
    "diasAtrasoPago": pd.to_numeric,
    "nroCheque": pd.to_numeric,
    "fechaSit1": pd.to_datetime,
    "fechaRechazo": pd.to_datetime,
    "fechaPago": pd.to_datetime,
    "fechaPagoMulta": pd.to_datetime,
    "fechaInformacion": pd.to_datetime,
    "comisionMaximaMantenimiento": pd.to_numeric,
    "ingresoMinimoMensual": pd.to_numeric,
    "antiguedadLaboralMinimaMeses": pd.to_numeric,
    "edadMaximaSolicitada": pd.to_numeric,
    "montoMinimoInvertir": pd.to_numeric,
    "plazoMinimoInvertirDias": pd.to_numeric,
    "tasaEfectivaAnualMinima": pd.to_numeric,
    "montoMaximoOtorgable": pd.to_numeric,
    "plazoMaximoOtorgable": pd.to_numeric,
    "relacionCuotaIngreso": pd.to_numeric,
    "cargoMaximoCancelacionAnticipada": pd.to_numeric,
    "tasaEfectivaAnualMaxima": pd.to_numeric,
    "costoFinancieroEfectivoTotalMaximo": pd.to_numeric,
    "relacionMontoTasacion": pd.to_numeric,
    "cuotaInicialCada100k": pd.to_numeric,
    "cuotaInicialCada10k": pd.to_numeric,
    "montoMinimoOtorgable": pd.to_numeric,
    "comisionMaximaAdministracionMantenimiento": pd.to_numeric,
    "comisionMaximaRenovacion": pd.to_numeric,
    "tasaEfectivaAnualMaximaFinanciacion": pd.to_numeric,
    "tasaEfectivaAnualMaximaAdelantoEfectivo": pd.to_numeric,
}

__params_map = {
    "id_variable": "idVariable",
    "categoria": "categoria",
    "periodicidad": "periodicidad",
    "moneda": "moneda",
    "tipo_serie": "tipoSerie",
    "unidad_expresion": "unidadExpresion",
    "offset": "offset",
    "limit": "limit",
    "desde": "desde",
    "hasta": "hasta",
    "fecha": "fecha",
    "fecha_desde": "fechaDesde",
    "fecha_hasta": "fechaHasta",
    "codigo_entidad": "codigoEntidad"
}


def __parse_params(params: dict) -> dict:
    return {__params_map[k]: v for k, v in params.items() if k in __params_map and v is not None}


def __connect_to_api(url: str, verify_cert: Union[bool, str] = False, timeout: int = 15) -> dict:
    verify = verify_cert
    if not verify:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    res = requests.get(url, verify=verify, timeout=timeout)

    if res.status_code == 200:
        data = res.json()
        return data.get('results', [])
        
    try:
        error_json = res.json()
        status = error_json.get('status', res.status_code)
        error_msgs = '.'.join(error_json.get('errorMessages', []))
        if status == 404:
            return []
        raise Exception(f"Error {status}. {error_msgs}")
    except ValueError:
        res.raise_for_status()


def __flatten_dict(d: dict, parent_key: str = '', sep: str = '_') -> dict:
    items = []
    for k, v in d.items():
        if isinstance(v, dict):
            items.extend(__flatten_dict(v, parent_key, sep=sep).items())
        elif isinstance(v, list):
            for item in v:
                items.extend(__flatten_dict(item, parent_key, sep=sep).items())
        else:
            items.append((k, v))
    return dict(items)


def __json_to_df(json_data: Union[Dict, List]) -> pd.DataFrame:
    if isinstance(json_data, dict):
        json_data = __flatten_dict(json_data)
        return pd.DataFrame([json_data])
    elif isinstance(json_data, list):
        flattened_list = [__flatten_dict(item) for item in json_data]
        return pd.DataFrame(flattened_list)
    return pd.DataFrame()


def __parse_cols(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    for col in df.columns:
        df[col] = __cols_to_parse[col](df[col]) if col in __cols_to_parse else df[col]
    return df


def get_from_bcra(endpoint: str, verify_cert: Union[bool, str] = False, **kwargs) -> pd.DataFrame:
    if kwargs:
        kwargs = __parse_params(kwargs)
        
    url = f"{__base_url}{endpoint}"
    if kwargs:
        url = f"{url}?{urlencode(kwargs)}"
        
    json_data = __connect_to_api(url=url, verify_cert=verify_cert)
    df = __json_to_df(json_data)
    df = __parse_cols(df)
    return df

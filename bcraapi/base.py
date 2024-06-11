from .metadata import cols_to_parse
import pandas as pd
import requests
import os

base_url = "https://api.bcra.gob.ar"
cert_path = os.path.join(os.path.dirname(__file__), "cert/bcra.gob.ar.crt")


def __connect_to_api(url: str) -> dict:
    res = requests.get(url, verify=cert_path)

    if res.status_code == 200:
        return res.json()['results']
    if res.status_code in [400, 404, 500]:
        raise Exception(f"Error {res.json()['status']}. {'.'.join(res.json()['errorMessages'])}")


def __flatten_dict(d: dict, mem: dict = None) -> dict:
    mem = {} if mem is None else mem
    for k, v in d.items():
        if isinstance(v, dict):
            mem = __flatten_dict(v, mem)
        else:
            mem[k] = v
    return mem


def __json_to_df(json: dict | list) -> pd.DataFrame:
    if isinstance(json, dict):
        json = __flatten_dict(json)
        return pd.DataFrame.from_dict(json, orient='index').T
    if isinstance(json, list):
        return pd.DataFrame(json)


def __parse_cols(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        df[col] = cols_to_parse[col](df[col]) if col in cols_to_parse else df[col]
    return df


def get_from_bcra(endpoint: str) -> pd.DataFrame:
    df = __connect_to_api(url=f"{base_url}{endpoint}")
    df = __json_to_df(df)
    df = __parse_cols(df)
    return df


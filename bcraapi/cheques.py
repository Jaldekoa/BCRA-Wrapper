from bcraapi import get_from_bcra
import pandas as pd


def entidades():
    """
    Método para obtener el listado de todas las entidades bancarias del país con su respectivo código de entidad.

    Returns:
        pd.DataFrame: DataFrame con el listado de todas las entidades bancarias del país con su respectivo código de entidad.
    """
    return get_from_bcra("/cheques/v1.0/entidades")


def denunciados(codigo_entidad: int, numero_cheque: int) -> pd.DataFrame:
    """
    Método para saber si un cheque de una determinada entidad se encuentra registrado como denunciado o no.

    Args:
        codigo_entidad (int): ID de la entidad financiera. La misma se puede consultar mediante ``entidades()``.
        numero_cheque (int): Corresponde al número de cheque a consultar.

    Returns:
        pd.DataFrame: DataFrame con el resultado si un cheque se encuentra registrado como denunciado o no.
    """
    return get_from_bcra(f"/cheques/v1.0/denunciados/{codigo_entidad}/{numero_cheque}")

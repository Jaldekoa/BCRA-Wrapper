from bcraapi.estadisticascambiarias import maestros_divisas, cotizaciones, cotizaciones_moneda
import pandas as pd


def test_maestros_divisas():
    df = maestros_divisas()
    assert isinstance(df, pd.DataFrame) and not df.empty


def test_cotizaciones():
    df = cotizaciones()
    assert isinstance(df, pd.DataFrame) and not df.empty
    df = cotizaciones(fecha="2024-06-12")
    assert isinstance(df, pd.DataFrame) and not df.empty


def test_cotizaciones_moneda():
    df = cotizaciones_moneda("EUR")
    assert isinstance(df, pd.DataFrame) and not df.empty
    df = cotizaciones_moneda("EUR", fecha_desde="2024-01-01", fecha_hasta="2024-06-14")
    assert isinstance(df, pd.DataFrame) and not df.empty

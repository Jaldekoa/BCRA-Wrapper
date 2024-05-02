from bcraapi import principales_variables, datos_variable
import pandas as pd


def test_principales_variables():
    assert isinstance(principales_variables(), pd.DataFrame)


def test_datos_variable():
    assert isinstance(datos_variable(1, "2024-02-01", "2024-02-05"), pd.DataFrame)

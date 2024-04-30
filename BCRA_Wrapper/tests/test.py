from BCRA_Wrapper.BCRA_Wrapper import datos_variable, principales_variables
import pandas as pd
import pytest


def test_principales_variables():
    assert isinstance(principales_variables(), pd.DataFrame)


def test_datos_variable():
    assert isinstance(datos_variable(1, "2024-02-01", "2024-02-05"), pd.DataFrame)

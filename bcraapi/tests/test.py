from bcraapi import principales_variables, datos_variable
from datetime import datetime
import pandas as pd
import pytest

variable_ids = principales_variables()["idVariable"].tolist()


def test_principales_variables():
    assert isinstance(principales_variables(), pd.DataFrame)


@pytest.mark.parametrize("id_variable", variable_ids)  # 27, 28, 29
def test_datos_variable(id_variable):
    df = datos_variable(id_variable, "2024-01-01", f"{datetime.today():%Y-%m-%d}")
    assert isinstance(df, pd.DataFrame) and not df.empty

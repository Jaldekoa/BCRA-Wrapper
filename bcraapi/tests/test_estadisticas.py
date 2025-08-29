from bcraapi.estadisticas import monetarias, datos_monetarias, metodologia
from datetime import datetime
import pandas as pd
import pytest

variable_ids = monetarias()["idVariable"].tolist()


def test_monetarias():
    df = monetarias()
    assert isinstance(df, pd.DataFrame) and not df.empty


def test_metodologia_void():
    df = metodologia()
    assert isinstance(df, pd.DataFrame) and not df.empty


@pytest.mark.parametrize("id_variable", variable_ids)
def test_datos_monetarias(id_variable):
    df = datos_monetarias(id_variable, hasta=f"{datetime.today():%Y-%m-%d}")
    assert (isinstance(df, pd.DataFrame) and not df.empty)


@pytest.mark.parametrize("id_variable", variable_ids)
def test_metodologia(id_variable):
    df = metodologia(id_variable)
    assert isinstance(df, pd.DataFrame) and not df.empty
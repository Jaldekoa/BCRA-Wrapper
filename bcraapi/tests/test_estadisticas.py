from bcraapi.estadisticas import monetarias, datos_monetarias, metodologia
from datetime import datetime
import pandas as pd
import pytest

variable_ids = monetarias()["idVariable"].tolist()


def test_monetarias(): # 4, 11, 13, 15
    df = monetarias()
    assert isinstance(df, pd.DataFrame) and not df.empty


@pytest.mark.parametrize("idVariable", variable_ids)
def test_datos_monetarias(idVariable):
    df = datos_monetarias(idVariable, hasta=f"{datetime.today():%Y-%m-%d}")
    assert (isinstance(df, pd.DataFrame) and not df.empty)


@pytest.mark.parametrize("idVariable", variable_ids)
def test_metodologia(idVariable):
    df = metodologia(idVariable)
    assert isinstance(df, pd.DataFrame) and not df.empty
from bcraapi.estadisticas import monetarias
from datetime import datetime
import pandas as pd
import pytest

variable_ids = monetarias()["idVariable"].tolist()


def test_monetarias():
    df = monetarias()
    assert isinstance(df, pd.DataFrame) and not df.empty


@pytest.mark.parametrize("id_variable", variable_ids)
def test_monetarias_idVariable(id_variable):
    df = monetarias(id_variable, hasta=f"{datetime.today():%Y-%m-%d}")
    assert (isinstance(df, pd.DataFrame) and not df.empty)

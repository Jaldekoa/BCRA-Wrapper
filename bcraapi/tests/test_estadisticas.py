from bcraapi.estadisticas import principales_variables, datos_variable
from datetime import datetime
import pandas as pd
import pytest

variable_ids = principales_variables()["idVariable"].tolist()
# 21,25,7919,"M2 privado, promedio móvil de 30 días, variación interanual (en %)",2021-12-31,54.4
variable_ids.remove(25)  # Error: No recent data

def test_principales_variables():
    df = principales_variables()
    assert isinstance(df, pd.DataFrame) and not df.empty


@pytest.mark.parametrize("id_variable", variable_ids)
def test_datos_variable(id_variable):
    df = datos_variable(id_variable, "2024-01-01", f"{datetime.today():%Y-%m-%d}")
    assert (isinstance(df, pd.DataFrame) and not df.empty) or id_variable == 25

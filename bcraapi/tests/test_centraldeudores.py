from bcraapi.centraldeudores import deudas, deudas_historicas, cheques_rechazados
import pandas as pd
import pytest


@pytest.mark.parametrize("identificacion", [30500010912])
def test_deudas(identificacion):
    df = deudas(identificacion)
    assert (isinstance(df, pd.DataFrame) and not df.empty)


@pytest.mark.parametrize("identificacion", [30500010912])
def test_deudas_historicas(identificacion):
    df = deudas_historicas(identificacion)
    assert (isinstance(df, pd.DataFrame) and not df.empty)


@pytest.mark.parametrize("identificacion", [30717283186])
def test_cheques_rechazados(identificacion):
    df = cheques_rechazados(identificacion)
    assert (isinstance(df, pd.DataFrame) and not df.empty)

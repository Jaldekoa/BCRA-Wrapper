from bcraapi.cheques import entidades, denunciados
import pandas as pd
import pytest


def test_entidades():
    df = entidades()
    assert isinstance(df, pd.DataFrame) and not df.empty


@pytest.mark.parametrize("codigo_entidad,numero_cheque,denunciado", [(11, 20377516, True), (11, 20377590, True)])
def test_denunciados(codigo_entidad, numero_cheque, denunciado):
    df = denunciados(codigo_entidad, numero_cheque)
    assert df['denunciado'].values == [denunciado]

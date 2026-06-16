from bcraapi.transparencia import cajas_ahorros, paquetes_productos, plazos_fijos, prestamos_prendarios, prestamos_hipotecarios, prestamos_personales, tarjetas_credito
import pandas as pd

def test_cajas_ahorros():
    df = cajas_ahorros()
    assert isinstance(df, pd.DataFrame)

def test_paquetes_productos():
    df = paquetes_productos()
    assert isinstance(df, pd.DataFrame)

def test_plazos_fijos():
    df = plazos_fijos()
    assert isinstance(df, pd.DataFrame)

def test_prestamos_prendarios():
    df = prestamos_prendarios()
    assert isinstance(df, pd.DataFrame)

def test_prestamos_hipotecarios():
    df = prestamos_hipotecarios()
    assert isinstance(df, pd.DataFrame)

def test_prestamos_personales():
    df = prestamos_personales()
    assert isinstance(df, pd.DataFrame)

def test_tarjetas_credito():
    df = tarjetas_credito()
    assert isinstance(df, pd.DataFrame)

def test_cajas_ahorros_con_entidad():
    df = cajas_ahorros(codigo_entidad=7)
    assert isinstance(df, pd.DataFrame)

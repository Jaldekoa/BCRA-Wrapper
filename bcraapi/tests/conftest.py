import pytest
import time

@pytest.fixture(autouse=True)
def delay_between_tests():
    """
    Agrega un pequeño retraso (sleep) después de cada test para evitar 
    que el servidor del BCRA cierre la conexión por exceso de peticiones.
    """
    yield
    time.sleep(1.5)

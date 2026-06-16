from .client import get_from_bcra
import pandas as pd

def cajas_ahorros(**kwargs) -> pd.DataFrame:
    """
    Obtiene la información sobre Cajas de Ahorro.
    
    Keyword Args:
        codigo_entidad (int): Filtrar por código de entidad financiera.
    """
    return get_from_bcra("/transparencia/v1.0/CajasAhorros", **kwargs)

def paquetes_productos(**kwargs) -> pd.DataFrame:
    """
    Obtiene la información sobre Paquetes de Productos.
    
    Keyword Args:
        codigo_entidad (int): Filtrar por código de entidad financiera.
    """
    return get_from_bcra("/transparencia/v1.0/PaquetesProductos", **kwargs)

def plazos_fijos(**kwargs) -> pd.DataFrame:
    """
    Obtiene la información sobre Plazos Fijos.
    
    Keyword Args:
        codigo_entidad (int): Filtrar por código de entidad financiera.
    """
    return get_from_bcra("/transparencia/v1.0/PlazosFijos", **kwargs)

def prestamos_prendarios(**kwargs) -> pd.DataFrame:
    """
    Obtiene la información sobre Préstamos Prendarios.
    
    Keyword Args:
        codigo_entidad (int): Filtrar por código de entidad financiera.
    """
    return get_from_bcra("/transparencia/v1.0/Prestamos/Prendarios", **kwargs)

def prestamos_hipotecarios(**kwargs) -> pd.DataFrame:
    """
    Obtiene la información sobre Préstamos Hipotecarios.
    
    Keyword Args:
        codigo_entidad (int): Filtrar por código de entidad financiera.
    """
    return get_from_bcra("/transparencia/v1.0/Prestamos/Hipotecarios", **kwargs)

def prestamos_personales(**kwargs) -> pd.DataFrame:
    """
    Obtiene la información sobre Préstamos Personales.
    
    Keyword Args:
        codigo_entidad (int): Filtrar por código de entidad financiera.
    """
    return get_from_bcra("/transparencia/v1.0/Prestamos/Personales", **kwargs)

def tarjetas_credito(**kwargs) -> pd.DataFrame:
    """
    Obtiene la información sobre Tarjetas de Crédito.
    
    Keyword Args:
        codigo_entidad (int): Filtrar por código de entidad financiera.
    """
    return get_from_bcra("/transparencia/v1.0/TarjetasCredito", **kwargs)

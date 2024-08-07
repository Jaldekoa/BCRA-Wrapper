# bcraapi: Python API for BCRA (Banco Central de la República Argentina)
bcraapi is a Python wrapper for BCRA APIs provided by Banco Central de la República Argentina itself.
It makes use of requests and pandas and returns the data in a pandas DataFrame.

The BCRA API does not require tokens or registration, so do not hesitate to use it.

## Installation
```commandline
pip install bcraapi
```

## APIs of the BCRA

- ### Estadísticas cambiarias v1.0
You will be able to access to resources related to exchange rate information published by the BCRA.

- ### Cheques denunciados v1.0
You will be able to consult reported, lost, stolen or adulterated checks. The information available here is provided by the financial entities operating in the country and is published without alterations.

- ### Estadísticas v2.0
You will be able to access resources related to the main variables information published by the BCRA. 


## API Cheques denunciados v1.0
### Entidades
Method to obtain the list of all the banking entities in the country with their respective entity code.

```python
from bcraapi import cheques

df = cheques.entidades()
```
#### Returns 
DataFrame with the list of all the banking entities in the country with their respective entity code.


### Denunciados
Method to know if a check from a certain entity is registered as reported or not.

```python
from bcraapi import cheques

df = cheques.denunciados(codigo_entidad=11, numero_cheque=20377516)
```
### Args
| Parameter        | Type  | Description                                                                                                                              |
|------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------|
| `codigo_entidad` | `int` | ID of the financial entity. It can be queried via `entidades()`.                                                                         |
| `numero_cheque`  | `int` | Corresponds to the check number to be consulted. |

#### Returns 
DataFrame with the result if a check is registered as reported or not.


## API Estadísticas v2.0
### Principales Variables
Method to obtain the list of all variables published by the BCRA.

```python
from bcraapi import estadisticas

df = estadisticas.principales_variables()
```

#### Returns 
DataFrame with the variables published by the BCRA.

### Datos de Variable
Method to obtain the values for the variable and date range indicated.

```python
from bcraapi import estadisticas

df = estadisticas.datos_variable(id_variable=1, desde="2024-02-01", hasta="2024-02-05")
```

### Args
| Parameter     | Type  | Description                                                                                                            |
|---------------|-------|------------------------------------------------------------------------------------------------------------------------|
| `id_variable` | `int` | ID of the desired variable. You can view all available ids and descriptions with the `principales_variables()` method. |
| `desde`       | `str` | The start date of the range to be queried, **it must be in the format YYYY-MM-DD**.                                        |
| `hasta`       | `str` | The end date of the range to be queried, it **must be in the format YYYY-MM-DD**.                                          |

#### Returns 
DataFrame with the values for the selected variable and date range.

## API Estadísticas Cambiarias v1.0
### Maestro de monedas
Method to obtain the list of all ISO currencies in force, with their respective denominations.
denomination.

```python
from bcraapi import estadisticascambiarias

df = estadisticascambiarias.maestros_divisas()
```
#### Returns 
DataFrame with the list of currencies of the BCRA.

### Cotizaciones por fecha
Method to obtain the list of all current foreign exchange rates published by the BCRA for a given date (yyyy-MM-dd).
BCRA for a given date. If no date is entered, the last existing quote will be returned.
the last existing quotation will be returned.

```python
from bcraapi import estadisticascambiarias

df = estadisticascambiarias.cotizaciones(fecha="2024-06-12")
```

### Args
| Parameter | Type  | Description                                                               |
|-----------|-------|---------------------------------------------------------------------------|
| `fecha`   | `str` | Date of the data to be consulted, it must have the format **YYYY-MM-DD**. |

#### Returns 
DataFrame with the values for the selected date.

### Evolución de moneda
Method to obtain the price evolution of a currency (ISO) in a particular date range.
If the date from and date to parameters are not entered, the last existing quote will be returned.
the last existing quote will be returned.

```python
from bcraapi import estadisticascambiarias

df = estadisticascambiarias.cotizaciones_moneda(moneda="USD")
```

### Args
| Parameter     | Type  | Description                                                                                    |
|---------------|-------|------------------------------------------------------------------------------------------------|
| `moneda`      | `str` | ISO currency. **This parameter is required**                                                   |
| `fecha_desde` | `str` | The start date of the range to be queried, **it must be in the format YYYY-MM-DD**.            |
| `fecha_hasta` | `str` | The end date of the range to be queried, **it must be in the format YYYY-MM-DD**.              |
| `limit`       | `int` | Maximum amount to be returned per application. **Must be greater than 10 and less than 1000**. |
| `ofset`       | `int` | Exclude from the answer the first N elements of the contributions to be refunded..              |

#### Returns 
Datarame with the evolution of the exchange rate of a currency.


## API Documentation:
- [APIs del Banco Central](https://www.bcra.gob.ar/BCRAyVos/catalogo-de-APIs-banco-central.asp)
- [API Estadísticas Cambiarias v1.0](https://www.bcra.gob.ar/Catalogo/apis.asp?fileName=estadisticascambiarias-v1&sectionName=estadisticascambiarias)
- [API Cheques v1.0](https://www.bcra.gob.ar/Catalogo/apis.asp?fileName=cheques-v1&sectionName=Cheques)
- [API Estadísticas v2.0](https://www.bcra.gob.ar/Catalogo/apis.asp?fileName=principales-variables-v2&sectionName=Estad%EDsticas)
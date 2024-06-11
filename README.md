# bcraapi: Python API for BCRA (Banco Central de la República Argentina)
bcraapi is a Python wrapper for BCRA APIs provided by Banco Central de la República Argentina itself.
It makes use of requests and pandas and returns the data in a pandas DataFrame.

The BCRA API does not require tokens or registration, so do not hesitate to use it.

## Installation
```commandline
pip install bcraapi
```

## APIs of the BCRA
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

## API Documentation:
- [APIs del Banco Central](https://www.bcra.gob.ar/BCRAyVos/catalogo-de-APIs-banco-central.asp)
- [API Cheques v1.0](https://www.bcra.gob.ar/Catalogo/apis.asp?fileName=cheques-v1&sectionName=Cheques)
- [API Estadísticas v2.0](https://www.bcra.gob.ar/Catalogo/apis.asp?fileName=principales-variables-v2&sectionName=Estad%EDsticas)
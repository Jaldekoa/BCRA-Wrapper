# BCRA Wrapper Documentation
This repository contains a Python wrapper to interact with the official BCRA (Banco Central de la República Argentina) API.
BCRA's API does not require tokens or registration, so feel free to use it.

## Instalation
```commandline
pip install BCRA-Wrapper
```

## Methods

### principales_variables (all variables)
Method to obtain the list of all variables published by the BCRA.

```python
import BCRA_Wrapper

BCRA_Wrapper.principales_variables()
```
#### Returns
- `pd.DataFrame`: A DataFrame containing all variables published by the BCRA.


### datos_variable (data for a single variable)
Method to obtain the values for the variable and date range indicated.

```python
import BCRA_Wrapper

BCRA_Wrapper.datos_variable(id_variable=1, desde="2024-02-01", hasta="2024-02-05")
```

#### Parameters
| Parameter     | Type  | Description                                                                                                            |
|---------------|-------|------------------------------------------------------------------------------------------------------------------------|
| `id_variable` | `int` | ID of the desired variable. You can view all available ids and descriptions with the `principales_variables()` method. |
| `desde`       | `str` | The start date of the range to be queried, it must be in the format YYYY-MM-DD.                                        |
| `hasta`       | `str` | The end date of the range to be queried, it must be in the format YYYY-MM-DD.                                          |


#### Returns
- `pd.DataFrame`: A DataFrame containing the `idVariable`, `cdSerie`, `fecha` (date) and `valor` (value) columns with data.



## API Documentation:
- [Catálogo de APIs del BCRA (online)](https://www.bcra.gob.ar/Catalogo/apis.asp?fileName=principales-variables-v1)
- [APIs Públicas: Manual para el Desarrollador (PDF)](https://www.bcra.gob.ar/Catalogo/Content/files/pdf/principales-variables-v1.pdf)

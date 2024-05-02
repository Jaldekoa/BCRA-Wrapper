# bcraapi: Python API for BCRA (Banco Central de la República Argentina)
bcraapi is a Python API for BCRA data provided by Banco Central de la República Argentina itself.
It makes use of requests and pandas and returns the data in a pandas DataFrame.

The BCRA API does not require tokens or registration, so do not hesitate to use it.

## Installation
```commandline
pip install bcraapi
```

## All variables published by the BCRA
You can easily obtain the list of all published variables through the BCRA API: 

```python
import bcraapi

df = bcraapi.principales_variables()
```

### Keyword Args
| Parameter | Type  | Description                                                                                                                                |
|-----------|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `lang`    | `str` | The currently configured languages are "es-AR" and "en-US". If this parameter is not reported, the response will be in "es-AR" by default. |


### Returns

This returns a DataFrame containing all variables published by the BCRA.

|    |   idVariable |   cdSerie | descripcion                                                                                                   | fecha      | valor      |
|---:|-------------:|----------:|:--------------------------------------------------------------------------------------------------------------|:-----------|:-----------|
|  0 |            1 |       246 | Reservas Internacionales del BCRA (en millones de dólares - cifras provisorias sujetas a cambio de valuación) | 29/04/2024 | 29.869     |
|  1 |            4 |      7927 | Tipo de Cambio Minorista ($ por USD) Comunicación B 9791 - Promedio vendedor                                  | 02/05/2024 | 918,05     |
|  2 |            5 |       272 | Tipo de Cambio Mayorista ($ por USD) Comunicación A 3500 - Referencia                                         | 02/05/2024 | 878,25     |
|  3 |            6 |      7935 | Tasa de Política Monetaria (en % n.a.)                                                                        | 02/05/2024 | 50,00      |
|  4 |            7 |      1222 | BADLAR en pesos de bancos privados (en % n.a.)                                                                | 30/04/2024 | 50,8125    |
|  5 |            8 |      7922 | TM20 en pesos de bancos privados (en % n.a.)                                                                  | 30/04/2024 | 51,2500    |
|  6 |            9 |      7920 | Tasas de interés de las operaciones de pase activas para el BCRA, a 1 día de plazo (en % n.a.)                | 02/05/2024 | 75,00      |
|  7 |           10 |      7921 | Tasas de interés de las operaciones de pase pasivas para el BCRA, a 1 día de plazo (en % n.a.)                | 02/05/2024 | 50,00      |
|  8 |           11 |      3139 | Tasas de interés por préstamos entre entidades financiera privadas (BAIBAR) (en % n.a.)                       | 30/04/2024 | 61,60      |
|  9 |           12 |      1212 | Tasas de interés por depósitos a 30 días de plazo en entidades financieras (en % n.a.)                        | 30/04/2024 | 51,02      |
| 10 |           13 |      7924 | Tasa de interés de préstamos por adelantos en cuenta corriente                                                | 30/04/2024 | 64,06      |
| 11 |           14 |      7925 | Tasa de interés de préstamos personales                                                                       | 30/04/2024 | 85,90      |
| 12 |           15 |       250 | Base monetaria - Total (en millones de pesos)                                                                 | 29/04/2024 | 14.034.425 |
| 13 |           16 |       251 | Circulación monetaria (en millones de pesos)                                                                  | 29/04/2024 | 8.828.413  |
| 14 |           17 |       251 | Billetes y monedas en poder del público (en millones de pesos)                                                | 29/04/2024 | 7.972.358  |
| 15 |           18 |       296 | Efectivo en entidades financieras (en millones de pesos)                                                      | 29/04/2024 | 856.055    |
| 16 |           19 |       252 | Depósitos de los bancos en cta. cte. en pesos en el BCRA (en millones de pesos)                               | 29/04/2024 | 5.206.012  |
| 17 |           21 |       444 | Depósitos en efectivo en las entidades financieras - Total (en millones de pesos)                             | 29/04/2024 | 83.992.914 |
| 18 |           22 |       446 | En cuentas corrientes (neto de utilización FUCO) (en millones de pesos)                                       | 29/04/2024 | 16.502.711 |
| 19 |           23 |       450 | En Caja de ahorros (en millones de pesos)                                                                     | 29/04/2024 | 28.177.560 |
| 20 |           24 |       452 | A plazo (incluye inversiones y excluye CEDROS) (en millones de pesos)                                         | 29/04/2024 | 35.051.621 |
| 21 |           25 |      7919 | M2 privado, promedio móvil de 30 días, variación interanual (en %)                                            | 30/04/2024 | 144,9      |
| 22 |           26 |       392 | Préstamos de las entidades financieras al sector privado (en millones de pesos)                               | 29/04/2024 | 26.460.065 |
| 23 |           27 |      7931 | Inflación mensual (variación en %)                                                                            | 31/03/2024 | 11,0       |
| 24 |           28 |      7932 | Inflación interanual (variación en % i.a.)                                                                    | 31/03/2024 | 287,9      |
| 25 |           29 |      7933 | Inflación esperada - REM próximos 12 meses - MEDIANA (variación en % i.a)                                     | 31/03/2024 | 120,0      |
| 26 |           30 |      3540 | CER (Base 2.2.2002=1)                                                                                         | 02/05/2024 | 356,3248   |
| 27 |           31 |      7913 | Unidad de Valor Adquisitivo (UVA) (en pesos -con dos decimales-, base 31.3.2016=14.05)                        | 02/05/2024 | 893,60     |
| 28 |           32 |      7914 | Unidad de Vivienda (UVI) (en pesos -con dos decimales-, base 31.3.2016=14.05)                                 | 02/05/2024 | 694,67     |
| 29 |           34 |      7936 | Tasa de Política Monetaria (en % e.a.)                                                                        | 02/05/2024 | 64,82      |
| 30 |           35 |      7937 | BADLAR en pesos de bancos privados (en % e.a.)                                                                | 30/04/2024 | 64,4000    |
| 31 |           40 |      7988 | Índice para Contratos de Locación (ICL-Ley 27.551, con dos decimales, base 30.6.20=1)                         | 02/05/2024 | 12,43      |
| 32 |           41 |      7990 | Tasas de interés de las operaciones de pase pasivas para el BCRA, a 1 día de plazo (en % e.a.)                | 02/05/2024 | 64,82      |
| 33 |           42 |       266 | Pases pasivos para el BCRA - Saldos (en millones de pesos)                                                    | 29/04/2024 | 33.307.225 |


## Single variable values and date range indicated
You can easily obtain the values for the specific variable and date range indicated.

```python
import bcraapi

df = bcraapi.datos_variable(id_variable=1, desde="2024-01-01", hasta="2024-02-01")
```

### Args
| Parameter     | Type  | Description                                                                                                            |
|---------------|-------|------------------------------------------------------------------------------------------------------------------------|
| `id_variable` | `int` | ID of the desired variable. You can view all available ids and descriptions with the `principales_variables()` method. |
| `desde`       | `str` | The start date of the range to be queried, it must be in the format YYYY-MM-DD.                                        |
| `hasta`       | `str` | The end date of the range to be queried, it must be in the format YYYY-MM-DD.                                          |


### Keyword Args
| Parameter | Type  | Description                                                                                                                                |
|-----------|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `lang`    | `str` | The currently configured languages are "es-AR" and "en-US". If this parameter is not reported, the response will be in "es-AR" by default. |

### Returns

This returns a DataFrame containing the `idVariable`, `cdSerie`, `fecha` (date) and `valor` (value) columns with data.

|    |   idVariable | fecha      |   valor |
|---:|-------------:|:-----------|--------:|
|  0 |            1 | 02/01/2024 |  23.47  |
|  1 |            1 | 03/01/2024 |  23.677 |
|  2 |            1 | 04/01/2024 |  23.835 |
|  3 |            1 | 05/01/2024 |  24.119 |
|  4 |            1 | 08/01/2024 |  23.233 |
|  5 |            1 | 09/01/2024 |  23.286 |
|  6 |            1 | 10/01/2024 |  23.411 |
|  7 |            1 | 11/01/2024 |  23.571 |
|  8 |            1 | 12/01/2024 |  23.98  |
|  9 |            1 | 15/01/2024 |  24.001 |
| 10 |            1 | 16/01/2024 |  23.972 |
| 11 |            1 | 17/01/2024 |  24.167 |
| 12 |            1 | 18/01/2024 |  24.3   |
| 13 |            1 | 19/01/2024 |  24.427 |
| 14 |            1 | 22/01/2024 |  24.488 |
| 15 |            1 | 23/01/2024 |  24.675 |
| 16 |            1 | 24/01/2024 |  24.848 |
| 17 |            1 | 25/01/2024 |  24.859 |
| 18 |            1 | 26/01/2024 |  25.007 |
| 19 |            1 | 29/01/2024 |  25.158 |
| 20 |            1 | 30/01/2024 |  25.105 |
| 21 |            1 | 31/01/2024 |  27.642 |
| 22 |            1 | 01/02/2024 |  27.072 |


## API Documentation:
- [Catálogo de APIs del BCRA (online)](https://www.bcra.gob.ar/Catalogo/apis.asp?fileName=principales-variables-v1)
- [APIs Públicas: Manual para el Desarrollador (PDF)](https://www.bcra.gob.ar/Catalogo/Content/files/pdf/principales-variables-v1.pdf)

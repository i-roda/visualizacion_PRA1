# Visualización de datos
## PRA1 - Selección del conjunto de datos

Asignatura: M2.859 / Semestre: 2023-2 / Fecha: 04-05-2024

## Descripción del repositorio
Este repositorio forma parte de la **Práctica (parte I)** de la asignatura **Visualización de datos (M2.859)** del
Máster Universitario de Ciencia de Datos (UOC). La primera parte de la práctica consiste en la selección de un conjunto de datos que será usado posteriormente en el proyecto de creación de una visualización de datos. 

El dataset final, que se utilizará en la segunda parte de la práctica, se ha obtenido combinando los datasets:
* [CO2 and Greenhouse Gas Emissions by Our World in Data](https://github.com/owid/co2-data)
* [Energy by Our World in Data](https://github.com/owid/energy-data)
* [Continents according to Our World in Data](https://ourworldindata.org/world-region-map-definitions)

También se ha generado un nuevo *codebook* donde se explican las variables del dataset combinado a partir de los *codebooks* de los datasets originales.

## Estructura del Repositorio
### Data
Contiene los datasets y codebooks originales, así como el dataset final y su correspondiente codebook:
- `continents-according-to-our-world-in-data.csv`: Lista de países y sus respectivos continentes.
- `owid-co2-codebook.csv`: Codebook del dataset de emisiones de CO2.
- `owid-co2-data.csv`: Datos sobre emisiones de CO2 y otros gases de efecto invernadero.
- `owid-energy-codebook.csv`: Codebook del dataset de energía.
- `owid-energy-data.csv`: Datos sobre consumo y producción de energía.
- `pra1_visualizacion.csv`: Dataset final combinado.
- `pra1_visualizacion_codebook.csv`: Codebook del dataset final.

### Source
Incluye el script en Python y el notebook de Jupyter que realizan el procesamiento de datos:
- `PRA1_Visualizacion.py`: Script Python que genera el dataset final y su codebook.
- `PRA1_Visualizacion.ipynb`: Notebook de Jupyter que permite visualizar paso a paso el mismo proceso.

## Licencia
Este proyecto está licenciado bajo la Licencia Pública General de GNU, versión 3 (GPL-3.0). Puedes consultar el texto completo de la licencia en el archivo `LICENSE` incluido en este repositorio o a través de [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).


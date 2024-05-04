#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np 

# Cargamos los datos de los tres archivos csv
data_energy = pd.read_csv('./data/owid-energy-data.csv')
data_co2 = pd.read_csv('./data/owid-co2-data.csv')
data_continents = pd.read_csv('./data/continents-according-to-our-world-in-data.csv')

# Añadimos el continente correspondiente a cada país de data_co2
merged_data = pd.merge(data_co2, data_continents[['Code', 'Continent']], left_on='iso_code', right_on='Code', how='left')
# Eliminamos la columna 'Code'
merged_data = merged_data.drop(columns=['Code'])
# Renombramos la columna 'Continent' a 'continent'
merged_data = merged_data.rename(columns={'Continent': 'continent'}) 

# Movemos la columna 'continent' a la segunda posición del dataframe
columns = list(merged_data.columns)
columns.remove('continent')
columns.insert(1, 'continent')
merged_data = merged_data[columns]

# Combinamos el dataframe anterior con el dataframe data_energy
# Eliminamos de data_energy las columnas que no vamos a incluir
columns_to_exclude = ['energy_per_capita', 'energy_per_gdp', 'gdp', 'iso_code', 'population', 'primary_energy_consumption']
data_energy = data_energy.drop(columns=columns_to_exclude)

# Combinamos los dos los dataframes
merged_data = pd.merge(merged_data, data_energy, on=['country', 'year'], how='left')

# Eliminamos los registros sin 'iso_code'
merged_data = merged_data.dropna(subset=['iso_code'])


# Creamos un nuevo archivo csv con el dataframe final
merged_data.to_csv('pra1_visualizacion.csv', index=False)

# Creamos un nuevo codebook para el nuevo csv
# Cargamos los datos
codebook_energy = pd.read_csv('./data/owid-energy-codebook.csv')
codebook_co2 = pd.read_csv('./data/owid-co2-codebook.csv')

# Concatenamos los dataframes
codebook = pd.concat([codebook_energy, codebook_co2], ignore_index=True)

# Eliminamos las filas duplicadas
codebook = codebook.drop_duplicates()

# Añadimos la información de la variable 'continent' 
new_row = pd.DataFrame({
    'column': ['continent'],
    'description': ['Continent - Continent corresponding to each country'],
    'unit': [np.nan],  
    'source': ['Our World in Data - Regions (2022)'] 
})

part1 = codebook.iloc[:1]  
part2 = codebook.iloc[1:]  
codebook = pd.concat([part1, new_row, part2], ignore_index=True)

# Creamos un nuevo archivo csv con el codebook final
codebook.to_csv('pra1_visualizacion_codebook.csv', index=False)






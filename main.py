'''
    PROMPT 1: Como obter um ponto aleatório que esteja dentro de uma geometria, considerando que a feição esteja armazenada em um arquivo geojson?
    PROMPT 2: troque o código para ao invés de selecionar uma geometria randômica, obtenha um ponto aleatório para todas as feature de uma featurecollection
'''

import geopandas as gpd
from shapely.geometry import shape, Point
import random

# Carregue o arquivo GeoJSON usando geopandas
file_path = 'caminho/do/seu/arquivo.geojson'
gdf = gpd.read_file(file_path)

# Função para gerar um ponto aleatório dentro de uma geometria
def generate_random_point(geometry):
    minx, miny, maxx, maxy = geometry.bounds
    while True:
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        point = Point(x, y)
        if point.within(geometry):
            return point

# Adicione uma coluna 'random_point' ao GeoDataFrame com pontos aleatórios
gdf['random_point'] = gdf['geometry'].apply(generate_random_point)

# Exiba o GeoDataFrame resultante
print(gdf[['geometry', 'random_point']])


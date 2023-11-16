'''
    PROMPT 1: Como obter um ponto aleatório que esteja dentro de uma geometria, considerando que a feição esteja armazenada em um arquivo geojson?
'''

import geopandas as gpd
from shapely.geometry import shape, Point
import random

# Carregue o arquivo GeoJSON usando geopandas
file_path = 'caminho/do/seu/arquivo.geojson'
gdf = gpd.read_file(file_path)

# Selecione uma geometria aleatória do GeoDataFrame
random_index = random.randint(0, len(gdf) - 1)
random_geometry = gdf['geometry'].iloc[random_index]

# Gere um ponto aleatório dentro da geometria
minx, miny, maxx, maxy = random_geometry.bounds
while True:
    x = random.uniform(minx, maxx)
    y = random.uniform(miny, maxy)
    point = Point(x, y)
    if point.within(random_geometry):
        break

print(f'Ponto aleatório dentro da geometria: {point}')

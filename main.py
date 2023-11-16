'''
    PROMPT 1: Como obter um ponto aleatório que esteja dentro de uma geometria, considerando que a feição esteja armazenada em um arquivo geojson?
    PROMPT 2: troque o código para ao invés de selecionar uma geometria randômica, obtenha um ponto aleatório para todas as feature de uma featurecollection
'''
import geopandas as gpd
from shapely.geometry import shape, Point
import random

def generate_random_point(geometry):
    # Gere um ponto aleatório dentro da geometria
    minx, miny, maxx, maxy = geometry.bounds
    
    while True:
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        point = Point(x, y)
        
        if point.within(geometry):  # exceção se a geometria for multipolygon
            return point

# Carregue o arquivo GeoJSON usando geopandas
file_path = 'geojsons/alegre_min.json'
gdf = gpd.read_file(file_path)

# Selecione uma geometria aleatória do GeoDataFrame

for index in range(0, len(gdf) - 1):

    geometry = gdf['geometry'].iloc[index]
    local_id = gdf['idd'].iloc[index]
    local_pri = gdf['primario'].iloc[index]
    local_sec = gdf['secundario'].iloc[index]

    if geometry.geom_type == 'Polygon':
        point = generate_random_point(geometry)

        print(f'ID: {local_id} {local_pri}. Ponto aleatório gerado: {point}')
    else:
        print(f'ERRO! ID: {local_id} {local_pri}. Geometria: {geometry.geom_type}')

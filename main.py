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

    random.seed(1)
    while True:
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        point = Point(x, y)
        
        if point.within(geometry):  # exceção se a geometria for multipolygon
            return point


geojsons_unidades = {
    1: 'alegre.json',
    2: 'goiabeiras.json',
    3: 'maruipe.json',
    4: 'sao_mateus.json',
    5: 'rive.json',
    6: 'jeronimo_monteiro.json',
#    8: 'sao_jose_do_calcado.geojson'
}

print('INSERT INTO public.tb_locais(idd, primario, secundario, terciario, zona, localizacao, filename, id_unidade) VALUES ')

for key, value in geojsons_unidades.items():
    
    # Carregue o arquivo GeoJSON usando geopandas
    file_path = 'geojsons/' + value
    gdf = gpd.read_file(file_path)

    # Selecione uma geometria aleatória do GeoDataFrame
    print()
    for index in range(0, len(gdf) - 1):

        local_id = gdf['idd'].iloc[index]
        local_pri = gdf['primario'].iloc[index]
        local_sec = gdf['secundario'].iloc[index]
        local_ter = gdf['terciario'].iloc[index]
        local_zona = gdf['zona'].iloc[index]

        geometry = gdf['geometry'].iloc[index]
        if geometry.geom_type == 'Polygon':
            point = generate_random_point(geometry)

        else:
            point = 'null'

        print(f'(\'{local_id}\', \'{local_pri}\', \'{local_sec}\', \'{local_ter}\', {local_zona}, \'{point}\', \'{value}\', \'{key}\')')


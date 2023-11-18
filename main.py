import geopandas as gpd
from shapely.geometry import Point
import random


def generate_random_point(geometry):
    # Gere um ponto aleatório dentro da geometria
    minx, miny, maxx, maxy = geometry.bounds

    while True:
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        point = Point(x, y)

        if point.within(geometry):  # resulta em exceção se a geometria for multipolygon
            return point


def get_random_point(geometry):
    # Função para obter um ponto aleatório dentro de uma geometria (suporta MultiPolygon)
    random.seed(1) # semente para manter o mesmo resultado entre execuções

    if geometry.geom_type == 'Polygon':
        return generate_random_point(geometry)
    elif geometry.geom_type == 'MultiPolygon':
        polygon = random.choice(geometry.geoms)
        return generate_random_point(polygon)
    else:
        raise ValueError(f"Tipo de geometria não suportado: {geometry.geom_type}")


def clean_atributes(gdf, attribute):
    value = gdf[attribute].iloc[index]

    if not value or value == 'None':
        return 'null'
    else:
        return '\'' + value.strip() + '\''


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
    print('--' + value)
    for index in range(0, len(gdf) - 1):

        local_id = gdf['idd'].iloc[index]
        local_pri = clean_atributes(gdf, 'primario')
        local_sec = clean_atributes(gdf, 'secundario')
        local_ter = clean_atributes(gdf, 'terciario')

        # converte para inteiro alguns valores que estava em float, exceto quando o valor é um NaN
        # como não consegui comparar diretamente com o valor NaN converti para string e fiz a comparação
        local_zona = int(gdf['zona'].iloc[index]) if str(gdf['zona'].iloc[index]) != 'nan' else 'null'

        geometry = gdf['geometry'].iloc[index]

        point = '\'' + str(get_random_point(geometry)) + '\''

        print(f'({local_id}, {local_pri}, {local_sec}, {local_ter}, {local_zona}, {point}, \'{value}\', {key}),')


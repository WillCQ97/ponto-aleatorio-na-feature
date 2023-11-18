# Geração de pontos aleatoriamente dentro de um polígono

- Esse código realiza o processamento de arquivos no formato geojson, que contém geometrias espaciais, para geração de um ponto aleatório dentro das coordenadas dessa geometria. É esperado que a geometria esteja no **formato Polygon ou Multipolygon**.
- O funcionamento é baseado na obtenção das coordenadas dos vértices do polígono e então usando a função rand, gerar coordenadas dentro desse limite.
- Trata-se de um código simples de execução praticamente única.
- Ao final é gerado um sql para inserção dos pontos na tabela de locações do **projeto scp-ods**.
- O código inicial foi gerado com uso do chatGPT. A versão final foi manualmente alterada com base nas versões geradas pelo chat.
- Execução utilizando `Python 3.11.5` e as bibliotecas `geopandas` e `shapely`. Foi criado um ambiente com uso do `miniconda` e usado o `pip` para instalação das bibliotecas.

  - `pip install geopandas shapely`

- O objetivo foi a geração de pontos para marcar os locais presentes nas unidades da UFES, sendo os quatro _campi_ mais algumas áreas experimentais.
- Para tal foram utilizadas os arquivos json do mapeamento das unidades feito pela equipe de prodesing:
  - alegre.json
  - goiabeiras.json
  - jeronimo_monteiro.json
  - maruipe.json
  - rive.json
  - sao_jose_do_calcado.geojson
  - sao_mateus.json

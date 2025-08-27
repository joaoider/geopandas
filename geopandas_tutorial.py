#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 Tutorial Profissional de GeoPandas
=====================================

Este script apresenta uma introdução prática ao GeoPandas, uma biblioteca Python
para trabalhar com dados geoespaciais de forma eficiente e intuitiva.

Autor: Assistente IA
Data: 2024
"""

# =============================================================================
# IMPORTAÇÕES E CONFIGURAÇÕES
# =============================================================================

def instalar_dependencias():
    """Instala e verifica as dependências necessárias."""
    try:
        import geopandas as gpd
        print("✅ GeoPandas já está instalado")
        return gpd
    except ImportError:
        print("📦 Instalando GeoPandas...")
        import subprocess
        subprocess.check_call(["pip", "install", "geopandas"])
        import geopandas as gpd
        print("✅ GeoPandas instalado com sucesso!")
        return gpd

def importar_bibliotecas():
    """Importa todas as bibliotecas necessárias."""
    # Bibliotecas principais
    import geopandas as gpd
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from shapely.geometry import Point, Polygon, LineString
    
    # Configurações de visualização
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 10
    
    # Configurações do GeoPandas
    gpd.options.use_pygeos = False
    
    print("✅ Bibliotecas importadas com sucesso!")
    return gpd, pd, np, plt

# =============================================================================
# CRIAÇÃO DE DADOS DE EXEMPLO
# =============================================================================

def criar_dados_exemplo():
    """Cria dados geoespaciais de exemplo para demonstração."""
    
    # Coordenadas de pontos (longitude, latitude)
    coordenadas = [
        (-74.006, 40.7128),  # Nova York
        (-87.6298, 41.8781), # Chicago
        (-118.2437, 34.0522), # Los Angeles
        (-95.3698, 29.7604),  # Houston
        (-80.1918, 25.7617)   # Miami
    ]
    
    # Dados associados aos pontos
    dados = {
        'cidade': ['Nova York', 'Chicago', 'Los Angeles', 'Houston', 'Miami'],
        'populacao': [8336817, 2693976, 3979576, 2320268, 454279],
        'estado': ['NY', 'IL', 'CA', 'TX', 'FL'],
        'regiao': ['Nordeste', 'Centro-Oeste', 'Oeste', 'Sul', 'Sul']
    }
    
    # Criando geometrias Point
    geometrias = [Point(lon, lat) for lon, lat in coordenadas]
    
    # Criando GeoDataFrame
    gdf = gpd.GeoDataFrame(dados, geometry=geometrias, crs='EPSG:4326')
    
    return gdf

def analisar_dados(gdf):
    """Analisa e exibe informações sobre o GeoDataFrame."""
    print("📊 INFORMAÇÕES DO GEODATAFRAME:")
    print("=" * 50)
    
    # Tipo de objeto
    print(f"Tipo: {type(gdf)}")
    
    # Sistema de coordenadas (CRS)
    print(f"\nSistema de Coordenadas (CRS): {gdf.crs}")
    
    # Dimensões
    print(f"\nDimensões: {gdf.shape}")
    
    # Colunas
    print(f"\nColunas: {list(gdf.columns)}")
    
    # Tipos de dados
    print(f"\nTipos de dados:")
    print(gdf.dtypes)
    
    # Estatísticas descritivas
    print(f"\nEstatísticas descritivas:")
    print(gdf.describe())

# =============================================================================
# VISUALIZAÇÕES
# =============================================================================

def criar_mapa_cidades(gdf, coluna_cor='populacao', titulo='Cidades dos Estados Unidos'):
    """Cria um mapa personalizado das cidades."""
    
    # Criando figura e eixos
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Plotando as cidades
    gdf.plot(
        column=coluna_cor,
        ax=ax,
        cmap='viridis',
        legend=True,
        legend_kwds={
            'label': 'População',
            'orientation': 'vertical',
            'shrink': 0.8
        },
        markersize=100,
        edgecolor='black',
        linewidth=1
    )
    
    # Adicionando rótulos das cidades
    for idx, row in gdf.iterrows():
        ax.annotate(
            row['cidade'],
            xy=(row.geometry.x, row.geometry.y),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=10,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7)
        )
    
    # Configurações do mapa
    ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # Adicionando bordas dos estados (simplificado)
    ax.set_xlim(-120, -70)
    ax.set_ylim(25, 45)
    
    plt.tight_layout()
    return fig, ax

def criar_visualizacoes_multiplas(gdf):
    """Cria múltiplas visualizações dos dados."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Análise Geoespacial das Cidades', fontsize=18, fontweight='bold')
    
    # 1. Mapa por população
    gdf.plot(
        column='populacao',
        ax=axes[0,0],
        cmap='plasma',
        legend=True,
        markersize=80
    )
    axes[0,0].set_title('Distribuição por População', fontweight='bold')
    axes[0,0].set_xlim(-120, -70)
    axes[0,0].set_ylim(25, 45)
    
    # 2. Mapa por região
    gdf.plot(
        column='regiao',
        ax=axes[0,1],
        categorical=True,
        legend=True,
        markersize=80
    )
    axes[0,1].set_title('Distribuição por Região', fontweight='bold')
    axes[0,1].set_xlim(-120, -70)
    axes[0,1].set_ylim(25, 45)
    
    # 3. Gráfico de barras - População por cidade
    gdf.plot.bar(x='cidade', y='populacao', ax=axes[1,0], color='skyblue')
    axes[1,0].set_title('População por Cidade', fontweight='bold')
    axes[1,0].tick_params(axis='x', rotation=45)
    axes[1,0].set_ylabel('População')
    
    # 4. Gráfico de pizza - Distribuição por região
    regiao_counts = gdf['regiao'].value_counts()
    axes[1,1].pie(regiao_counts.values, labels=regiao_counts.index, autopct='%1.1f%%')
    axes[1,1].set_title('Distribuição por Região', fontweight='bold')
    
    plt.tight_layout()
    return fig, axes

# =============================================================================
# OPERAÇÕES ESPACIAIS
# =============================================================================

def operacoes_espaciais(gdf):
    """Demonstra operações espaciais básicas."""
    print("🔍 OPERAÇÕES ESPACIAIS:")
    print("=" * 30)
    
    # 1. Filtragem espacial por região
    cidades_sul = gdf[gdf['regiao'] == 'Sul']
    print(f"Cidades do Sul: {list(cidades_sul['cidade'])}")
    
    # 2. Cálculo de distâncias
    print("\n📏 CÁLCULO DE DISTÂNCIAS:")
    print("=" * 30)
    
    # Convertendo para projeção adequada para cálculos de distância
    cidades_proj = gdf.to_crs('EPSG:3857')  # Web Mercator
    
    # Calculando distâncias entre Nova York e outras cidades
    ny_point = cidades_proj[cidades_proj['cidade'] == 'Nova York'].geometry.iloc[0]
    
    for idx, row in cidades_proj.iterrows():
        if row['cidade'] != 'Nova York':
            distancia = ny_point.distance(row.geometry) / 1000  # Convertendo para km
            print(f"Nova York → {row['cidade']}: {distancia:.1f} km")
    
    # 3. Estatísticas por região
    print("\n📊 ESTATÍSTICAS POR REGIÃO:")
    print("=" * 30)
    
    estatisticas_regiao = gdf.groupby('regiao').agg({
        'populacao': ['count', 'sum', 'mean'],
        'cidade': 'count'
    }).round(2)
    
    estatisticas_regiao.columns = ['Número de Cidades', 'População Total', 'População Média']
    print(estatisticas_regiao)

def criar_areas_influencia(gdf, raio_km=300):
    """Cria áreas de influência ao redor das cidades."""
    
    # Convertendo para projeção adequada
    gdf_proj = gdf.to_crs('EPSG:3857')
    
    # Criando buffers (áreas de influência)
    areas_influencia = gdf_proj.copy()
    areas_influencia['geometry'] = gdf_proj.geometry.buffer(raio_km * 1000)  # Convertendo km para metros
    
    # Convertendo de volta para WGS84
    areas_influencia = areas_influencia.to_crs('EPSG:4326')
    
    return areas_influencia

def visualizar_areas_influencia(gdf, areas_influencia):
    """Visualiza as áreas de influência das cidades."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Plotando áreas de influência
    areas_influencia.plot(
        ax=ax,
        alpha=0.3,
        color='lightblue',
        edgecolor='blue',
        linewidth=1
    )
    
    # Plotando cidades
    gdf.plot(
        ax=ax,
        color='red',
        markersize=100,
        edgecolor='black',
        linewidth=2
    )
    
    # Adicionando rótulos
    for idx, row in gdf.iterrows():
        ax.annotate(
            row['cidade'],
            xy=(row.geometry.x, row.geometry.y),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=10,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8)
        )
    
    ax.set_title('Áreas de Influência das Cidades (300 km)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-120, -70)
    ax.set_ylim(25, 45)
    
    plt.tight_layout()
    return fig, ax

# =============================================================================
# EXPORTAÇÃO DE DADOS
# =============================================================================

def salvar_dados(gdf):
    """Salva os dados em diferentes formatos."""
    print("💾 SALVANDO DADOS:")
    print("=" * 20)
    
    try:
        # 1. GeoJSON (formato web-friendly)
        gdf.to_file('cidades_exemplo.geojson', driver='GeoJSON')
        print("✅ Dados salvos em GeoJSON")
        
        # 2. Shapefile (formato padrão GIS)
        gdf.to_file('cidades_exemplo.shp', driver='ESRI Shapefile')
        print("✅ Dados salvos em Shapefile")
        
        # 3. CSV com coordenadas separadas
        cidades_csv = gdf.copy()
        cidades_csv['longitude'] = cidades_csv.geometry.x
        cidades_csv['latitude'] = cidades_csv.geometry.y
        cidades_csv = cidades_csv.drop(columns=['geometry'])
        cidades_csv.to_csv('cidades_exemplo.csv', index=False)
        print("✅ Dados salvos em CSV")
        
        # 4. Parquet (formato eficiente para grandes datasets)
        gdf.to_parquet('cidades_exemplo.parquet')
        print("✅ Dados salvos em Parquet")
        
    except Exception as e:
        print(f"❌ Erro ao salvar dados: {e}")
    
    print("\n📁 Arquivos criados:")
    import os
    for arquivo in ['cidades_exemplo.geojson', 'cidades_exemplo.shp', 'cidades_exemplo.csv', 'cidades_exemplo.parquet']:
        if os.path.exists(arquivo):
            tamanho = os.path.getsize(arquivo) / 1024  # KB
            print(f"  • {arquivo}: {tamanho:.1f} KB")

def exibir_dicas():
    """Exibe dicas e boas práticas."""
    print("🔧 DICAS E BOAS PRÁTICAS:")
    print("=" * 40)
    
    dicas = [
        "1. Sempre verifique o CRS dos seus dados antes de fazer operações espaciais",
        "2. Use projeções adequadas para cálculos de distância e área",
        "3. Considere o uso de índices espaciais para datasets grandes",
        "4. Valide a geometria dos seus dados antes de processá-los",
        "5. Use formatos de arquivo apropriados para cada caso de uso",
        "6. Sempre documente as transformações de coordenadas",
        "7. Considere o uso de bibliotecas complementares (shapely, pyproj)",
        "8. Teste suas operações espaciais com dados de exemplo pequenos"
    ]
    
    for dica in dicas:
        print(f"  {dica}")
    
    print("\n📚 Recursos Adicionais:")
    recursos = [
        "• Documentação oficial: https://geopandas.org/",
        "• Exemplos práticos: https://geopandas.org/examples/",
        "• Comunidade: https://github.com/geopandas/geopandas",
        "• Tutorial interativo: https://geopandas.org/getting_started.html"
    ]
    
    for recurso in recursos:
        print(f"  {recurso}")

# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def main():
    """Função principal que executa todo o tutorial."""
    print("🚀 INICIANDO TUTORIAL PROFISSIONAL DE GEOPANDAS")
    print("=" * 60)
    
    # 1. Instalação e importação
    gpd = instalar_dependencias()
    gpd, pd, np, plt = importar_bibliotecas()
    
    # 2. Criação de dados
    print("\n🌍 Criando dados de exemplo...")
    cidades_gdf = criar_dados_exemplo()
    print("✅ Dados criados com sucesso!")
    
    # 3. Análise dos dados
    print("\n📊 Analisando dados...")
    analisar_dados(cidades_gdf)
    
    # 4. Visualizações
    print("\n🗺️ Criando visualizações...")
    
    # Mapa básico
    fig1, ax1 = criar_mapa_cidades(cidades_gdf)
    plt.show()
    
    # Visualizações múltiplas
    fig2, axes2 = criar_visualizacoes_multiplas(cidades_gdf)
    plt.show()
    
    # 5. Operações espaciais
    print("\n🔍 Executando operações espaciais...")
    operacoes_espaciais(cidades_gdf)
    
    # 6. Áreas de influência
    print("\n🚀 Criando áreas de influência...")
    areas_influencia = criar_areas_influencia(cidades_gdf, raio_km=300)
    fig3, ax3 = visualizar_areas_influencia(cidades_gdf, areas_influencia)
    plt.show()
    
    # 7. Salvando dados
    print("\n💾 Salvando dados...")
    salvar_dados(cidades_gdf)
    
    # 8. Dicas e boas práticas
    print("\n🔧 Exibindo dicas...")
    exibir_dicas()
    
    # 9. Conclusão
    print("\n" + "=" * 60)
    print("🎉 TUTORIAL CONCLUÍDO COM SUCESSO!")
    print("=" * 60)
    print("\n✅ O que foi aprendido:")
    print("  • Instalação e configuração do GeoPandas")
    print("  • Criação e manipulação de dados geoespaciais")
    print("  • Visualizações profissionais e informativas")
    print("  • Operações espaciais básicas e avançadas")
    print("  • Exportação em múltiplos formatos")
    print("  • Boas práticas para uso profissional")
    print("\n🚀 Agora você está pronto para usar o GeoPandas profissionalmente!")
    print("\n---")
    print("Desenvolvido com ❤️ usando GeoPandas")
    print("Última atualização: 2024")

if __name__ == "__main__":
    main()

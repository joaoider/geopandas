#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Exemplo Rápido de GeoPandas
===============================

Este é um exemplo simples e rápido para demonstrar o GeoPandas em ação.
Execute este arquivo para ver resultados imediatos!
"""

def exemplo_rapido():
    """Exemplo rápido e funcional de GeoPandas."""
    
    print("🚀 EXEMPLO RÁPIDO DE GEOPANDAS")
    print("=" * 40)
    
    try:
        # Importando bibliotecas
        import geopandas as gpd
        import matplotlib.pyplot as plt
        from shapely.geometry import Point
        
        print("✅ Bibliotecas importadas com sucesso!")
        
        # Criando dados simples
        print("\n🌍 Criando dados de exemplo...")
        
        # Coordenadas de algumas cidades brasileiras
        coordenadas = [
            (-46.6388, -23.5489),  # São Paulo
            (-43.1729, -22.9068),  # Rio de Janeiro
            (-38.5011, -12.9714),  # Salvador
            (-34.8811, -8.0476),   # Recife
            (-49.2666, -25.4289)   # Curitiba
        ]
        
        # Dados das cidades
        dados = {
            'cidade': ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Recife', 'Curitiba'],
            'populacao': [12325232, 6747816, 2886698, 1653461, 1948626],
            'regiao': ['Sudeste', 'Sudeste', 'Nordeste', 'Nordeste', 'Sul']
        }
        
        # Criando geometrias
        geometrias = [Point(lon, lat) for lon, lat in coordenadas]
        
        # Criando GeoDataFrame
        gdf = gpd.GeoDataFrame(dados, geometry=geometrias, crs='EPSG:4326')
        
        print(f"✅ Criados {len(gdf)} pontos de dados!")
        
        # Informações básicas
        print(f"\n📊 Informações do GeoDataFrame:")
        print(f"  • Dimensões: {gdf.shape}")
        print(f"  • CRS: {gdf.crs}")
        print(f"  • Colunas: {list(gdf.columns)}")
        
        # Estatísticas simples
        print(f"\n📈 Estatísticas:")
        print(f"  • População total: {gdf['populacao'].sum():,}")
        print(f"  • População média: {gdf['populacao'].mean():,.0f}")
        print(f"  • Cidade maior: {gdf.loc[gdf['populacao'].idxmax(), 'cidade']}")
        
        # Visualização simples
        print(f"\n🗺️ Criando visualização...")
        
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        
        # Plotando as cidades
        gdf.plot(
            column='populacao',
            ax=ax,
            cmap='viridis',
            legend=True,
            legend_kwds={'label': 'População'},
            markersize=100,
            edgecolor='black',
            linewidth=1
        )
        
        # Adicionando rótulos
        for idx, row in gdf.iterrows():
            ax.annotate(
                row['cidade'],
                xy=(row.geometry.x, row.geometry.y),
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=9,
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8)
            )
        
        # Configurações do mapa
        ax.set_title('Cidades Brasileiras - Exemplo Rápido', fontsize=14, fontweight='bold')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.grid(True, alpha=0.3)
        
        # Ajustando limites para o Brasil
        ax.set_xlim(-52, -34)
        ax.set_ylim(-26, -8)
        
        plt.tight_layout()
        
        print("✅ Visualização criada com sucesso!")
        print("🖼️  Abrindo gráfico...")
        
        plt.show()
        
        # Salvando dados
        print(f"\n💾 Salvando dados...")
        gdf.to_file('cidades_brasil_exemplo.geojson', driver='GeoJSON')
        print("✅ Dados salvos em 'cidades_brasil_exemplo.geojson'")
        
        print(f"\n🎉 Exemplo executado com sucesso!")
        print(f"🚀 Agora você pode explorar o tutorial completo em 'geopandas_tutorial.py'")
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        print("💡 Execute 'python setup.py' para instalar as dependências")
        
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        print("💡 Verifique se todas as dependências estão instaladas")

if __name__ == "__main__":
    exemplo_rapido()

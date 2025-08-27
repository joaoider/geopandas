# 📊 Tutorial Profissional de GeoPandas

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-0.13+-green.svg)](https://geopandas.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Este projeto apresenta um **tutorial completo e profissional** sobre o **GeoPandas**, uma biblioteca Python poderosa para análise de dados geoespaciais.

## 🎯 Sobre o Projeto

O GeoPandas é uma extensão do Pandas que adiciona suporte para dados geoespaciais, permitindo trabalhar com informações geográficas de forma intuitiva e eficiente. Este tutorial foi desenvolvido para demonstrar as melhores práticas e funcionalidades avançadas da biblioteca.

## ✨ Características

- 🚀 **Código Profissional**: Estrutura organizada e bem documentada
- 📚 **Tutorial Completo**: Do básico ao avançado
- 🗺️ **Visualizações Profissionais**: Mapas e gráficos de alta qualidade
- 🔍 **Operações Espaciais**: Demonstrações práticas de funcionalidades
- 💾 **Múltiplos Formatos**: Exportação em diversos formatos de arquivo
- 🔧 **Boas Práticas**: Dicas para uso profissional

## 📋 Pré-requisitos

- **Python 3.7+**
- **Conhecimento básico de Pandas**
- **Familiaridade com conceitos de GIS**
- **Bibliotecas Python** (instaladas automaticamente)

## 🚀 Instalação e Uso

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/geopandas.git
cd geopandas
```

### 2. Execute o Tutorial

```bash
python geopandas_tutorial.py
```

### 3. Ou Execute no Jupyter

```bash
jupyter notebook geopandas_tutorial.py
```

## 📁 Estrutura do Projeto

```
geopandas/
├── geopandas_tutorial.py    # Tutorial principal em Python
├── README.md               # Este arquivo
├── .gitignore             # Arquivos ignorados pelo Git
└── minicurso-geopandas/   # Diretório adicional (se existir)
```

## 🎓 O que Você Aprenderá

### 📊 **Fundamentos**
- Instalação e configuração do GeoPandas
- Estrutura de dados geoespaciais
- Sistemas de coordenadas (CRS)

### 🗺️ **Visualização**
- Criação de mapas profissionais
- Personalização de gráficos
- Múltiplas visualizações em um layout

### 🔍 **Operações Espaciais**
- Filtragem espacial
- Cálculo de distâncias
- Criação de buffers e áreas de influência
- Estatísticas geoespaciais

### 💾 **Exportação de Dados**
- GeoJSON (web-friendly)
- Shapefile (padrão GIS)
- CSV com coordenadas
- Parquet (eficiente)

### 🔧 **Boas Práticas**
- Validação de dados
- Tratamento de erros
- Otimização de performance
- Documentação de código

## 📚 Exemplos de Código

### Criação de GeoDataFrame

```python
import geopandas as gpd
from shapely.geometry import Point

# Coordenadas das cidades
coordenadas = [(-74.006, 40.7128), (-87.6298, 41.8781)]
geometrias = [Point(lon, lat) for lon, lat in coordenadas]

# Dados das cidades
dados = {
    'cidade': ['Nova York', 'Chicago'],
    'populacao': [8336817, 2693976]
}

# Criando GeoDataFrame
gdf = gpd.GeoDataFrame(dados, geometry=geometrias, crs='EPSG:4326')
```

### Visualização Profissional

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(14, 10))

gdf.plot(
    column='populacao',
    ax=ax,
    cmap='viridis',
    legend=True,
    markersize=100,
    edgecolor='black'
)

ax.set_title('Cidades dos Estados Unidos', fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.grid(True, alpha=0.3)

plt.show()
```

## 🛠️ Dependências

O tutorial instala automaticamente as seguintes bibliotecas:

- **GeoPandas**: Análise geoespacial
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica
- **Matplotlib**: Visualizações
- **Shapely**: Geometrias espaciais

## 📖 Documentação Adicional

- [Documentação Oficial do GeoPandas](https://geopandas.org/)
- [Exemplos e Tutoriais](https://geopandas.org/examples/)
- [Comunidade no GitHub](https://github.com/geopandas/geopandas)
- [Guia de Início Rápido](https://geopandas.org/getting_started.html)

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Assistente IA** - Desenvolvido com ❤️ para a comunidade Python

## 🙏 Agradecimentos

- Comunidade GeoPandas
- Contribuidores do projeto
- Usuários que testaram e forneceram feedback

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:

- Abra uma [Issue](https://github.com/seu-usuario/geopandas/issues)
- Entre em contato através do email: seu-email@exemplo.com
- Participe da discussão na comunidade

---

⭐ **Se este tutorial foi útil, considere dar uma estrela ao projeto!**

*Última atualização: Dezembro 2024*
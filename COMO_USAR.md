# 🚀 Como Usar - Tutorial Profissional de GeoPandas

## ⚡ Início Rápido

### 1. **Primeira Execução (Recomendado)**
```bash
python setup.py
```
Este comando irá:
- ✅ Verificar a versão do Python
- 📦 Instalar todas as dependências
- 🔍 Testar a instalação
- 🚀 Executar um teste do tutorial

### 2. **Exemplo Rápido (Para ver resultados imediatos)**
```bash
python exemplo_rapido.py
```
Este comando irá:
- 🌍 Criar dados de cidades brasileiras
- 🗺️ Gerar um mapa visual
- 💾 Salvar os dados em GeoJSON
- 📊 Mostrar estatísticas básicas

### 3. **Tutorial Completo**
```bash
python geopandas_tutorial.py
```
Este comando irá:
- 📚 Executar o tutorial completo
- 🎯 Demonstrar todas as funcionalidades
- 🔍 Mostrar operações espaciais avançadas
- 💾 Exportar dados em múltiplos formatos

## 📋 Pré-requisitos

- **Python 3.7+** (verificado automaticamente)
- **Conexão com internet** (para instalação das dependências)
- **Permissões de escrita** (para salvar arquivos de saída)

## 🔧 Instalação Manual (Alternativa)

Se preferir instalar manualmente:

```bash
# 1. Atualizar pip
python -m pip install --upgrade pip

# 2. Instalar GeoPandas e dependências
pip install geopandas pandas numpy matplotlib shapely pyproj fiona

# 3. Verificar instalação
python -c "import geopandas; print('GeoPandas:', geopandas.__version__)"
```

## 📁 Estrutura dos Arquivos

```
geopandas/
├── 📚 geopandas_tutorial.py    # Tutorial completo e profissional
├── 🚀 exemplo_rapido.py        # Exemplo simples para início rápido
├── ⚙️  setup.py                # Script de instalação automática
├── 📦 requirements.txt          # Lista de dependências
├── 📖 README.md                # Documentação completa
├── 🎯 COMO_USAR.md             # Este arquivo
└── 📁 minicurso-geopandas/     # Diretório adicional
```

## 🎯 Casos de Uso

### 🆕 **Primeira vez usando GeoPandas?**
1. Execute `python setup.py`
2. Depois `python exemplo_rapido.py`
3. Finalmente `python geopandas_tutorial.py`

### 🔄 **Já conhece GeoPandas?**
1. Execute `python geopandas_tutorial.py` diretamente
2. Explore as funções específicas que interessam
3. Use como referência para seus projetos

### 🧪 **Quer testar rapidamente?**
1. Execute `python exemplo_rapido.py`
2. Veja resultados em segundos
3. Modifique os dados de exemplo

## 🚨 Solução de Problemas

### ❌ **Erro: "No module named 'geopandas'"**
```bash
python setup.py
```

### ❌ **Erro: "Permission denied"**
- Execute como administrador
- Ou use ambiente virtual: `python -m venv venv`

### ❌ **Erro: "matplotlib backend"**
- Instale: `pip install tkinter` (Linux)
- Ou use: `matplotlib.use('Agg')` no código

### ❌ **Erro: "CRS not found"**
- Instale: `pip install pyproj`
- Ou use CRS simples: `crs='EPSG:4326'`

## 🔍 Verificações

### ✅ **Teste de Importação**
```bash
python -c "import geopandas_tutorial; print('✅ OK')"
```

### ✅ **Teste de Função**
```bash
python -c "import geopandas_tutorial; print(geopandas_tutorial.criar_dados_exemplo())"
```

### ✅ **Teste de Dependências**
```bash
python -c "import geopandas, pandas, numpy, matplotlib; print('✅ Todas OK')"
```

## 📚 Próximos Passos

1. **Explore o código** em `geopandas_tutorial.py`
2. **Modifique os dados** de exemplo
3. **Adicione suas funcionalidades**
4. **Compartilhe** com a comunidade
5. **Contribua** para o projeto

## 🆘 Precisa de Ajuda?

- 📖 Leia o `README.md` completo
- 🔍 Verifique este guia `COMO_USAR.md`
- 🐛 Execute `python setup.py` para diagnóstico
- 💬 Abra uma issue no GitHub

---

**🚀 Agora você está pronto para explorar o mundo do GeoPandas!**

*Última atualização: Dezembro 2024*

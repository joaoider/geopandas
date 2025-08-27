#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Script de Setup para o Tutorial Profissional de GeoPandas
============================================================

Este script automatiza a instalação e configuração do ambiente para o tutorial.
"""

import subprocess
import sys
import os
from pathlib import Path

def verificar_python():
    """Verifica se a versão do Python é compatível."""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ é necessário!")
        print(f"Versão atual: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detectado")
    return True

def instalar_dependencias():
    """Instala as dependências necessárias."""
    print("\n📦 Instalando dependências...")
    
    try:
        # Instalando dependências principais
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # Instalando GeoPandas e dependências
        dependencias = [
            "geopandas>=0.13.0",
            "pandas>=1.3.0",
            "numpy>=1.21.0",
            "matplotlib>=3.5.0",
            "shapely>=1.8.0",
            "pyproj>=3.0.0",
            "fiona>=1.8.0"
        ]
        
        for dep in dependencias:
            print(f"  📥 Instalando {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
        
        print("✅ Todas as dependências foram instaladas com sucesso!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def verificar_instalacao():
    """Verifica se a instalação foi bem-sucedida."""
    print("\n🔍 Verificando instalação...")
    
    try:
        import geopandas as gpd
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        from shapely.geometry import Point
        
        print("✅ GeoPandas:", gpd.__version__)
        print("✅ Pandas:", pd.__version__)
        print("✅ NumPy:", np.__version__)
        print("✅ Matplotlib:", plt.matplotlib.__version__)
        print("✅ Shapely:", Point(0, 0).__class__.__module__)
        
        return True
        
    except ImportError as e:
        print(f"❌ Erro na verificação: {e}")
        return False

def criar_ambiente_virtual():
    """Cria um ambiente virtual para o projeto."""
    print("\n🌍 Criando ambiente virtual...")
    
    try:
        # Verificando se venv está disponível
        subprocess.check_call([sys.executable, "-m", "venv", "--help"], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Criando ambiente virtual
        venv_path = Path("venv")
        if not venv_path.exists():
            subprocess.check_call([sys.executable, "-m", "venv", "venv"])
            print("✅ Ambiente virtual criado em 'venv/'")
        else:
            print("✅ Ambiente virtual já existe em 'venv/'")
        
        return True
        
    except subprocess.CalledProcessError:
        print("⚠️  Não foi possível criar ambiente virtual (venv não disponível)")
        return False

def executar_tutorial():
    """Executa o tutorial para testar a instalação."""
    print("\n🚀 Executando tutorial de teste...")
    
    try:
        # Importando e executando uma função simples
        import geopandas_tutorial
        
        # Testando criação de dados
        dados = geopandas_tutorial.criar_dados_exemplo()
        print(f"✅ Tutorial funcionando! Criados {len(dados)} pontos de dados")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao executar tutorial: {e}")
        return False

def mostrar_instrucoes():
    """Mostra instruções de uso."""
    print("\n" + "="*60)
    print("🎉 SETUP CONCLUÍDO COM SUCESSO!")
    print("="*60)
    
    print("\n📚 Como usar:")
    print("  1. Execute o tutorial: python geopandas_tutorial.py")
    print("  2. Ou use no Jupyter: jupyter notebook")
    print("  3. Ou importe as funções: import geopandas_tutorial")
    
    print("\n🔧 Comandos úteis:")
    print("  • python geopandas_tutorial.py          # Executar tutorial completo")
    print("  • python -c 'import geopandas_tutorial' # Testar importação")
    print("  • pip list | grep geopandas             # Verificar versão instalada")
    
    print("\n📁 Arquivos criados:")
    print("  • geopandas_tutorial.py                 # Tutorial principal")
    print("  • requirements.txt                      # Dependências")
    print("  • README.md                             # Documentação")
    
    print("\n🚀 Próximos passos:")
    print("  1. Explore o código em geopandas_tutorial.py")
    print("  2. Modifique os dados de exemplo")
    print("  3. Adicione suas próprias funcionalidades")
    print("  4. Compartilhe com a comunidade!")
    
    print("\n---")
    print("Desenvolvido com ❤️ para a comunidade Python")
    print("Boa sorte com seus projetos geoespaciais!")

def main():
    """Função principal do setup."""
    print("🚀 SETUP DO TUTORIAL PROFISSIONAL DE GEOPANDAS")
    print("=" * 60)
    
    # Verificações iniciais
    if not verificar_python():
        sys.exit(1)
    
    # Criação do ambiente virtual (opcional)
    criar_ambiente_virtual()
    
    # Instalação das dependências
    if not instalar_dependencias():
        print("❌ Falha na instalação das dependências")
        sys.exit(1)
    
    # Verificação da instalação
    if not verificar_instalacao():
        print("❌ Falha na verificação da instalação")
        sys.exit(1)
    
    # Teste do tutorial
    if not executar_tutorial():
        print("❌ Falha na execução do tutorial")
        sys.exit(1)
    
    # Instruções finais
    mostrar_instrucoes()

if __name__ == "__main__":
    main()

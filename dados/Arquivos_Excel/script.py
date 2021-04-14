# Combinar múltiplas planilahs de excel, com múltiplas abas em um único data frame pandas

# Impota as bibliotecas

import pandas as pd
import os

# Caminho do diretório que contém os arquivos
diretorio = 'C:/Users/user/Desktop/wetransfer-eacf1d (1)/Dados brutos COPEL'
arquivos = os.listdir(diretorio) 

# Cria um arquivo vazio para armazenar os dados
df_combinado = pd.DataFrame()

# Loop para abrir cada arquivo excel
for arquivo in arquivos:                         
    
    # Cria o caminho para cada arquivo
    nome_arquivo = [diretorio + "\\" + arquivo][0]
    
    # Testa se os arquivos terminam com .xlsx
    if nome_arquivo.endswith('.xlsx'):
        
        # Abrea o arquivo e cria uma lista com o nome das abas
        arquivo_exel = pd.ExcelFile(nome_arquivo)
        abas = arquivo_exel.sheet_names
        
        # Loop para abrir cada aba
        for aba in abas:
          
            # Armazena cada planilha de cada aba em 'df' e adiciona ao 'df_combinado'
            df = arquivo_exel.parse(sheet_name = aba)
            df_combinado = df_combinado.append(df)

# Visualiza o arquivo combinado            
df_combinado


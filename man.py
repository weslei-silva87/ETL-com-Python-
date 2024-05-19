import pandas as pd
import os
import glob

# Caminho para ler os arquivos
folder_path = 'src\\data\\raw'

# Lista todos os arquivos de Excel
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print('Nenhum arquivo compatível encontrado')
else:
    # Criação de um dataframe
    dfs = []

    for excel_file in excel_files:
        try:
            # Ler o aquivo em excel 
            df_temp = pd.read_excel(excel_file)
            dfs.append(df_temp)  # Adiciona o DataFrame temporário à lista

            # Pegar o nome do arquivo
            File_nome = os.path.basename(excel_file)

    #criar mais uma coluna com nome do arquivo
            df_temp['filenome'] = File_nome

    # Criamos uma nova coluna LOCATION
            if 'brasil' in File_nome.lower():
                df_temp['location'] = 'br'
            if 'france' in File_nome.lower():
                df_temp['location'] = 'fr'
            if 'italian' in File_nome.lower():
                df_temp['location'] = 'it'

            # Criamos uma nova coluna chamada CAMPAIGN
            df_temp['campaign'] = df_temp ['utm_link'].str.extract(r'utm_campaign=(.*)')

    # Salvando os valores no tadaframe oficial
            dfs.append(df_temp)
          
        except Exception as e:
            print(f'Erro ao ler o arquivo {excel_file}: {e}')


# iNCLUINDO OS RESULTADOS EM UA TABELA UNICA
if dfs:
    result = pd.concat(dfs, ignore_index=True)

    #CAMINHO DE SAIDA   
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    # CONFIGURAR O MOOTR DE ESCRITA
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

# LEVA OS DADOS DE RESULTADO A SEREM ESCRITOS EM EXCEL
    result.to_excel(writer, index=False)

# SALVA O ARQUIVO EM EXCEL
    writer._save()

else:
    print('nehum dado para ser salvo')
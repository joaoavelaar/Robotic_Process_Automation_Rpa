from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pandas as pd

navegador = opcoesSelenium.Chrome()

#Abrindo o site do rpachallengeocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

dataFrameLista = []

linha = 1
#for = para
for linhaAtual in linhas:

    print(linhaAtual.text)
    dataFrameLista.append(linhaAtual.text)

    linha = linha + 1

arquivoExcel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')
arquivoExcel.save()

dataFrame = pd.DataFrame(dataFrameLista, columns=['Nome_Coluna_Dados'])

#Prepara o arquivo do Excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Sheet1', index=False)

#Salva as informações no arquivo de Excel
arquivoExcel.save()

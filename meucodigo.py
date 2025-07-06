from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

empresas = ('PETR3.SA','MGLU3.SA','VIVT3.SA')
valores = list()
data_hora = list()



for empresas in empresas:
  input_busca = driver.find_element(By.ID, 'filled-normal')
  input_busca.send_keys(empresas)
  sleep(2)

  input_busca.send_keys(Keys.ENTER)
  sleep(1)

  span_val = driver.find_element (By.XPATH, '//SPAN[@class="chart-info-val ng-binding"]')
  cotacao_valor = span_val.text

  valores.append(cotacao_valor)
  data_hora.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))


print(empresas)
print(valores)
print(data_hora)

dados = {
      'empresas': empresas,
      'valor': valores,
      'data_hora': data_hora,

}

print(dados)

df_empresas = pd.DataFrame(dados)
df_empresas.to_excel('./empresas.xlsx')








input('')





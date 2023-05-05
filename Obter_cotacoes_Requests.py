#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests

# Define a URL da API do Banco Central do Brasil para obter as cotações
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json"
# Define a URL da API do Banco Central do Brasil para obter as cotações do Euro
url_euro = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados/ultimos/1?formato=json"
# Define a URL da API do Banco Central do Brasil para obter as cotações da Libra
url_libra = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados/ultimos/1?formato=json"

# Faz a requisição para obter a cotação do Dólar
response = requests.get(url)
cotacao_dolar = response.json()[0]["valor"]

# Faz a requisição para obter a cotação do Euro
response_euro = requests.get(url_euro)
cotacao_euro = response_euro.json()[0]["valor"]

# Faz a requisição para obter a cotação da Libra
response_libra = requests.get(url_libra)
cotacao_libra = response_libra.json()[0]["valor"]

# Imprime as cotações obtidas
print("Cotação do Dólar:", cotacao_dolar)
print("Cotação do Euro:", cotacao_euro)
print("Cotação da Libra:", cotacao_libra)


# In[ ]:





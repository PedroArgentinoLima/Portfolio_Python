#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import random
from faker import Faker
import datetime

# Configuração de data

hoje = datetime.date.today() # obtém a data de hoje
primeiro_dia_mes_passado = datetime.date(hoje.year, hoje.month-1, 1) # obtém a data do dia 1 do mês passado
ontem = hoje - datetime.timedelta(days=1)

# Criação das colunas com valores aleatórios
faker = Faker('pt_BR')

pagadores = [faker.name() for i in range(10000)]
cnpjs = [faker.random_number(digits=14) for i in range(10000)]
ufs = [faker.state_abbr() for i in range(10000)]
ctes = [faker.random_number(digits=2) for i in range(10000)]
valores_fretes = [round(random.uniform(1000, 2000), 2) for i in range(10000)]
volumes = [random.randint(1, 10) for i in range(10000)]
pesos = [round(random.uniform(1, 100), 2) for i in range(10000)]
valores_mercadorias = [round(random.uniform(1000, 10000), 2) for i in range(10000)]

empresas = ["TransBrasil Cargas", "NovaLog Transportes", "Sudeste Expresso", "Norte Cargo Brasil", "Via Sul Transportadora"]
modais = ["Rodoviário", "Expresso", "Logística"]
produtos = ["B2B", "B2C", "SFX"]

def get_produto(modal, produtos):
    if modal == "Logística":
        produto = "Logística"
    else:
        produto = random.sample(produtos, 2)
    return produto

# Criação do dataframe
df = pd.DataFrame({
    'Emissao': pd.date_range(start=primeiro_dia_mes_passado, end=ontem, periods=10000),
    'Pagador': pagadores,
    'CNPJ': cnpjs,
    'UF Origem': ufs,
    'Empresa': [random.choice(empresas) for i in range(10000)],
    'Modal': [random.choice(modais) for i in range(10000)],
    'Ctes': ctes,
    'Valor frete': valores_fretes,
    'Volumes': volumes,
    'Peso calculado': pesos,
    'Valor Mercadoria': valores_mercadorias
})

df['Produto'] = df.apply(lambda x: get_produto(x['Modal'], produtos) if not isinstance(x['Modal'], float) else np.nan, axis=1)
df = df.explode('Produto')

# Criação do arquivo .xlsx
df.to_excel('DB_Jornal.xlsx', index=False)


# In[ ]:





# Enviar um SMS indicando se houve alguma pessoa que bateu a meta de vendas
# Se houver, esta pessoa ganhará uma viagem com tudo pago

import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC4db9e61151f65d8d69813f9477f94635"
# Your Auth Token from twilio.com/console
auth_token = "355afccc08c2380c7fd6804ee3801a25"

client = Client(account_sid, auth_token)

# Passo a passo da solução
# Abrir os arquivos em excel
# Para cada arquivo:
# Verificar se algum valor na coluna VEndas daquele arquivo é maior que 55.000
# Se for maior que 55.000 -> envia um SMS com o nome, o mês e as vendas do vendedor

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():  # any() verifica se algum valor da coluna é maior que 55000
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        # loc localiza a linha e a coluna da planilha
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} O Vendedor {vendedor}, bateu as metas de vendas, vendendo um total de R$ {vendas}')
        message = client.messages.create(
            to="+5511972911397",
            from_="+18647270836",
            body=f'No mês de {mes}, O Vendedor {vendedor} bateu as metas de vendas, vendendo um total de R$ {vendas}.'
                 f' Sendo assim, o Sr(a) {vendedor} irá ganhar uma viagem com tudo pago para as Maldivias!')

        print(message.sid)




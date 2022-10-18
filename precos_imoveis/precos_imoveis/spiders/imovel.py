import scrapy
import pandas as pd
from precos_imoveis.items import PrecosImoveisItem
from unidecode import unidecode
import precos_imoveis.spiders.config as banco
import pymysql
from urllib.parse import quote
import mysql.connector
from sqlalchemy import create_engine




class ImovelSpider(scrapy.Spider):
    name = 'imovel'

    start_urls = ['https://www.vivareal.com.br/venda']

    def parse(self, response):
        items = PrecosImoveisItem()
        items['endereco'] = response.css('.property-card__address::text').getall()


        lista_cidades = []
        lista_estados = []
        
        for k in range(len(items['endereco'])):
            
            estado = items['endereco'][k].split('-')[-1].strip()
            lista_estados.append(estado)

            endereco_sem_estado = items['endereco'][k][:-5]
            dados_endereco = endereco_sem_estado.split(',')
            cidade = dados_endereco[len(dados_endereco)-1]
            cidade = unidecode(cidade).upper().strip()
            print(cidade)
            lista_cidades.append(cidade)

        items['metros_quadrados'] = response.css('.js-property-card-detail-area::text').getall()
        items['quarto'] = response.css('.js-property-detail-rooms .js-property-card-value::text').getall()
        items['banheiro'] = response.css('.js-property-detail-bathroom .js-property-card-value::text').getall()
        items['vaga'] = response.css('.js-property-detail-garages .js-property-card-value::text').getall()
        items['preco'] = response.css('#js-site-main p::text').getall()

        lista_preco = [line.strip() for line in  items['preco'] if line.strip() != ""]

        print(items['preco'])
        print(lista_preco)

        # if len(items['preco']) > len(items['quarto']):
        #     lista_precos = items['preco'][0:36]
        # else:
        #     lista_precos = items['preco']

        


        df = pd.DataFrame(columns=['metros_quadrados','quartos','banheiros','vagas','cidade','estado','preco'])
        df['metros_quadrados'] =  items['metros_quadrados']
        df['quartos'] =  items['quarto']
        df['banheiros'] =  items['banheiro']
        df['vagas'] =  items['vaga']
        df['cidade'] =  lista_cidades
        df['estado'] =  lista_estados
        # df['preco'] =  items['preco']
        print(len(items['banheiro']))
        print(len(df['cidade']))
        print(len(lista_preco))
        df['preco'] =  lista_preco[:36]

        df['preco'] = df['preco'].apply(lambda x: int(x.replace('R$','').replace('.','').strip()) if 'R$' in x else 0.0)
        df = df[df['preco'] != 0.0]

        print(df)
        print(banco.USER)
        engine = create_engine("mysql+pymysql://" +banco.USER+ ":%s" % quote(banco.SENHA) +"@"+banco.HOST+":"+banco.PORT+"/"+banco.SCHEMA)
        
        df.to_sql(banco.TABELA, con = engine, if_exists='replace', index = False)


        pass

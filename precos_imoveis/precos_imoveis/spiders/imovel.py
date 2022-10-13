import scrapy
import pandas as pd
from precos_imoveis.items import PrecosImoveisItem
from unidecode import unidecode

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
            lista_cidades.append(cidade)

        items['metros_quadrados'] = response.css('.js-property-card-detail-area::text').getall()
        items['banheiro'] = response.css('::text').getall()
        items['vaga'] = response.css('::text').getall()
        items['preco'] = response.css('::text').getall()
        items['condominio'] = response.css('::text').getall()


        pass

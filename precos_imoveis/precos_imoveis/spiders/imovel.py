import scrapy


class ImovelSpider(scrapy.Spider):
    name = 'imovel'

    start_urls = ['https://www.vivareal.com.br/venda']

    def parse(self, response):
        pass

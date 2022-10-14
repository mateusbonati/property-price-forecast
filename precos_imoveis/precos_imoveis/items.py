# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PrecosImoveisItem(scrapy.Item):
    endereco = scrapy.Field()
    quarto = scrapy.Field()
    metros_quadrados = scrapy.Field()
    banheiro = scrapy.Field()
    vaga = scrapy.Field()
    preco = scrapy.Field()


    pass

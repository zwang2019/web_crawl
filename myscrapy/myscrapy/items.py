# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from pyasn1.type.univ import Null


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:

    title_cn = scrapy.Field()
    title_foreign = scrapy.Field()
    title_other = scrapy.Field()

    director = scrapy.Field()
    cast = scrapy.Field()

    year = scrapy.Field()
    country = scrapy.Field()
    genre = scrapy.Field()

    rating = scrapy.Field()
    reviews = scrapy.Field()

    quotation = scrapy.Field()
    link_url = scrapy.Field()
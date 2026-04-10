from typing import AsyncIterator, Any

import scrapy
from ..items import MyscrapyItem

import re


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    # async def start(self) -> AsyncIterator[Any]:
    #     for i in range(10):
    #         page_code = i * 25
    #         url = f'https://movie.douban.com/top250?start={page_code}&filter='
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # response xpath
        li = response.xpath('//ol[@class="grid_view"]/li')
        for li in li:
            item = MyscrapyItem()
            # title
            item['title_cn'] = li.xpath('.//div[@class="hd"]/a/span[@class="title"][1]/text()').extract_first()
            title_foreign = li.xpath('.//div[@class="hd"]/a/span[@class="title"][2]/text()').extract_first()
            title_other = li.xpath('.//div[@class="hd"]/a/span[@class="other"]/text()').extract_first()
            item['title_foreign'] = text = re.sub(r'^\s*/?\s*', '', title_foreign) if title_foreign is not None else None
            item['title_other'] = text = re.sub(r'^\s*/?\s*', '', title_other) if title_other is not None else None
            # director & cast
            description = li.xpath('.//div[@class="bd"]/p[1]/text()')[0].extract()
            match = re.search(r'导演:\s*(.*?)(?=\s*主演:|\s*主演\.\.\.|\s*主\.\.\.|$)', description, re.S)
            item['director'] = match.group(1).strip() if match else '...'
            match = re.search(r'主演:\s*(.*)', description, re.S)
            item['cast'] =match.group(1).strip() if match else '...'
            # year & country & genre
            description_2 = li.xpath('.//div[@class="bd"]/p[1]/text()')[1].extract()
            match = re.search(r'^\s*(\d{4})(?=\s*/)', description_2)
            item['year'] = match.group(1) if match else None
            match = re.search(r'^\s*\d{4}\s*/\s*(.*?)\s*(?=/)', description_2)
            item['country'] = match.group(1).strip() if match else None
            match = re.search(r'/\s*([^/]+?)\s*$', description_2)
            item['genre'] = match.group(1).strip() if match else None
            # rating & reviews
            item['rating'] = li.xpath('.//div[@class="bd"]/div/span[@class="rating_num"]/text()').extract_first()
            match = re.search(r'^(\d+)人评价$', li.xpath('.//div[@class="bd"]/div/span[4]/text()').extract_first().strip())
            item['reviews'] = int(match.group(1)) if match else None
            # quotation
            item['quotation'] = li.xpath('.//div[@class="bd"]/p[2]/span/text()').extract_first()
            # url
            item['link_url'] = li.xpath('.//div[@class="pic"]/a/@href').extract_first()

            yield item
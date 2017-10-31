import scrapy

class DmozItem(scrapy.Item):
    title =scrapy.Field()
    link=scrapy.Field()
    desc=scrapy.Field()


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains=["dmoz.org"]
    start_urls=[
        "http://blog.csdn.net/duruiqi_fx",
        "http://blog.csdn.net/duruiqi_fx/article/details/72927777"
    ]

    def parse(self, response):
        for sel  in response.xpath('//ul/li'):
            item =DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield  item

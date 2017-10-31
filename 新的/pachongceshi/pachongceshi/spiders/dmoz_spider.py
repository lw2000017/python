from scrapy.spider import Spider



class DmmozSpider(Spider):
    name = 'dmoz'
    allowed_domains=['dmoz.org']
    start_urls=[
        "http://blog.csdn.net/duruiqi_fx",
        "http://blog.csdn.net/duruiqi_fx/article/details/72927777"
    ]

    def parse(self, response):
        filename=response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)




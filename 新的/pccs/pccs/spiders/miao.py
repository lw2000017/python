import scrapy
from scrapy import Selector

class NgaSpider(scrapy.Spider):
    name = "NgaSpider"
    host = "http://bbs.ngacn.cc/"
    start_urls = [
        "http://ngacn.cc/thread.php?fid=406",
    ]

    def parse(self, response):
        selector = Selector(response)
        content_list = selector.xpath("//*[@class='topic']")
        for content in content_list:
            topic = content.xpath('string(.)').extract_first()
            print topic
            url = self.host + content.xpath('@href').extract_first()
            print url
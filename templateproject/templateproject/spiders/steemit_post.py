# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy_splash import SplashRequest

class SteemitPostSpider(scrapy.Spider):
    name = 'steemit_post'
    allowed_domains = ['steemit.com']
    start_urls = ['https://steemit.com/@ertinfagor/blog']
    # http_user = 'splash-user'
    # http_pass = 'splash-password'

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            yield SplashRequest(
                link.url,
                self.parse_link,
                endpoint='render.json',
                args={
                    'wait': 0.5,
                    'html': 1,
                }
            )

    def parse_link(self, response):
        print("PARSED", response.real_url, response.url)
        print (response.xpath(".//*[@id='posts_list']/ul/li/article/div[@class='PostSummary__content']/div[1]/h3/a/text()").extract())
#        print(response.css("title").extract())
#        print(response.data["har"]["log"]["pages"])
#        print(response.headers.get('Content-Type'))

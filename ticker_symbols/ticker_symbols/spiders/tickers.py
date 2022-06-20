import scrapy


class TickersSpider(scrapy.Spider):
    name = 'tickers'
    allowed_domains = ['ng.investing.com']
    start_urls = ['http://ng.investing.com/']

    def parse(self, response):
        pass

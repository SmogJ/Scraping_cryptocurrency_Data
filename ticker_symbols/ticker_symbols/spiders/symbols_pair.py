import scrapy


class SymbolsPairSpider(scrapy.Spider):
    name = 'symbols_pair'
    allowed_domains = ['ng.investing.com']
    start_urls = ['http://ng.investing.com/']

    def parse(self, response):
        pass

        Time = response.css('td[class$="-time"]::text').get()

        Vol = response.css('td[class$="pcp"] + td::text').get()

        Chg = response.css('td[class$="pcp"]::text').get() 

        Low = response.css('td[class$="low"]::text').get()

        High = response.css('td[class$="high"]::text').get()

        Open = response.css('td:nth-child(5)::text').get()

        Last = response.css('td[class$="last"]::text').get()

        Exchange = response.css('td:nth-child(3).left::text').get()

        Name = response.css('td.left.bold.elp>a::text').get()

        crypto_table= response.css('table[id^="crypto_currencies_"]').get()
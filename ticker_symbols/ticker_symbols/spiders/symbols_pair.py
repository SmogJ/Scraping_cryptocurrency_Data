import scrapy


class SymbolsPairSpider(scrapy.Spider):
    name = 'symbols_pair'
    allowed_domains = ['ng.investing.com/crypto/currency-pairs']
    start_urls = ['https://ng.investing.com/crypto/currency-pairs/']

    def parse(self, response):
        crypto_table= response.css('table[id^="crypto_currencies_"]').get()

        for i in crypto_table:
            showmore= response.css('span.arial_12.showArrowafter').get()

            items= {
            'Name':response.css('td.left.bold.elp>a::text').get(),

            'Exchange': response.css('td:nth-child(3).left::text').get(),
            
            'Last': response.css('td[class$="last"]::text').get(),

            'Open': response.css('td:nth-child(5)::text').get(),

            'High': response.css('td[class$="high"]::text').get(),

            'Low': response.css('td[class$="low"]::text').get(),

            'Chg': response.css('td[class$="pcp"]::text').get(),

            'Vol': response.css('td[class$="pcp"] + td::text').get(),

            'Time': response.css('td[class$="-time"]::text').get()
            }

            yield items

        pass

import scrapy

# import gspread
# gc = gspread.service_account(file="symbolstickers.json")
# sh = gc.open("symbols_tickers").ticker

class SymbolsPairSpider(scrapy.Spider):
    name = 'symbols_pair'
    allowed_domains = ['ng.investing.com/crypto/currency-pairs']
    start_urls = ['https://ng.investing.com/crypto/currency-pairs/']


    def parse(self, response):

        # showmore = response.css(' span.arial_12.showArrowafter')
        # for s in showmore:
        #     yield s.css('span.arial_12.showArrowafter').

        crypto_table = response.css('table[id^="crypto_currencies_"] > tbody > tr')

        for i in crypto_table:
            tickers= {
            'showmore':i.css('span.arial_12.showArrowafter').extract(),    
            'Name': i.css('td.left.bold.elp>a::text').extract(),
            'Exchange': i.css('td:nth-child(3).left::text').extract(),
            'Last': i.css('td[class$="last"]::text').extract(),
            'Open': i.css('td:nth-child(5)::text').extract(),
            'High': i.css('td[class$="high"]::text').extract(),
            'Low': i.css('td[class$="low"]::text').extract(),
            'Chg': i.css('td[class$="pcp"]::text').extract(),
            'Vol': i.css('td[class$="pcp"] + td::text').extract(),
            'Time': i.css('td[class$="-time"]::text').extract()
            }
            yield tickers
            # sh.append(tickers)
        pass

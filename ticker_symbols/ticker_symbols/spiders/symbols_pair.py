# from fileinput import filename
# from time import time
import scrapy

import pandas as pd 

import datetime

import gspread

gc = gspread.service_account(filename='symbolstickers.json') # connecting the bot to the gspread worksheet
sh = gc.open("symbols_tickers") # opening workbook
wksheet= sh.worksheet("symbols") # pointing at the actual sheet on the workbook
wksheet.clear() # clears the sheet of any data
wksheet.format('A1:J1', {'textFormat': {'bold': True}}) # formatting the sheet header
wksheet.append_row(['Name', 'Exchange', 'Last', 'Open', 'High', 'Low', 'Chg', 'Vol', 'Time', 'Cur_Time']) # Naming the data columns

class SymbolsPairSpider(scrapy.Spider):
    name = 'symbols_pair'
    allowed_domains = ['ng.investing.com/crypto/currency-pairs']
    start_urls = ['https://ng.investing.com/crypto/currency-pairs/']

    def parse(self, response):
        crypto_table= response.css('table[id^="crypto_currencies_"] > tbody > tr')

        for i in crypto_table:
            # showmore= i.css('span.arial_12.showArrowafter').get()

            item= [{
            'Name':i.css('td.left.bold.elp>a::text').get(),
            'Exchange': i.css('td:nth-child(3).left::text').get(),
            'Last': i.css('td[class$="last"]::text').get(),
            'Open': i.css('td:nth-child(5)::text').get(),
            'High': i.css('td[class$="high"]::text').get(),
            'Low': i.css('td[class$="low"]::text').get(),
            'Chg': i.css('td[class$="pcp"]::text').get(),
            'Vol': i.css('td[class$="pcp"] + td::text').get(),
            'Time': i.css('td[class$="-time"]::text').get(),
            'Cur_Time': datetime.datetime.now()
            }]
            yield item
            
            # appends the data to the worksheet
            wksheet.append_row([              
                str(item['Name']),
                str(item['Exchange']),
                str(item['Last']),
                str(item['Open']),
                str(item['High']),
                str(item['Low']),
                str(item['Chg']),
                str(item['Vol']),
                str(item['Time']),
                str(item['Cur_Time'])
            ])

            # convert data to excel
            sheet = pd.DataFrame(item) # converts dictionary to pandas dataframe
            sheet.to_excel('tickers.xlsx')  # save the data ad excel

            # wksheet.update([sheet.columns.values.tolist()] + sheet.values.tolist()) # updates sheet with data from dataframe
            # print(sheet)

        pass



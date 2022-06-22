# Scraping Ticker Smybols from CoinMarketCap
This Bot will be used to scrape ticker symbols for cryptocurrecy pairing on the https://ng.investing.com/crypto/currency-pairs,
the ticker symbols is inteded to develop a personal cryptocurrency trading journal using Microsoft Excel.

~ The cryptocurrency tickers will be store using a google sheet 

~ Hopefully this will also be used for more trading bot development.

# I will be using the Scrapy for this project
- create project folder amd venv 
- initialize folder        
- pip install scrapy 
- create file: scrapy genspider <script.py> <url>        

Time=response.css('td[class$="-time"]::text').get()

Vol=response.css('td[class$="pcp"] + td::text').get()

Chg=response.css('td[class$="pcp"]::text').get() 

Low=response.css('td[class$="low"]::text').get()

High=response.css('td[class$="high"]::text').get()

Open=response.css('td:nth-child(5)::text').get()

Last=response.css('td[class$="last"]::text').get()

Exchange=response.css('td:nth-child(3).left::text').get()

Name=response.css('td.left.bold.elp>a::text').get()
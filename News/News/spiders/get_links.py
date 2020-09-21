import scrapy
import selenium
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

class TweetSpider3(scrapy.Spider):
    name = 'get_links'

    def start_requests(self):
        yield SeleniumRequest(url="https://www.rbc.ru/tags/?tag=Украина", callback=self.parse, wait_time=1)


    def parse(self, response):

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(chrome_options=options, executable_path = "./chromedriver.exe")

        driver.get("https://www.rbc.ru/tags/?tag=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0")

        y = 2020
        while y>2006:
            if y == 2020:
                m = 7
            else:
                m = 12

            while m>0:
                d = 31 #adjusting to number of days each month is unnecessary with this site
                while d>0:
                    driver.get("https://www.rbc.ru/tags/?tag=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0&dateFrom="+str(d)+"."+str(m)+"."+str(y)+"&dateTo="+str(d)+"."+str(m)+"."+str(y))
                    response2 = Selector(text=driver.page_source)
                    adreses = response2.xpath("//a[@class='search-item__link']/@href").extract()
                    if len(adreses)!=0:
                        for adres in adreses:
                            yield {"link": adres, "date": str(d)+"."+str(m)+"."+str(y)}



                    d -=1
                m -=1
            y -=1



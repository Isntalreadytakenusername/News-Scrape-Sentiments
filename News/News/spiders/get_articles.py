import scrapy
import pandas as pd
import numpy as np

class TesttSpider(scrapy.Spider):
    links = pd.read_csv("from2007Links.csv")
    links = links["link"].dropna()
    links.drop_duplicates(inplace = True)
    links = links.tolist()
    name = 'get_articles'
    allowed_domains = ['https://www.rbc.ru/tags/?tag=%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0']
    start_urls = links

    def parse(self, response):
        text = response.xpath("//div[contains(@class, 'article__text article__text_free')]/p/descendant-or-self::*/text()").extract()
        date = response.xpath("/html/body/div[8]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[1]/div[1]/span[2]/@content").extract()
        yield {"text": text, "date": date[:9]}

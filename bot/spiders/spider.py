import scrapy
import datetime
from bot.items import test_item
from env import env


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        f'https://www.statistischebibliothek.de/mir/servlets/solr/select?q=mods.genre:journal%20AND%20state:published&sort=modified%20desc&start=0&rows={env("ROWS_TO_SCRAPE")}', #7278',
    ]

    def parse(self, response):

        for quote in response.css('div.hit_item'):
            item = test_item()
            item['id'] = quote.css('.hit_counter::text').get()
            item['title']= quote.css('.hit_title>a::attr("title")').get()
            next_page = quote.css('.hit_title>a::attr("href")').get()
            yield scrapy.Request(next_page, self.parseFirst, meta={'item': item})


    def parseFirst(self, response):
        response.meta['item']['subtitle'] = response.css('dt:contains("Sachtitel")+dd::text').get()
        response.meta['item']['amt'] = response.css('dt:contains("Statistisches Amt")+dd::text').get()
        response.meta['item']['region'] = response.css('dt:contains("Region")+dd::text').get()
        response.meta['item']['min_level'] = response.css('dt:contains("kleinste räumliche Ebene")+dd::text').get()
        next_page = response.css('div:nth-child(2) > ul > li:nth-child(1) > a::attr("href")').get()
        yield scrapy.Request(next_page, self.parseSecond, meta={'item': response.meta['item']})

    def parseSecond(self, response):
        response.meta['item']['betreffsjahr'] = response.css('#headline>h1::text').get()
        response.meta['item']['erscheinungsdatum'] = response.css('dt:contains("Erscheinungsdatum")+dd>meta::attr("content")').get()
        response.meta['item']['eintragungsdatum'] = datetime.date.today().isoformat()
        response.meta['item']['url'] = response.request.url
        yield response.meta['item']
        # next_page = response.css('li.next a::attr("href")').get()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)
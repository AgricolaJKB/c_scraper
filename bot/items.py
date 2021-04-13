# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class test_item(scrapy.Item):
   id = scrapy.Field()
   title = scrapy.Field()
   subtitle = scrapy.Field()
   amt = scrapy.Field()
   region = scrapy.Field()
   min_level = scrapy.Field()
   betreffsjahr = scrapy.Field()
   erscheinungsdatum = scrapy.Field()
   eintragungsdatum = scrapy.Field()
   url = scrapy.Field()

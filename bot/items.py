import scrapy

class test_item(scrapy.Item):
   title = scrapy.Field()
   subtitle = scrapy.Field()
   amt = scrapy.Field()
   region = scrapy.Field()
   min_level = scrapy.Field()
   betreffsjahr = scrapy.Field()
   erscheinungsdatum = scrapy.Field()
   eintragungsdatum = scrapy.Field()
   url = scrapy.Field()

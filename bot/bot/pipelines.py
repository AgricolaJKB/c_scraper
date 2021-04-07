# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mariadb
import sys
from env import env

class TutorialPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = env('DB_USERNAME')
        password = env('DB_PASSWORD')  # your password
        database = env('DB_DATABASE')
        port = 3306
        try:
            self.connection = mariadb.connect(host=hostname, user=username, password=password, database=database, port=port)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute(
            f"insert into {env('DB_TABLE')}(orig_id, title, subtitle, amt, region, min_level, betreffsjahr, erscheinungsdatum, eintragungsdatum) values(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (item['id'], item['title'], item['subtitle'], item['amt'], item['region'], item['min_level'], item['betreffsjahr'],
             item['erscheinungsdatum'], item['eintragungsdatum']))
        except mariadb.Error as e:
            print(f"Error: {e}")
        self.connection.commit()
        return item
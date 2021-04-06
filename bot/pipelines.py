import psycopg2


class TutorialPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = 'password' # your password
        database = 'postgres'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        print('yay')
        self.cur.execute("insert into main(title, subtitle, amt, region, min_level, betreffsjahr, erscheinungsdatum, eintragungsdatum) values(%s,%s, %s,%s, %s,%s, %s,%s)",(item['title'],item['subtitle'], item['amt'],item['region'], item['min_level'],item['betreffsjahr'], item['erscheinungsdatum'],item['eintragungsdatum']))
        self.connection.commit()
        return item
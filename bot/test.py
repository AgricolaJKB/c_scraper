import psycopg2



hostname = 'localhost'
username = 'postgres'
password = 'password'  # your password
database = 'postgres'
connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
cur = connection.cursor()





def process_item(item, cur, connection):
    cur.execute(
        "insert into main(title, subtitle, amt, region, min_level, betreffsjahr, erscheinungsdatum, eintragungsdatum) values(%s,%s, %s,%s, %s,%s, %s,%s)",
        (item['title'], item['subtitle'], item['amt'], item['region'], item['min_level'], item['betreffsjahr'],
         item['erscheinungsdatum'], item['eintragungsdatum']))
    connection.commit()
    return item


process_item({'title': 'sdfshdk', 'subtitle': 'sdfsdflks', 'amt': 'sdf', 'region': 'DFKLKJ', 'min_level': 'DJFKDJ', 'betreffsjahr': 'kdjfkskldlj', 'erscheinungsdatum': 'sdfksjd', 'eintragungsdatum': '04-03-2020'}, cur, connection)
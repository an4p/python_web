import psycopg2

con = psycopg2.connect(host="127.0.0.1", database="mypythontestdb",
                       user="postgres",password="Univer123",port=5433)

cur = con.cursor()
sql="insert into clients(name, last_name) values('aaa','bbb')"
cur.execute(sql)
con.commit()
con.close()


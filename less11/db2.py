import psycopg2
import psycopg2.extras

con = psycopg2.connect(host="127.0.0.1", database="mypythontestdb",
                       user="postgres",password="Univer123",port=5433)

cur = con.cursor(cursor_factory = psycopg2.extras.DictCursor)
# sql="insert into clients(name, last_name) values('aaa','bbb')"
# cur.execute(sql)
# con.commit()
sql = "select * from clients"
cur.execute(sql)
for row in cur:
    # print(str(row[0])+" "+row[1]+" "+row[2])
    print(str(row["id"]) + " " + row["name"] + " " + row["last_name"])
con.close()


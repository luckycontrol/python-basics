import pymysql

db = pymysql.connect(
    host='192.168.1.33',
    port=3306,
    user='employees',
    passwd='976763',
    db='employees',
    charset='utf8',
    autocommit=True
)

cursor = db.cursor()
cursor.execute("show tables")
data = cursor.fetchall()
print(data)
db.close()
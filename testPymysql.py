import pymysql

db = pymysql.connect(user='root', password='123qwe', database='python39')
cur = db.cursor()
# db.begin()
# cur.execute('show tables')
# print(cur.fetchall())
#  cur.execute('create table test1 (FIRST_NAME CHAR(20) NOT NULL,LAST_NAME VARCHAR(8),AGE INT,SEX CHAR(1),INCOME FLOAT)')
# cur.execute('show tables')
# print(cur.fetchall())
# db.rollback()
cur.execute('show tables')
print(cur.fetchall())
cur.execute('select * from test1')
print(cur.fetchall())
data = ('Mac', 'Mohan', 20, 'M', 2000), ('Macdddd', 'Mohanddd', 10, 'M', 1000.3)
cur.executemany('INSERT INTO test1 values (%s, %s, %s, %s, %s)', data)
cur.execute('select * from test1')
print(cur.fetchall())
# db.rollback()
cur.close()
db.commit()
db.close()
import pymysql.cursors

# 创建连接
config = {
          'user':'root',
          'password':'Bg1234',
          'host':'192.168.15.211',
          'port':3306,
          'database':'bgdb'}
conn = pymysql.connect(**config)

# 创建游标
cur = conn.cursor()

# 执行查询SQL
sql = "select * from student"
cur.execute(sql)

# 获取查询结果
result_set = cur.fetchall()
if result_set:
    for row in result_set:
        print ("%s, %s, %s, %s, %s, %s" % (row[0],row[1],row[2],row[3],row[4],row[5]))

# 关闭游标和连接
cur.close()
conn.close()

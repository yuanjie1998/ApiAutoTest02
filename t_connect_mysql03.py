import pymysql

conn = pymysql.connect(host='191.0.0.200',
                       user='admin',
                       passwd='123456',
                       port=3306,
                       db='lgywdutynew',
                       charset='utf8')
list01 = []
tuple01 = tuple()
cursor = conn.cursor()

sql = "SELECT * FROM `lgywsoft_tags_sso_user` WHERE loginName LIKE '%应急管理局' ORDER BY id DESC"
cursor.execute(sql)
dataAll = cursor.fetchall()

# 循环结果
for n in dataAll:
    print(n)
    for j in n:
        if j == "光明区应急管理局":
            print(j)

# 关闭游标、连接
cursor.close()
conn.close()


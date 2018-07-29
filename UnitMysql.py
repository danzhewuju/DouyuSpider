#!/usr/bin/python
import pymysql
from Host_info import *
import time,datetime


class Unit_Mysql:
    def connect_db(self):
        return pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            database='douyu',
            charset='utf8'
        )

    def insert_db(self, host):
        con = self.connect_db()
        cur = con.cursor()
        try:
            sql_str = "insert into host_info  (username, kind, timestamp, w_number, room_number, link, online, " \
                      "coefficient)" \
                      " values ('%s', '%s','%s','%s','%s','%s','%s','%s')" \
                      % (host.username, host.kind, host.localtime, host.w_number, host.room_number, host.link,
                         host.online, host.coefficient)
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print("插入错误!")
            raise
        finally:
            cur.close()
            con.close()


# host = Host()
# host.username = "大仙"
# host.kind = "王者荣耀"

# for index in range(10):
#     time1 = int(time.time())
#     print(time1)
#     timearray = time.localtime(time1)
#     datetime1 = time.strftime("%Y-%m-%d %H:%M:%S")
#     print(datetime1)
# time1 = int(time.time())
# print(time1)
# timearray = time.localtime(time1)
# print(timearray)
# datetime1 = time.strftime("%Y-%m-%d %H:%M:%S")
# print(datetime1)


# print(host.localtime)
# host.w_number = 1960000
# host.followers = 12000000
# host.coefficient = host.w_number / host.followers
# user =Unit_Mysql()
# user.insert_db(host)

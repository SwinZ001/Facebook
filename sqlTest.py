import pymysql

class Db_utils():
    # 将数据库相关内容进行封装：
    def __init__(self,host,database,user,password):
        try:
            self.db = pymysql.connect(host=host,database=database,user=user,password=password)
            # 获取游标
            self.cursor = self.db.cursor()
            print("数据库连接成功")
        except pymysql.Error as e:
            print("数据库连接失败"+str(e))


    def create_table(self,table_name):
        try:
            self.cursor.execute("drop table if exists "+table_name)
            self.cursor.execute("create table "+table_name+"(id int auto_increment primary key,usename char(255) not null,type char(255),state char(255))")
            print("表格创建成功")
        except pymysql.Error as e:
            print("表格创建失败"+str(e))

    # 封装查询
    def sql_select(self, sql):
        self.cursor.execute(sql)  # 执行sql语句
        '''
        fetchone()函数它的返回值是单个的元组,也就是一行记录,如果没有结果,那就会返回null
        其次是fetchall()函数,它的返回值是多个元组,即返回多个行记录,如果没有结果,返回的是()
        '''
        all = self.cursor.fetchall()  # 用变量名all来接收游标返回的所有内容
        self.db.commit()
        return all

    # 封装新增
    def sql_add(self,sql,*value):
        try:
            ad = self.cursor.execute(sql,*value)  # 执行sql语句, 用变量ad来承接执行语句，返回受影响的行数，比如影响0行，返回0
            self.db.commit()  # 确认
            return print("添加成功"+str(ad))
        except pymysql.Error as e:
            return print("添加失败"+str(e))


    # 封装修改
    def sql_update(self, sql):
        up = self.cursor.execute(sql)  # 执行sql语句, 用变量up来承接执行语句，返回受影响的行数，比如影响0行，返回0
        self.db.commit()  # 确认
        return up

    # 封装删除
    def sql_delete(self, sql,*value):
        try:
            de = self.cursor.execute(sql,*value)  # 执行sql语句, 用变量de来承接执行语句，返回受影响的行数，比如影响0行，返回0
            self.db.commit()  # 确认
            return print("删除成功"+str(de))
        except pymysql.Error as e:
            return print("删除失败" + str(e))

    def closs_db(self):
        self.cursor.close()
        self.db.close()

# if __name__ == "__main__":
#     db=Db_utils(host="localhost",database="test",user="root",password="123456")
#     # db.create_table("userData")
#     try:
#         # db.cursor.execute("insert into userdata values(null,1,2,3)")
#         # db.commit()
#     except pymysql.Error as e:
#         print(str(e))
"""
作者：仲启瑞
联系方式：
TEL:18305125976
QQ：1062127784
"""
# 创建数据库基本框架

import pymysql  #导入下载的pymysql包

# 创建admin表
def create_admin_table(db):


    # 创建游标对象
    cur = db.cursor()

    # 创建表格的SQL语句
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """
    try:
        # 执行SQL语句创建表格
        cur.execute(create_table_sql)
        print(f"Table 'admin' created successfully or already exists!")

        db.commit()  # 提交更改
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()  # 发生错误时回滚

def create_admin_wait_table(db):


    # 创建游标对象
    cur = db.cursor()

    # 创建表格的SQL语句
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS admin_wait (
        admin_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """
    try:
        # 执行SQL语句创建表格
        cur.execute(create_table_sql)
        print(f"Table 'admin' created successfully or already exists!")

        db.commit()  # 提交更改
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()  # 发生错误时回滚

def create_stu_table(db):


    # 创建游标对象
    cur = db.cursor()

    # 创建表格的SQL语句
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS stu (
        stu_id VARCHAR(50) PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """
    try:
        # 执行SQL语句创建表格
        cur.execute(create_table_sql)
        print(f"Table 'stu' created successfully or already exists!")

        db.commit()  # 提交更改
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()  # 发生错误时回滚

def create_stu_wait_table(db):


    # 创建游标对象
    cur = db.cursor()

    # 创建表格的SQL语句
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS stu_wait (
        stu_id VARCHAR(50) PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """
    try:
        # 执行SQL语句创建表格
        cur.execute(create_table_sql)
        print(f"Table 'stu' created successfully or already exists!")

        db.commit()  # 提交更改
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()  # 发生错误时回滚

def create_book_table(db):


    # 创建游标对象
    cur = db.cursor()

    # 创建表格的SQL语句
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS book (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        bookname VARCHAR(50) NOT NULL UNIQUE,
        author VARCHAR(55) NOT NULL,
        publisher VARCHAR(55) NOT NULL,
        num INT NOT NULL
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """
    try:
        # 执行SQL语句创建表格
        cur.execute(create_table_sql)
        print(f"Table 'book' created successfully or already exists!")

        db.commit()  # 提交更改
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()  # 发生错误时回滚

def create_lrbook_table(db):

    # 创建游标对象
    cur = db.cursor()

    # 创建表格的SQL语句
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS lrbook (
        id INT AUTO_INCREMENT PRIMARY KEY,
        stu_id VARCHAR(50) NOT NULL,
        book_id VARCHAR(55) NOT NULL,
        lend_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        return_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """
    try:
        # 执行SQL语句创建表格
        cur.execute(create_table_sql)
        print(f"Table 'lrbook' created successfully or already exists!")

        db.commit()  # 提交更改
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()  # 发生错误时回滚

def insert_first(db):
    username = "root"
    password = "123456"
    insert_root_sql = """
    INSERT INTO admin (username, password)
            VALUES (%s, %s)
    """
    try:
        cur.execute(insert_root_sql, (username, password))
        db.commit()
        print("Admin account registered successfully!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        return False
    finally:
        cur.close()




db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     charset='utf8')
#用connec方法连接数据库 host:本机地址 port:端口号 user:用户名 passwd:密码
# database:要操作的数据库 charset:字符集类型


cur = db.cursor()   #生产游标对象（操作数据库执行sql语句获取结果的对象）

create_db_sql = "CREATE DATABASE exp3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

try:
    # 执行SQL语句创建数据库
    cur.execute(create_db_sql)
    print("Database created successfully!")

    db.commit()  # 提交更改
except Exception as e:
    print(f"Error: {e}")
    db.rollback()  # 发生错误时回滚

cur.execute("use exp3;")
create_admin_table(db)
create_admin_wait_table(db)
create_stu_table(db)
create_stu_wait_table(db)
create_book_table(db)
create_lrbook_table(db)
insert_first(db)


#关闭游标和数据库
cur.close()
db.close()
"""
作者：仲启瑞
联系方式：
TEL:18305125976
QQ：1062127784
"""
import pymysql
import utils

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='exp3',
                     charset='utf8')



while True:
    print("Enter 1: admin")
    print("Enter 2: user")
    print("Enter 0: exit")

    flag1 = input("input your response: ")
    if flag1 == "0":
        break

    if flag1 == "1":
        print("Enter 1: log in")
        print("Enter 2: sign up")
        print("Enter 0: exit")
        flag2 = input("input your response: ")
        if flag2 == "1":
            username = input("username: ")
            password = input("password: ")
            admin = utils.Admin(username, password)
            admin_id = admin.login_admin(db)
            if admin_id:
                print("Admin login successful, admin_id:", admin_id[0])
                while True:
                    print("Enter 1: add book")
                    print("Enter 2: search book")
                    print("Enter 0: exit")
                    flag3 = input("input your response: ")
                    if flag3 == "0":
                        break
                    if flag3 == "1":
                        bookname = input("Book name: ")
                        author = input("Author: ")
                        publisher = input("Publisher: ")
                        num = int(input("Number of copies: "))
                        if (admin.add_book(db, bookname, author, publisher, num)):
                            print("Success")
                        else:
                            print("Fail")

                    if flag3 == "2":
                        booklist = utils.search_book(db)
                        for row in booklist:
                            print(row)
            else:
                print("username or password error")
        if flag2 == "2":
            username = input("username: ")
            password = input("password: ")
            admin = utils.Admin(username, password)
            admin.register_admin(db)
        if flag2 == "3":
            username = input("username: ")
            password = input("password: ")
            admin = utils.Admin(username, password)
            admin_id = admin.login_admin(db)
            if admin_id:
                bookname = input("Book name: ")
                author = input("Author: ")
                publisher = input("Publisher: ")
                num = int(input("Number of copies: "))
                admin.add_book(db, bookname, author, publisher, num)
            else:
                print("Admin authentication required to add books.")

    if flag1 == "2":
        print("Enter 1: log in")
        print("Enter 2: sign up")
        print("Enter 0: exit")
        flag2 = input("input your response: ")
        if flag2 == "1":
            stu_id = input("stu_id: ")
            password = input("password: ")
            student = utils.Student(stu_id, "", password)
            stu_id = student.login_student(db)
            if stu_id[0]:
                print("Student login successful, stu_id:", stu_id[0]," username:",stu_id[1])
                while True:
                    print("Enter 1: borrow book")
                    print("Enter 2: return book")
                    print("Enter 3: search book")
                    print("Enter 4: show return book")
                    print("Enter 0: exit")
                    flag3 = input("input your response: ")
                    if flag3 == "0":
                        break
                    if flag3 == "1":
                        booklist = utils.search_book(db)
                        for row in booklist:
                            print(row)
                        book_id = int(input("book id: "))
                        student.borrow_book(db, book_id)
                    if flag3 == "2":
                        result = student.show_borrowed_books(db)
                        if result:
                            print("未归还的书:")
                            for row in result:
                                lend_time = row[3].strftime('%Y-%m-%d %H:%M:%S')
                                print(f"Borrow ID: {row[0]}, Book Name: {row[1]}, Author: {row[2]}, Lend Time: {lend_time}")
                            borrow_id = int(input("borrow id: "))
                            student.return_book(db, borrow_id)
                        else:
                            print("没有未归还的书")
                    if flag3 == "3":
                        booklist = utils.search_book(db)
                        for row in booklist:
                            print(row)

                    if flag3 == "4":
                        result = student.show_borrowed_books(db)
                        print(result)
                        if result:
                            print("未归还的书:")
                            for row in result:
                                lend_time = row[3].strftime('%Y-%m-%d %H:%M:%S')
                                print(
                                    f"Borrow ID: {row[0]}, Book Name: {row[1]}, Author: {row[2]}, Lend Time: {lend_time}")
                        else:
                            print("没有未归还的书")
            else:
                print("username or password error")
        else:
            stu_id = input("请输入学号: ")
            username = input("请输入姓名: ")
            password = input("请输入密码: ")
            student = utils.Student(stu_id, username, password)
            student.register_student(db)

db.close()

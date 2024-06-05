"""
作者：仲启瑞
联系方式：
TEL:18305125976
QQ：1062127784
"""
import pymysql
# import hashlib

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_admin(self, db):
        cur = db.cursor()

        insert_admin_sql = """
        INSERT INTO admin_wait (username, password)
        VALUES (%s, %s)
        """
        try:
            cur.execute(insert_admin_sql, (self.username, self.password))
            db.commit()
            print("Admin account registered successfully!")
            return True
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
            return False
        finally:
            cur.close()

    def login_admin(self, db):
        db.commit()
        cur = db.cursor()

        admin_sql = """
        SELECT admin_id FROM admin WHERE username = %s AND password = %s
        """
        cur.execute(admin_sql, (self.username, self.password))
        admin_result = cur.fetchone()
        cur.close()
        return admin_result

    def add_book(self, db, bookname, author, publisher, num):
        cur = db.cursor()
        insert_book_sql = """
        INSERT INTO book (bookname, author, publisher, num)
        VALUES (%s, %s, %s, %s)
        """
        try:
            cur.execute(insert_book_sql, (bookname, author, publisher, num))
            db.commit()
            print("Book added successfully!")
            cur.close()
            return True
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
            cur.close()
            return False

class Student:
    def __init__(self, stu_id, username, password):
        self.stu_id = stu_id
        self.username = username
        self.password = password

    def register_student(self, db):
        cur = db.cursor()
        insert_student_sql = """
        INSERT INTO stu_wait (stu_id, username, password)
        VALUES (%s, %s, %s)
        """
        try:
            cur.execute(insert_student_sql, (self.stu_id, self.username, self.password))
            db.commit()
            print("Student account registered successfully!")
            return True
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
            return False
        finally:
            cur.close()

    def login_student(self, db):
        cur = db.cursor()

        student_sql = """
        SELECT stu_id,username FROM stu WHERE stu_id = %s AND password = %s
        """
        cur.execute(student_sql, (self.stu_id,self.password))
        student_result = cur.fetchone()
        cur.close()
        return student_result

    def borrow_book(self, db, book_id):
        cur = db.cursor()
        check_stock_sql = "SELECT num FROM book WHERE book_id = %s"
        cur.execute(check_stock_sql, (book_id))
        result = cur.fetchone()

        if result[0] and result[0] > 0:
            update_book_sql = "UPDATE book SET num = num - 1 WHERE book_id = %s"
            insert_borrow_sql = "INSERT INTO lrbook (stu_id, book_id, lend_time, return_time) VALUES ((SELECT stu_id FROM stu WHERE stu_id = %s), %s, CURRENT_TIMESTAMP, NULL)"
            try:
                cur.execute(update_book_sql, (book_id,))
                print(self.stu_id)
                cur.execute(insert_borrow_sql, (self.stu_id[0], book_id,))
                db.commit()
                print("Book borrowed successfully!")
                return True
            except Exception as e:
                print(f"Error: {e}")
                db.rollback()
                return False
            finally:
                cur.close()
        else:
            print("Book is not available for borrowing.")

    def return_book(self, db, borrow_id):
        cur = db.cursor()
        get_book_id_sql = "SELECT book_id FROM lrbook WHERE id = %s AND return_time IS NULL"
        cur.execute(get_book_id_sql, (borrow_id,))
        result = cur.fetchone()
        if result:
            book_id = result[0]
            update_book_sql = "UPDATE book SET num = num + 1 WHERE book_id = %s"
            update_borrow_sql = "UPDATE lrbook SET return_time = CURRENT_TIMESTAMP WHERE id = %s"
            try:
                cur.execute(update_book_sql, (book_id,))
                cur.execute(update_borrow_sql, (borrow_id,))
                db.commit()
                print("Book returned successfully!")
                return True
            except Exception as e:
                print(f"Error: {e}")
                db.rollback()
                return False
            finally:
                cur.close()
        else:
            print("No active borrow record found for this ID.")

    def show_borrowed_books(self, db):
        cur = db.cursor()
        show_books_sql = """
        SELECT lrbook.id, book.bookname, book.author, lrbook.lend_time
        FROM lrbook
        JOIN book ON lrbook.book_id = book.book_id
        WHERE lrbook.return_time IS NULL AND lrbook.stu_id = %s
        """
        try:
            cur.execute(show_books_sql, (self.stu_id))
            result = cur.fetchall()
            if result:
                return result
            else:
                print("No borrowed books.")
                return None
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cur.close()


def search_book(db):
    db.commit()
    cur = db.cursor()
    seqrch_book_sql = """
    select * from book;
    """
    try:
        cur.execute(seqrch_book_sql)
        results = cur.fetchall()
        return results
    except Exception as e:
        print(f"Error: {e}")
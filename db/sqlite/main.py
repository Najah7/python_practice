import sqlite3

# NOTE:基本的にexecuteを使って普通のSQL操作
# 覚えるのはconnect、cursorオブジェクトの作成、commit、close、くらい

def main():
    # create new db or connect db that already exits
    db = sqlite3.connect('test_sqlite.db')
    
    # メモリ上に作る場合（on memory）
    # db = sqlite3.connect(':memory:')
    
    # make cursur instance
    cursor = db.cursor()
    
    # HACK:この書き方だとsqlite3の.schemaの時に表示おかしい
    try :
        cursor.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING )')
    except: pass
    
    try:
        cursor.execute('INSERT INTO persons (name) VALUES ("test1")')
    except:pass
    
    cursor.execute('SELECT * FROM persons')
    print(cursor.fetchall())
    
    try:
        for i in range(2, 4):
            cursor.execute(f'INSERT INTO persons (name) VALUES ("test{i}")')
    except: pass
    
    try:
        cursor.execute('UPDATE persons SET name = "new_name" WHERE name = "test1"')
    except: pass
    
    
    db.commit()
    
    # close connection
    cursor.close()
    db.close()
    
    
    
if __name__=='__main__':
    main()
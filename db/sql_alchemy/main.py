from dotenv import load_dotenv
import os
load_dotenv()

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# NOTE:最初のengineさえ変えればSQLite⇔MySQLの変更が容易にできる。（再利用性up）

# select database engine
# NOTE:キーワード引数echo=Trueにしたら、SQLALCHEMYの行ったクエリを確認することができる（最適化などで使える）
engine = sqlalchemy.create_engine('sqlite:///test.db')

# MySQLの場合(test_mysql_databaseはデータベース名。先に、作成しておく必要があるかも？)
# NOTE:mysql+[pymysql or mysqlconnector]://[user]:[password]@[host]/database_name
engine = sqlalchemy.create_engine(
    f'mysql+pymysql://root:{os.environ.get("MYSQL_PASSWORD")}@localhost/test_mysql_database',
)

# prepare to make schema of database
Base = sqlalchemy.ext.declarative.declarative_base()

# make schema of database
class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.INTEGER,
        primary_key=True,
        autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))

# create tables
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# It's same as INSERT
person1 = Person(name='test')
session.add(person1)
person2 = Person(name='test2')
session.add(person2)
session.commit()

# It's samae as UPDATE
person3 = session.query(Person).filter_by(name='test2').first()
person3.name = 'new_name+++++'
session.add(person3)
session.commit()

# It's same as DEELTE
person4 = session.query(Person).filter_by(name='test').first()
session.delete(person4)
session.commit()

# It's same as SELECT 
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
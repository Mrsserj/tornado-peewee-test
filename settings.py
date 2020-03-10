from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database='test',
    user='postgres',
    password='123',
    host='localhost')


if __name__ == "__main__":
    print(db.database)
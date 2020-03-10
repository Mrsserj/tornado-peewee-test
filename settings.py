from peewee_async import PooledPostgresqlDatabase

db = PooledPostgresqlDatabase(
    database='test',
    user='postgres',
    password='123',
    host='localhost')

login_url = "/login"


if __name__ == "__main__":
    print(db.database)
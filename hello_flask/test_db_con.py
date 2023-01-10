import psycopg2
from config_postgresql import config


def connect():
    connection = None
    try:
        params = config()
        print('Подключение к базе данных PostgresQL ...')
        connection = psycopg2.connect(**params)
        with connection.cursor() as crsr:
            print('Версия бызы данных PostgresQL: ')
            crsr.execute('SELECT VERSION()')
            db_version = crsr.fetchall()
            print(db_version)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Подключение к базе данных прервано.')


if __name__ == '__main__':
    connect()

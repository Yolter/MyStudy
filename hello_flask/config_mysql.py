from configparser import ConfigParser

import mysql.connector.errors
from mysql.connector import connect


class ConnectError(Exception):
    pass


class UseDatabase:
    def __init__(self, conf: dict) -> None:
        self.configuration = conf

    def __enter__(self) -> 'db cursor':
        try:
            self.conn = connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def config(filename='db_mysql.ini', section='mysql') -> dict:
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1}'
                        ' file.'.format(section, filename))
    return db


if __name__ == '__main__':
    config()

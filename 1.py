import datetime as dt

date_format = '%d.%m.%Y'
now = dt.datetime.now()
now_date = now.date()
today = now_date.strftime(date_format)


class Record:
    def __init__(self, amount, comment, date=today):
        self.amount = amount
        self.comment = comment
        self.date = date

    def print(self):
        print(self.amount, self.comment, self.date)
        print()


if __name__ == '__main__':
    r1 = Record(10, 'first recording')
    r2 = Record(20, 'second recording', '10.11.2022')
    r3 = Record(30, 'third recording', '09.11.2022')
    r4 = Record(40, 'fourth record', '02.11.2022')

    n = dt.datetime.strptime('10.11.2022', date_format)
    m = dt.datetime.now() - n

    r1.print()
    print(n)



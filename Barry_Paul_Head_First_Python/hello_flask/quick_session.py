from flask import Flask, session


app = Flask(__name__)


app.secret_key = 'YouWon_tGuess'


@app.route('/setuser/<user>')
def set_user(user: str) -> str:
    session['user'] = user
    return 'Установлено значение пользователя: ' + session['user']


@app.route('/getuser')
def get_user() -> str:
    return 'Пользовательское значение в данный момент установлено на: '\
        + session['user']


if __name__ == '__main__':
    app.run(debug=True)



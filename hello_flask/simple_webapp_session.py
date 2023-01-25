from flask import Flask, session


app = Flask(__name__)

app.secret_key = 'YouWon_tGuess'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'Теперь вы в системе!'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'Вы теперь не в системе!'


@app.route('/status')
def chek_status() -> str:
    if 'logged_in' in session:
        return 'Вы сейчас в системе.'
    return 'Вы сейчас не в системе.'


@app.route('/')
def hello() -> str:
    return 'Привет, ты в приложении для изучения сессий!'


@app.route('/page1')
def page1() -> str:
    return 'Это страница №1'


@app.route('/page2')
def page2() -> str:
    return 'Это страница №2'


@app.route('/page3')
def page3() -> str:
    return 'Это страница №3'


if __name__ == '__main__':
    app.run(debug=True)

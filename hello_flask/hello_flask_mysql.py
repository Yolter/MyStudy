from flask import Flask, render_template, request, session  # escape, redirect
from vsearch import search4letters
from config_mysql import config, UseDatabase, ConnectError
from checker import check_logged_in


app = Flask(__name__)

app.secret_key = 'YouWon_tGuess'


# def hello() -> '302':
#     return redirect('/entry')
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep=' | ')
    with UseDatabase(config()) as crsr:
        _SQL = """INSERT INTO log
                  (phrase, letters, ip, browser_string, results)
                  VALUES
                  (%s, %s, %s, %s, %s)"""
        crsr.execute(_SQL, (req.form['phrase'], req.form['letters'],
                            req.remote_addr, str(req.user_agent), res))


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'Теперь вы в системе!'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'Вы теперь не в системе!'


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the Web!')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    if not search4letters(phrase, letters):
        results = 'Совпадений не найдено'
    else:
        results = str(search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print('***** Логирование прервано из-за этой ошибки: ', str(err))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/viewlog')
@check_logged_in
def viewlog() -> 'html':
    try:
        with UseDatabase(config()) as crsr:
            _SQL = """SELECT * FROM log"""
            crsr.execute(_SQL)
            contents = crsr.fetchall()
        titles = ('Id', 'Time Stamp', 'Phrase', 'Letters',
                  'Ip', 'User_agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,)
    except ConnectError as err:
        print('База данных точно подключена? Ошибка: ', str(err))
    except Exception as err:
        print('Что то пошло не так. Ошибка: ', str(err))
    return 'Ошибка'


if __name__ == '__main__':
    app.run(debug=True)

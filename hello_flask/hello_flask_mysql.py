from flask import Flask, render_template, request, escape  # redirect
from vsearch import search4letters
from config_mysql import config, UseDatabase


app = Flask(__name__)


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


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    if not search4letters(phrase, letters):
        results = 'No matches found'
    else:
        results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the Web!')


@app.route('/viewlog')
def viewlog() -> 'html':
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


if __name__ == '__main__':
    app.run(debug=True)

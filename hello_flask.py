from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Димон, брат, как дела? привет тебе с моего ноута!'


app.run()

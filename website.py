from flask import Flask


app = Flask('website')


@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    from elsa import cli
    cli(app, base_url='http://pyvo.hroncok.cz')

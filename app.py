from flask import Flask

app = Flask(__name__)
app.config['FLASK_APP'] = 'app'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


@app.route('/')
def index():
    return {'message': 'Olá!'}


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('dataset-encode0.html')


if __name__ == '__main__':
    app.run()

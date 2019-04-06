from flask import Flask, render_template
from data import Article

article = Article()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', article=article)

@app.route('/articles/<id>')
def articles_content(id):
    return render_template('articles_content.html', id=id)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/html')
def html():
    return render_template('html.html')

@app.route('/css')
def css():
    return render_template('css.html')

@app.route('/javascript')
def javascript():
    return render_template('javascript.html')

@app.route("/create Account")
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask , render_template
from db import articles
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def article():
    return render_template('articles.html', articles=articles)

@app.route('/articles/<id>')
def articles1(id):
    return render_template('article.html', id=id)

if __name__ == '__main__':
    app.run(debug=True , port=4000)

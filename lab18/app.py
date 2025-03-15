from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    books = [
        {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'},
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
        {'title': '1984', 'author': 'George Orwell'}
    ]
    return render_template('index.html', books=books, title="Book List")

if __name__ == '__main__':
    app.run(debug=True)

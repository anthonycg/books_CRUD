from flask_app.models import book
from flask_app.config import mysqlconnection
from flask import render_template, flash, request, session, redirect
from flask_app import app

@app.route('/books')
def books():
    all_books = book.Book.get_all()
    return render_template('books.html', all_books = all_books)

@app.route('/create/book', methods=['POST'])
def create_book():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    book.Book.save(data)
    return redirect ('/books')




from crypt import methods
import imp
from re import A
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.config import mysqlconnection
from flask import render_template, flash, request, session, redirect
from flask_app import app

@app.route('/')
def index():
    all_authors = Author.get_all()
    return render_template('authors.html', all_authors = all_authors)

@app.route('/authors', methods=['POST'])
def authors():
    data = {
        "name": request.form['name']
    }
    Author.save(data)
    Author.get_all()
    return redirect('/')

@app.route('/author/<int:id>')
def author_favs(id):
    #set data to data needed to render template
    data = {
        "id": id
    }
    #identify author 
    author = Author.get_all
    #populate the select form with all other books available
    return render_template('show_author.html', author = author, author_favorites=Author.get_favs(data), all_books = Book.get_all())

@app.route('/author/process/<int:id>', methods=['POST'])
def add_author_favs(id):
    #set data to needed data -- id
    data = {
        "id": id
    }
    Author.get_favs(data)
    return redirect('/author/<int:id>')

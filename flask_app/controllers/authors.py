import imp
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
    #get all of current author's favorite books

    #populate the select form with all other books available
    return render_template('show_author.html', author_favorites=Author.get_favs(data), all_books = Book.get_all())

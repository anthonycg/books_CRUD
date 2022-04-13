from crypt import methods
from flask_app.models.author import Author
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

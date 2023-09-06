from app import app
from flask import render_template

@app.route('/produtos')
def store():
    return render_template('store.html')
from app import app
from flask import render_template


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/idols')
def idol():
    context = {
        "customer_name" : "Brian",
        "customer_username": "bjohn",
        "person":{
            1: 'William',
            2: 'Brad',
            3: 'David',
            4: 'Robert'
        }
    }
    return render_template('idols.html', **context)
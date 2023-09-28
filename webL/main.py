from webL import app
from flask import render_template, request, redirect, url_for

import sqlite3
import logging
from logging.handlers import RotatingFileHandler
import datetime

DATABASE = 'database.db'

@app.route('/')
def index():
    date_obj = datetime.date.today()  # '2022-09-08'
    date_str = '{date_obj.year}-{date_obj.month}-{date_obj.day} '
    
    time_str2 = datetime.datetime.now().time()
    time_obj = datetime.datetime.now().time()
    time_str2 = '{time_obj.hour}:{time_obj.minute}:{time_obj.second}'

    # wdate =  '{datetime.datetime.now().year()}' 
    # + str(datetime.datetime.now().month()) + '/'
    # + str(datetime.datetime.now().day())

    app.logger.debug(date_str) 
    app.logger.debug(time_str2)
    print(date_str)
    # app.logger.debug(str(datetime.datetime.now().year()))

    # date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    date = date_str
    time = datetime.datetime.strptime(time_str2, '%H:%M:%S').time()
    app.logger.debug('[{date} {time}]/ ((main.py))')

    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()
    con.close()

    books=[]

    for row in db_books:
        books.append(
            {'title': row[0], 'price': row[1], 'arrival_day': row[2]})

    return render_template(
        'index.html',
        books=books
    )


@app.route('/ee')
def index2():
    bookA = {
        'title': 'play boos',
        'price': 1230,
        'arrival_day': '2023年8月23日'
    }
    bookN = []
    books = [{
        'title':'play boos',
        'price':1230,
        'arrival_day':'2023年8月23日'
    },
    {
        'title': 'gay boos',
        'price': 3230,
        'arrival_day': '2032年8月3日'

    }]
    # return '<h1>Hello World!</h1>'
    return render_template(
        'index.html',
        books=books
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )
@app.route('/register',methods=['POST'])
def register():
    app.logger.info('/register (main.py)')

    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    app.logger.info('INSERT INTO books (main.py)')
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?,?,?)', [title, price, arrival_day])
    con.commit()
    con.close()

    return redirect(url_for('index'))


# ログの設定
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

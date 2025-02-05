from flask import Flask, render_template, request, redirect, url_for, flash,render_template
import sqlite3
from datetime import datetime
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection():
    conn = sqlite3.connect('tire_shop.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        custom_tire_id = request.form['custom_tire_id']
        tire_name = request.form['tire_name']
        buyer_name = request.form['buyer_name']
        # Update to include time in the format YYYY-MM-DD HH:MM:SS
        date_sold = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO tires (custom_tire_id, tire_name, date_sold, buyer_name) VALUES (?, ?, ?, ?)', 
                         (custom_tire_id, tire_name, date_sold, buyer_name))
            conn.commit()
            flash('تم اضافه عميله بيع بنجاح', 'success')
        except sqlite3.IntegrityError:
            flash('هذه العمليه مسجله من قبل', 'error')
        finally:
            conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')


from datetime import datetime

@app.route('/search/<type>', methods=['GET', 'POST'])
def search(type):
    if request.method == 'POST':
        conn = get_db_connection()
        results = []
        if type == 'date_sold':
            year = request.form.get('year')
            month = request.form.get('month')
            day = request.form.get('day')
            search_term = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            logging.debug("Searching for date: %s", search_term)
            # Update the query to only compare the date part of the datetime
            results = conn.execute('SELECT * FROM tires WHERE date(date_sold) = date(?) ORDER BY date_sold DESC', (search_term,)).fetchall()            
            logging.debug("Number of results found: %d", len(results))
        elif type == 'custom_tire_id':
            search_term = request.form['search_term']
            results = conn.execute('SELECT * FROM tires WHERE custom_tire_id = ?', (search_term,)).fetchall()
        elif type == 'buyer_name':
            search_term = request.form['search_term']
            # Include ORDER BY clause to sort results from newer to older
            results = conn.execute('SELECT * FROM tires WHERE buyer_name LIKE ? ORDER BY date_sold DESC', ('%' + search_term + '%',)).fetchall()        
            conn.close()
        return render_template('search_results.html', results=results, type=type)
    return render_template('search.html', type=type)

@app.route('/index')
def index():
    conn = get_db_connection()
    tires = conn.execute('SELECT * FROM tires ORDER BY date_sold DESC').fetchall()
    conn.close()
    return render_template('index.html', tires=tires)

if __name__ == '__main__':
    app.run(debug=True)

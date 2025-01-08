from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = 'Sql@2024'  
app.config['MYSQL_DB'] = 'KIET'

mysql = MySQL(app)
@app.route('/')
def index():
    return render_template('data.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        roll = request.form['roll']
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        sex = request.form['sex']

    try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO x (roll,name,age,phone,sex) VALUES (%s, %s, %s,%s,%s)", (roll,name,age,phone,sex))
            mysql.connection.commit()
            cur.close()
            flash("Data Submitted Successfully!", "success")
            return redirect('/')
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)
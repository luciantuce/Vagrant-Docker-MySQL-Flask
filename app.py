#!/usr/bin/python
from flask import *
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'P@ssw0rd'
app.config['MYSQL_DATABASE_DB'] = 'employees'
app.config['MYSQL_DATABASE_HOST'] = '10.0.2.15'
mysql.init_app(app)

#@app.route("/")
#def main():
#    return "Welcome!"
#    return render_template('index.html')

@app.route("/")
def db():
    cursor = mysql.connect().cursor()
    cursor.execute("select * from employees where birth_date = '1965-02-01' and hire_date > '1990-01-01' and gender = 'M' order by trim(last_name) asc, trim(first_name)")
    data = cursor.fetchall()
    return render_template("view.html", data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
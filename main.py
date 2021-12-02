
from flask import Flask

from flask import  render_template  
from flask import request
from flask import redirect
from flask import url_for
from flaskext.mysql import MySQL 


from flask import  flash

#Username: gdhtnQjxsZ

#Database name: gdhtnQjxsZ

#Password: gwMSTG4ARS

#Server: remotemysql.com

#Port: 3306

# initializations
app = Flask(__name__)

# Mysql Connection
mysql=MySQL() 
app.config['MYSQL_DATABASE_HOST']='remotemysql.com' 
app.config['MYSQL_DATABASE_USER']='gdhtnQjxsZ' 
app.config['MYSQL_DATABASE_PASSWORD']='gwMSTG4ARS' 
app.config['MYSQL_DATABASE_Db']='gdhtnQjxsZ' 


# settings
app.secret_key = "mysecretkey"

mysql.init_app(app) 

@app.route('/base') 
def index(): 
     
    sql='SELECT * FROM `gdhtnQjxsZ`.`contacts`;'
    conn=mysql.connect() 
    cursor=conn.cursor() 
    cursor.execute(sql) 

    data=cursor.fetchall()
    conn.commit() 
    return render_template('index.html', contacts = data) 


#############################


@app.route('/')
def pagina():
    return render_template("index1.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/servicios')
def servicios():
    return render_template("servicios.html")

@app.route('/ubicacion')
def ubicacion():
    return render_template("ubicacion.html")    

@app.route('/pagina')
def paginga():
    return render_template('index1.html')
"""

"""
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        
        conn=mysql.connect()
        cursor=conn.cursor()
       

        cursor.execute("INSERT INTO `gdhtnQjxsZ`.`contacts`  (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email)) 
        

        flash('Contacto agregado con exito')
       # data=cursor.fetchall()
        conn.commit()
    #return render_template('index.html' , contacts = data) 
    return redirect(url_for('index'))
@app.route('/edit/<string:id>', methods = ['POST', 'GET'])
def get_contact(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `gdhtnQjxsZ`.`contacts` WHERE id = {0}".format(id))
    data = cursor.fetchall()
    cursor.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])




@app.route('/update/<string:id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute("UPDATE `gdhtnQjxsZ`.`contacts` SET fullname = %s, email = %s, phone = %s WHERE id = %s",(fullname, email, phone, id))
        flash('Contacto actualizado')
        conn.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    
    cursor.execute('DELETE FROM `gdhtnQjxsZ`.`contacts` WHERE id = {0}'.format(id))
    conn.commit()
    flash('Contacto borrado')
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=3306)
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, request, render_template

app = Flask(_name_)

# Set up database connection
try:
    cnx = mysql.connector.connect(user='jack', password='1234',
                              host='wizard',
                              database='medical')
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

@app.route('/')
def home():
    return render_template('medical_records.html')

@app.route('/process', methods=['POST'])
def process():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    dob = request.form['dob']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zip = request.form['zip']
    condition = request.form['condition']
    medications = request.form['medications']
    insur_name = request.form['insur_name']
    policy_num = request.form['policy_num']
    group_num = request.form['group_num']
    insured_name = request.form['insured_name']
    insured_dob = request.form['insured_dob']
    insured_relation = request.form['insured_relation']
    insur_phone = request.form['insur_phone']
    pcp = request.form['pcp']
    notes = request.form['notes']
    
    # Insert data into database
    try:
        cursor.execute("INSERT INTO medical_records (name, email, phone, dob, address, city, state, zip, medical_condition, medications, insurance_name, policy_number, group_number, insured_name, insured_dob, insured_relationship, insurance_phone, pcp, notes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name, email, phone, dob, address, city, state, zip, condition, medications, insur_name, policy_num, group_num, insured_name, insured_dob, insured_relation, insur_phone, pcp, notes))
        cnx.commit()
        return 'Medical record added successfully!'
    except:
        return 'Error: Could not insert data into the database'

if _name_ == '_main_':
    app.run(debug=True)
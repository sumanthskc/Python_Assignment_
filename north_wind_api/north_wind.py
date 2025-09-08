from flask import Flask, request, jsonify
import mysql.connector as connection

app=Flask(__name__)
db=connection.connect(
    host="localhost",
    user="root",
    password="Suman@_2004",
    database="assignment_northwind"
)

cursor=db.cursor()

@app.route("/customers",methods=["POST"])
def insert_customer():
    data=request.json
    query="INSERT INTO customers (CustomerName, ContactName, Country) VALUES (%s, %s, %s)"
    cursor.execute(query,(data['CustomerName'],data['ContactName'],data["Country"]))
    db.commit()
    return jsonify({"message":"Customer added"}),201

@app.route("/customers/<int:id>",methods=["PUT"])
def update_customer(id):
    data=request.json
    query="UPDATE CUSTOMERS SET Customername=%s, ContactName=%s, Country=%s WHERE CustomerID=%s"
    cursor.execute(query,(data["CustomerName"],data["ContactName"],data["Country"],id))
    db.commit()
    return jsonify({"message":"Customer Updated!"})
@app.route('/customers', methods=['GET'])
def get_customers():
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
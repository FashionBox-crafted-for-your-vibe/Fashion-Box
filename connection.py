'''import mysql.connector as mysql

# Establish connection
con1 = mysql.connect(
    host="localhost",
    user="root",
    password="aadi1710",
    database="demo"
)

mycursor = con1.cursor()

ans = 'y'
while ans.lower() == 'y':
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    message = input("Enter your message: ")

    sql = "INSERT INTO customers (name, email, message) VALUES (%s, %s, %s)"
    val = (name, email, message)
    mycursor.execute(sql, val)
    con1.commit()

    print(mycursor.rowcount, "record inserted.")

    ans = input("Do you want to add more records? (y/n): ")

# Close connection after loop ends
con1.close()
print("Connection closed.")'''

from flask import Flask, request, redirect, render_template_string
import mysql.connector as mysql

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connect(
        host="localhost",
        user="root",
        password="aadi1710",
        database="demo"
    )

@app.route("/contact", methods=["POST"])
def contact():
    # Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Insert into MySQL
    con = get_db_connection()
    cursor = con.cursor()
    sql = "INSERT INTO customers (name, email, message) VALUES (%s, %s, %s)"
    val = (name, email, message)
    cursor.execute(sql, val)
    con.commit()
    cursor.close()
    con.close()

    return "✅ Your message has been saved successfully!"

# Optional: Home route to test server
@app.route("/")
def home():
    return "<h1>Flask MySQL Contact Form</h1><p>Go to /contact via the HTML form.</p>"

if __name__ == "__main__":
    app.run(debug=True)
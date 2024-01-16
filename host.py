from flask import Flask, request, jsonify, render_template
import pyodbc
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Create the connection string
# conn_str = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:saidhanushserver.database.windows.net,1433;Database=saidhanushdatabase007;Uid=saidhanushserver;Pwd=Aizen101;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
conn_str = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:saidhanushserver.database.windows.net,1433;Database=saidhanushdatabase007;Uid=saidhanushserver;Pwd=Aizen101;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/validate', methods=['GET', 'POST'])
def validate_credentials():
    if request.method == 'POST':
        data = request.get_json()

        # JSON payload looks like {"username": "user123", "password": "pass123"}
        username = data.get('username')
        password = data.get('password')

        # Execute a SQL query to fetch the credentials and check if both username and password match
        query = "SELECT * FROM credentials WHERE Username = ? AND Password = ?"
        result = cursor.execute(query, username, password).fetchone()

        # Check if the provided credentials are valid
        if result:
            return jsonify({"url": "https://enyopenaiservice.azurewebsites.net/#/"}), 200

        return jsonify({"message": "Invalid credentials"}), 401

    else:
        return jsonify({"message": "Method Not Allowed"}), 405

if __name__ == '__main__':
    app.run(port=5005)
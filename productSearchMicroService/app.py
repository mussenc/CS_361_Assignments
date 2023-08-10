from flask import Flask, json, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv, find_dotenv
import os

app = Flask(__name__)

# Configure .env file to hold these values
load_dotenv(find_dotenv())
app.config['MYSQL_HOST'] = os.environ.get("DBHOST")
app.config['MYSQL_USER'] = os.environ.get("DBUSER")
app.config['MYSQL_PASSWORD'] = os.environ.get("DBPW")
app.config['MYSQL_DB'] = os.environ.get("DB")
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

@app.route('/')
def root():
    return "Test successful"

@app.route('/productsearch/')
def green_energy_products():
    """
    Search Products table and return matching results as JSON
    """

    # Get query string parameters
    greenEnergyType = request.args.get('greenEnergyType', None)
    productID = request.args.get('productID', None)
    cost = request.args.get('cost', None)
    power = request.args.get('power', None)

    # No WHERE condition by default
    where = False
    comp_lookup = {'eq': '=', 'lt': '<', 'gt': '>', 'leq': '<=', 'geq': '>='}

    # Convert string parameters to SQL conditional syntax
    if greenEnergyType is not None:
        greenEnergyType = ' greenEnergyType = ' + greenEnergyType
        where = True
    if productID is not None:
        productID = ' productID = ' + productID
        if where is True:
            productID = ' AND' + productID
        where = True

    # Convert comparison parameters to SQL conditional syntax
    if cost is not None:
        q = cost.index('q')
        comp = comp_lookup[cost[0:q+1]]
        cost = f" cost {comp} '{cost[q+1:]}'"
        if where is True:
            cost = ' AND' + cost
        where = True
    if power is not None:
        q = power.index('q')
        comp = comp_lookup[power[0:q+1]]
        power = f" power {comp} '{power[q+1:]}'"
        if where is True:
            power = ' AND' + power
        where = True

    # Build query
    query = "SELECT * FROM GreenEnergyProducts"
    if where is True:
        query += " WHERE"
    for param in [greenEnergyType, productID, cost, power]:
        if param is not None:
             query += param
    query += ';'

    # Execute query and return as JSON
    cur = mysql.connection.cursor()
    cur.execute(query)
    results = json.dumps(cur.fetchall())
    return results


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6363))
    app.run(port=port, debug=True)
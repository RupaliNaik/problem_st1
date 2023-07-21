#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, jsonify
import json
import psycopg2

app = Flask(__name__)

# Replace these variables with your PostgreSQL database credentials
DB_HOST ='localhost'
DB_NAME ='my_db1'
DB_USER ='root'
DB_PASSWORD ='user@123'


def create_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def insert_housing_data(data):
    try:
        conn = create_connection()
        cur = conn.cursor()

        for item in data:
            cur.execute("INSERT INTO houses (location, sale_price) VALUES (%s, %s)", (item['location'], item['sale_price']))

        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print("Error inserting data:", e)
        return False

def execute_sql_query(query):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()[0]
        cur.close()
        conn.close()
        return result
    except Exception as e:
        print("Error executing query:", e)
        return None

@app.route('/store_data', methods=['POST'])
def store_data():
    try:
        data = json.loads(request.data)
        if insert_housing_data(data):
            return jsonify({"message": "Data stored successfully."}), 201
        else:
            return jsonify({"message": "Failed to store data."}), 500
    except Exception as e:
        return jsonify({"message": "Error processing request.", "error": str(e)}), 400

@app.route('/average_sale_price', methods=['GET'])
def average_sale_price():
    query = "SELECT AVG(sale_price) FROM houses"
    result = execute_sql_query(query)
    if result is not None:
        return jsonify({"average_sale_price": float(result)})
    else:
        return jsonify({"message": "Failed to retrieve average sale price."}), 500


# In[3]:


@app.route('/average_sale_price_per_location', methods=['GET'])
def average_sale_price_per_location():
    query = "SELECT location, AVG(sale_price) FROM houses GROUP BY location"
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(dict(results))
    except Exception as e:
        print("Error executing query:", e)
        return jsonify({"message": "Failed to retrieve average sale price per location."}), 500


# In[4]:


@app.route('/max_sale_price', methods=['GET'])
def max_sale_price():
    query = "SELECT MAX(sale_price) FROM houses"
    result = execute_sql_query(query)
    if result is not None:
        return jsonify({"max_sale_price": float(result)})
    else:
        return jsonify({"message": "Failed to retrieve max sale price."}), 500


# In[5]:


@app.route('/min_sale_price', methods=['GET'])
def min_sale_price():
    query = "SELECT MIN(sale_price) FROM houses"
    result = execute_sql_query(query)
    if result is not None:
        return jsonify({"min_sale_price": float(result)})
    else:
        return jsonify({"message": "Failed to retrieve min sale price."}), 500


# In[6]:


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





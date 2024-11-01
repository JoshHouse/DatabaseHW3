from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return connection
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        raise

@app.route('/api/update_basket_a', methods=['GET'])
def update_basket_a():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO public.basket_a (a, fruit_a) VALUES (%s, %s)', (5, 'Cherry'))
        connection.commit()
        connection.close()
        return jsonify({"status": "Success!"}), 200
    except Exception as e:
        print(f"Error in update_basket_a: {str(e)}")
        return jsonify({"status": "Error", "error": str(e)}), 500


@app.route('/api/unique')
def unique_fruits():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Fetch all fruits from basket_a and basket_b
        cursor.execute('SELECT fruit_a FROM public.basket_a')
        fruits_a = [fruit[0] for fruit in cursor.fetchall()]
        
        cursor.execute('SELECT fruit_b FROM public.basket_b')
        fruits_b = [fruit[0] for fruit in cursor.fetchall()]
        
        # Use set operations to find unique fruits
        unique_fruits_a = list(set(fruits_a) - set(fruits_b))  # Fruits in basket_a but not in basket_b
        unique_fruits_b = list(set(fruits_b) - set(fruits_a))  # Fruits in basket_b but not in basket_a
        
        connection.close()
        
        return jsonify({
            "status": "Success!",
            "unique_fruits_a": unique_fruits_a,
            "unique_fruits_b": unique_fruits_b
        }), 200
    except Exception as e:
        print(f"Error in unique_fruits: {str(e)}")
        return jsonify({"status": "Error", "error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)



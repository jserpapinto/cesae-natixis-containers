import logging
from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

app = Flask(__name__)
CORS(app)

# Obter as variáveis de ambiente
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
APP_PORT = os.getenv("APP_PORT", 5000)

@app.route('/health', methods=['GET'])
def health_check():
    try:
        # Verificar se todas as variáveis de ambiente necessárias estão definidas
        if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
            logging.error("Missing required environment variables")
            return jsonify({
                "status": "error",
                "message": "Missing required environment variables"
            }), 500

        logging.info(f"Attempting to connect to database at {DB_HOST}")
        # Tentar conectar à base de dados
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS health_checks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            check_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status VARCHAR(50)
        )
        """
        cursor.execute(create_table_query)

        # Insert new health check record
        insert_query = "INSERT INTO health_checks (status) VALUES ('success')"
        cursor.execute(insert_query)
        connection.commit()

        # Count total requests
        count_query = "SELECT COUNT(*) FROM health_checks"
        cursor.execute(count_query)
        total_requests = cursor.fetchone()[0]

        cursor.close()
        connection.close()
        
        logging.info(f"Successfully connected to database. Total health checks: {total_requests}")
        return jsonify({
            "status": "success", 
            "message": "Connected to database",
            "total_health_checks": total_requests
        }), 200
    except mysql.connector.Error as err:
        # Retorna erro caso a conexão falhe
        logging.error(f"Database connection failed: {err}")
        return jsonify({"status": "error", "message": f"Database connection failed: {err}"}), 500

if __name__ == '__main__':
    logging.info(f"Starting Flask application on port {APP_PORT}")
    app.run(host='0.0.0.0', port=APP_PORT)
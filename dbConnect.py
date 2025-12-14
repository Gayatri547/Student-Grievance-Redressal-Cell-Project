import psycopg2
class DBConnect:
  def getDbConnection():
    # Establishing a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="studentgrievance",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    return conn

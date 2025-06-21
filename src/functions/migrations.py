import sqlite3
from datetime import datetime

DB_NAME = "database.db"


# Users jadvalini yaratish
create_users_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        telegram_id INTEGER UNIQUE NOT NULL,
        full_name VARCHAR(100) NOT NULL,
        username VARCHAR(100) UNIQUE,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100)
    );
"""
# Users jadvalini o'chirish
drop_users_table_query = "DROP TABLE IF EXISTS users;"

def create_users_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # delete users table
    cursor.execute(drop_users_table_query)
    # create users table
    cursor.execute(create_users_table_query)
    conn.commit()
    conn.close()
    
    print(f"✅ {DB_NAME} users table created successfully!")
    
    
def main():
    create_users_table()
    
if __name__ == "__main__":
    main()
        
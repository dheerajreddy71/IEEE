import sqlite3

def create_tables():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
    ''')

    # Create events table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        date TEXT
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()

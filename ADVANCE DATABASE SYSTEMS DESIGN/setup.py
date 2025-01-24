import sqlite3

db_path = 'soccer.db'

def create_tables():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the 'teams' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create the 'players' table with a foreign key relationship
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            team_id INTEGER,
            FOREIGN KEY (team_id) REFERENCES teams(id)
        )
    ''')

    conn.commit()
    conn.close()

def insert_initial_data():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insert sample teams
    cursor.execute("INSERT INTO teams (name) VALUES ('Team A')")
    
    cursor.execute("INSERT INTO teams (name) VALUES ('Team B')")
    cursor.execute("INSERT INTO teams (name) VALUES ('Team C')")

    # Insert sample players with team_id
    cursor.execute("INSERT INTO players (name, position, team_id) VALUES ('Player 1', 'Forward', 1)")
    cursor.execute("INSERT INTO players (name, position, team_id) VALUES ('Player 2', 'Midfielder', 2)")
    cursor.execute("INSERT INTO players (name, position, team_id) VALUES ('Player 3', 'Defender', 3)")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    insert_initial_data()
    print('Database setup complete.')

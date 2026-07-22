import sqlite3
from pathlib import Path


DATABASE_PATH = Path("sample_tracker.db")


def create_connection(database_path=DATABASE_PATH) -> sqlite3.Connection:
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(database_path) #if the database file does not exist, it will be created automatically


def create_tables(database_path=DATABASE_PATH) -> None:
    """Create the required database tables."""
    connection = create_connection(database_path)

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        connection.commit()
    finally:
        connection.close()

#CRUD operations for the projects table
def insert_project(name: str, database_path=DATABASE_PATH) -> int:
    """Insert a project and return its database ID."""
    connection = create_connection(database_path)

    try:
        cursor = connection.execute(
            "INSERT INTO projects (name) VALUES (?)", #VALUES (?) is a placeholder for the project name
            (name,), #make sure to pass a tuple with a single element
        )
        connection.commit()

        return cursor.lastrowid #ID of last inserted row
    finally:
        connection.close()

def list_projects(database_path=DATABASE_PATH) -> list[tuple[int, str]]:
    """Return all saved projects ordered by ID."""
    connection = create_connection(database_path)

    try:
        cursor = connection.execute(
            "SELECT id, name FROM projects ORDER BY id"
        )
        return cursor.fetchall()
    finally:
        connection.close()
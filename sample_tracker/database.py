import sqlite3
from pathlib import Path


DATABASE_PATH = Path("sample_tracker.db")


def create_connection() -> sqlite3.Connection:
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_PATH)


def create_tables() -> None:
    """Create the required database tables."""
    connection = create_connection()

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
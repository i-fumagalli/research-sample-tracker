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

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS samples (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                project_id INTEGER NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
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

def project_exists(project_id: int, database_path=DATABASE_PATH) -> bool:
    """Check if a project with the given ID exists in the database."""
    connection = create_connection(database_path)

    try:
        cursor = connection.execute(
            "SELECT 1 FROM projects WHERE id = ?", (project_id,)
        )
        return cursor.fetchone() is not None #fetchone() returns None if no row is found, otherwise it returns a tuple representing the row
    finally:
        connection.close()

#sample table CRUD operations
def insert_sample(name: str, project_id: int, database_path=DATABASE_PATH) -> int:
    """Insert a sample and return its database ID."""
    connection = create_connection(database_path)

    try:
        cursor = connection.execute(
            "INSERT INTO samples (name, project_id) VALUES (?, ?)",
            (name, project_id), #tuple containing the sample name and project ID
        )
        connection.commit()

        return cursor.lastrowid
    finally:
        connection.close()

def list_samples(database_path=DATABASE_PATH) -> list[tuple[int, str, int]]:
    """Return all samples ordered by ID."""
    connection = create_connection(database_path)

    try:
        cursor = connection.execute(
            "SELECT id, name, project_id FROM samples ORDER BY id"
        )
        return cursor.fetchall()
    finally:
        connection.close()

def list_samples_with_projects(database_path=DATABASE_PATH) -> list[tuple[int, str, int, str]]:
    """Return all samples along with their associated project names."""
    connection = create_connection(database_path)

    try:
        cursor = connection.execute(
            """
            SELECT samples.id, samples.name, samples.project_id, projects.name
            FROM samples
            JOIN projects ON samples.project_id = projects.id
            ORDER BY samples.id
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()
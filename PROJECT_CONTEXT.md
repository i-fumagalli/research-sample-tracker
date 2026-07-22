# Project Context

## Project

Research Sample Tracker

## Goal

Build a Python application that manages research projects and biological samples.

## Current technology

- Python
- SQLite
- pytest
- argparse
- Git and GitHub

## Current structure

- `sample_tracker/main.py`
- `sample_tracker/database.py`
- `tests/test_main.py`

## Current functionality

- Validate project names
- Create the SQLite projects table
- Insert projects into SQLite
- Return the generated project ID
- List all saved projects ordered by ID
- Use a command-line `add` command to create projects
- Run automated tests with pytest
- Use temporary SQLite databases for database tests
- Use a command-line `list` command to display projects without creating a new project
- Test listing multiple projects with a temporary SQLite database

## Current usage

Add a project:

```bash
python -m sample_tracker.main add "Microbiome Study"
```

The command validates the project name, saves it in SQLite, and lists all saved projects.

List all saved projects without creating a new project:

```bash
python -m sample_tracker.main list
```

## Current database schema

```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

## Running tests

Tests must be run from the project root with:

```bash
python -m pytest
```
There are currently 5 automated tests.

Database tests use a temporary SQLite database and do not modify `sample_tracker.db`.
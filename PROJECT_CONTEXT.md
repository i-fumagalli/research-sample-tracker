# Project Context

## Project

Research Sample Tracker

## Goal

Build a Python application that manages research projects and biological samples.

## Current technology

- Python
- SQLite
- pytest
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
- Run automated tests with pytest

## Current output

Running:

```bash
python -m sample_tracker.main
```

creates a project called `Microbiome Study`, saves it in SQLite, and lists all saved projects.

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
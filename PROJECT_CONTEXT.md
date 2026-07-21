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
- Create the projects table
- Insert projects into SQLite
- Return the generated project ID
- Run three automated tests

## Current database schema

```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
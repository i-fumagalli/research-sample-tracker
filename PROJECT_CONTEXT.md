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
- Store biological samples in SQLite
- Link each biological sample to a research project using `project_id`
- Insert biological samples into SQLite
- List saved biological samples from the database
- Use a command-line `add-sample` command to create biological samples
- Test sample insertion and sample listing with a temporary SQLite database
- Store biological samples in SQLite
- Link samples to projects using `project_id`
- Add biological samples with the `add-sample` command
- List biological samples with the `list-samples` command
- Validate sample names
- Reject samples linked to non-existing projects
- Test project existence, sample insertion, sample listing, and sample validation
- Display project names together with biological samples
- Show user-friendly error messages instead of Python tracebacks
- Delete biological samples from SQLite
- Use a command-line `delete-sample` command
- Return `True` or `False` depending on whether a sample was deleted
- Test sample deletion with a temporary SQLite database

## Current usage

Add a project:

```bash
python -m sample_tracker.main add "Microbiome Study"
```

List all saved projects:

```bash
python -m sample_tracker.main list
```

Add a biological sample to poject ID 1:

```bash
python -m sample_tracker.main add-sample "Sample 1" 1
```

Add a biological sample:

```bash
python -m sample_tracker.main add-sample "Sample 2" 3
```

List all biological samples:

```bash
python -m sample_tracker.main list_samples
```

Delete a biological sample:

```bash
python -m sample_tracker.main delete-sample 3
```


## Current database schema

```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE samples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    project_id INTEGER NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);

CREATE TABLE samples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    project_id INTEGER NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);
```

## Running tests

Tests must be run from the project root with:

```bash
python -m pytest
```
There are currently 18 automated tests.

Database tests use a temporary SQLite database and do not modify `sample_tracker.db`.

## Current task

Complete CRUD support for projects and biological samples.

Current CRUD status:

- Projects:
  - Create: complete
  - Read: complete
  - Update: not implemented
  - Delete: not implemented

- Samples:
  - Create: complete
  - Read: complete
  - Update: not implemented
  - Delete: complete
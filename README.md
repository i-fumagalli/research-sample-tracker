# Research Sample Tracker

A small Python command-line project for managing research projects and biological samples.

I built this project to practise Python, SQLite, command-line programs and automated testing.

## Features

- Add, list, update, and delete research projects
- Add, list, update, and delete biological samples
- Connect samples to a research project
- Prevent deleting a project if samples still belong to it
- Validate project and sample names
- Save data in a SQLite database
- Test the application with pytest

## Technologies

- Python
- SQLite
- argparse
- pytest
- Git

## Project structure

```
research-sample-tracker/
├── sample_tracker/
│   ├── __init__.py
│   ├── database.py
│   └── main.py
├── tests/
│   ├── test_database.py
│   └── test_main.py
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/i-fumagalli/research-sample-tracker.git
cd research-sample-tracker
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install pytest:

```bash
python -m pip install pytest
```

## Usage

Run the commands from the project folder.

### Add a project

```bash
python -m sample_tracker.main add "Microbiome Study"
```

Arguments:

```text
name 
```
- `name`: Name of the new project

### List projects

```bash
python -m sample_tracker.main list
```

### Update a project

```bash
python -m sample_tracker.main update-project 1 "Updated Project"
```

Arguments:

```text
project_id new_name
```
- `project_id`: ID of the project to update
- `new_name`: New name of the project

### Delete a project

```bash
python -m sample_tracker.main delete-project 1
```

Arguments:

```text
project_id
```
- `project_id`: ID of the project to delete

A project can't be deleted while samples are still connected to it.

### Add a sample

```bash
python -m sample_tracker.main add-sample "Sample 1" 1
```
Arguments:

```text
name project_id
```

- `name`: Name of the biological sample
- `project_id`: ID of the project the sample belongs to

### List samples

```bash
python -m sample_tracker.main list-samples
```

### Update a sample

```bash
python -m sample_tracker.main update-sample 1 "Updated Sample" 1
```

Arguments:

```text
sample_id new_name project_id
```
- `sample_id`: ID of the sample to update
- `new_name`: New name of the sample
- `project_id`: ID of the project the sample should belong to


### Delete a sample

```bash
python -m sample_tracker.main delete-sample 1
```

Arguments:

```text
sample_id
```
- `sample_id`: ID of the sample to delete

## Tests

Run all tests with:

```bash
python -m pytest
```

The tests cover the main database functions, validation, and CLI commands.

## Database

The application uses two tables:

```text
projects
- id
- name

samples
- id
- name
- project_id
```

Each sample belongs to one project.

## Next steps

Things I may add later:
- FastAPI
- Docker
- GitHub Actions
- More validation

## License

See the LICENSE file.
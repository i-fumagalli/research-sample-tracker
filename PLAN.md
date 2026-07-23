# Project Plan

## Goal

Build a Python application for managing research projects and biological samples.

## Completed

- Created GitHub repository
- Set up Python virtual environment
- Added project name validation
- Added automated tests with pytest
- Added SQLite database setup
- Added project insertion into SQLite
- Added listing of saved projects
- Replaced the hard-coded project name with user input
- Added command-line argument parsing with argparse
- Added an `add` command for creating research projects
- Added isolated database tests using a temporary SQLite database
- Added a `list` command to display saved projects without creating a new project
- Added a database test for listing multiple projects
- Added a `samples` table linked to research projects
- Added sample insertion into SQLite
- Added listing of saved samples
- Added database tests for inserting and listing samples
- Added an `add-sample` command for creating biological samples
- Added a `samples` table linked to research projects
- Added sample insertion and sample listing
- Added `add-sample` and `list-samples` commands
- Added sample name validation
- Added project existence checks before creating samples
- Added tests for sample creation, listing, validation, and project checks
- Added project names to the `list-samples` output
- Added user-friendly error messages
- Added sample deletion in SQLite
- Added a `delete-sample` command
- Added tests for deleting samples
- Added full CRUD support for research projects
- Added full CRUD support for biological samples
- Added `update-project` and `delete-project` commands
- Added `update-sample` and `delete-sample` commands
- Prevented deletion of projects that still have associated samples
- Added tests for project and sample update and delete operations

## Current task

- Add CLI tests for project and sample commands

## Next tasks

- Improve empty-list messages
- Finalize README and project documentation
- Prepare the codebase for FastAPI

## Later

- FastAPI
- Docker
- GitHub Actions
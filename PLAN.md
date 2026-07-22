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

## Current task

- Add sample update functionality

## Next tasks

- Add a command to update biological samples
- Add project deletion
- Add project update functionality
- Add commands to delete and update projects
- Add tests for all update and delete operations

## Later

- FastAPI
- Docker
- GitHub Actions
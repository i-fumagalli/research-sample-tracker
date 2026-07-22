from pathlib import Path

from sample_tracker.database import (
    create_tables, 
    insert_project, 
    list_projects,
    insert_sample,
    list_samples,
    project_exists,
    list_samples_with_projects,
    delete_sample,
    )

def test_insert_and_list_project(tmp_path: Path) -> None:
    #tmp_path is a temporary directory provided by pytest for testing purposes
    database_path = tmp_path / "test.db" #create a temporary database file in the temporary directory
    create_tables(database_path) # Create the projects table in the temporary test database.

    project_id = insert_project("Test Project", database_path)
    projects = list_projects(database_path)

    assert project_id is not None
    assert (project_id, "Test Project") in projects

def test_list_multiple_projects(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    first_project_id = insert_project("Microbiome Study", database_path)
    second_project_id = insert_project("Genomics Research", database_path)

    projects = list_projects(database_path)

    assert projects == [(first_project_id, "Microbiome Study"), 
                        (second_project_id, "Genomics Research"),]

def test_insert_sample(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    project_id = insert_project("Microbiome Study", database_path)

    sample_id = insert_sample("Sample 1", project_id, database_path)

    assert sample_id is not None

def test_insert_and_list_sample(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    project_id = insert_project("Microbiome Study", database_path)

    sample_id = insert_sample("Sample 1", project_id, database_path)

    samples = list_samples(database_path)

    assert samples == [(sample_id, "Sample 1", project_id)]

def test_project_exists(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    project_id = insert_project("Microbiome Study", database_path)

    assert project_exists(project_id, database_path) is True

def test_project_does_not_exist(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    assert project_exists(999, database_path) is False


def test_list_projects_returns_empty_list(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    projects = list_projects(database_path)

    assert projects == []

def test_list_multiple_samples(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    project_id = insert_project("Microbiome Study", database_path)

    first_sample_id = insert_sample("Sample 1", project_id, database_path)
    second_sample_id = insert_sample("Sample 2", project_id, database_path)

    samples = list_samples(database_path)

    assert samples == [(first_sample_id, "Sample 1", project_id), 
                       (second_sample_id, "Sample 2", project_id)]

def test_list_samples_with_project_names(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    project_id = insert_project("Microbiome Study", database_path)

    sample_id = insert_sample("Sample 1", project_id, database_path)

    samples_with_projects = list_samples_with_projects(database_path)

    assert samples_with_projects == [(sample_id, "Sample 1", project_id, "Microbiome Study")]

def test_delete_sample(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"
    create_tables(database_path)

    project_id = insert_project("Microbiome Study", database_path)

    sample_id = insert_sample("Sample 1", project_id, database_path)

    deleted = delete_sample(sample_id, database_path)
    samples = list_samples(database_path)

    assert deleted is True
    assert samples == []
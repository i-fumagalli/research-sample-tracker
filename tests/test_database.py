from sample_tracker.database import (create_tables, insert_project, list_projects,)

def test_insert_and_list_project() -> None:
    create_tables()

    project_id = insert_project("Test Project")
    projects = list_projects()

    assert project_id is not None
    assert (project_id, "Test Project") in projects
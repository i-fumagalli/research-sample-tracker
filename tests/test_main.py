from pathlib import Path

import pytest

from sample_tracker.main import create_project, create_sample, main


def test_create_project_with_valid_name() -> None:
    project = create_project("Microbiome Study")

    assert project == {"name": "Microbiome Study"}


def test_create_project_removes_surrounding_spaces() -> None:
    project = create_project("  Microbiome Study  ")

    assert project == {"name": "Microbiome Study"}


def test_create_project_rejects_empty_name() -> None: #match checks also the error message
    with pytest.raises(ValueError, match="Project name must not be empty."):
        create_project("   ")

def test_create_sample_with_valid_data() -> None:
    sample = create_sample("Sample 1", 1)

    assert sample == {"name": "Sample 1", "project_id": 1}

def test_create_sample_removes_surrounding_spaces() -> None:
    sample = create_sample("  Sample 1  ", 1)

    assert sample == {"name": "Sample 1", "project_id": 1}

def test_create_sample_rejects_empty_name() -> None:
    with pytest.raises(ValueError, match="Sample name must not be empty."):
        create_sample("   ", 1)


def test_create_project_keeps_spaces_inside_name() -> None:
    project = create_project("Microbiome Study   2024")

    assert project == {"name": "Microbiome Study   2024"}


def test_create_sample_keeps_project_id() -> None:
    sample = create_sample("Sample 1", 42)

    assert sample == {"name": "Sample 1", "project_id": 42}


def test_cli_add_project(tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
    database_path = tmp_path / "test.db"

    main(["add", "Microbiome Study"], database_path)

    output = capsys.readouterr().out #capture the output of the command

    assert "Created project 1: Microbiome Study" in output
    assert "1: Microbiome Study" in output

def test_cli_list_projects(tmp_path: Path, capsys) -> None:
    database_path = tmp_path / "test.db"

    main(["add", "Microbiome Study"], database_path)

    capsys.readouterr() #clear the output buffer to avoid capturing the output of the add command

    main(["list"], database_path)

    output = capsys.readouterr().out

    assert "Saved projects:" in output
    assert "1: Microbiome Study" in output


def test_cli_add_sample(tmp_path: Path, capsys) -> None:
    database_path = tmp_path / "test.db"

    main(["add", "Microbiome Study"], database_path)
    capsys.readouterr()

    main(["add-sample", "Sample 1", "1"], database_path)

    output = capsys.readouterr().out

    assert "Created sample 1: Sample 1 for project ID 1" in output


def test_cli_list_samples(tmp_path: Path, capsys) -> None:
    database_path = tmp_path / "test.db"

    main(["add", "Microbiome Study"], database_path)
    capsys.readouterr()

    main(["add-sample", "Sample 1", "1"], database_path)
    capsys.readouterr()

    main(["list-samples"], database_path)

    output = capsys.readouterr().out

    assert "Saved samples:" in output
    assert "1: Sample 1" in output
    assert "Project: Microbiome Study, ID: 1" in output


def test_cli_update_project(tmp_path: Path, capsys) -> None:
    database_path = tmp_path / "test.db"

    main(["add", "Microbiome Study"], database_path)
    capsys.readouterr()

    main(["update-project", "1", "Updated Study"], database_path)

    output = capsys.readouterr().out

    assert "Updated project 1: Updated Study" in output


def test_cli_delete_project(tmp_path: Path, capsys) -> None:
    database_path = tmp_path / "test.db"

    main(["add", "Microbiome Study"], database_path)
    capsys.readouterr()

    main(["delete-project", "1"], database_path)

    output = capsys.readouterr().out

    assert "Deleted project with ID 1" in output


def test_cli_update_sample(tmp_path: Path, capsys) -> None:
    database_path = tmp_path / "test.db"

    main(["add", "Microbiome Study"], database_path)
    capsys.readouterr()

    main(["add-sample", "Sample 1", "1"], database_path)
    capsys.readouterr()

    main(["update-sample", "1", "Updated Sample", "1"], database_path)

    output = capsys.readouterr().out

    assert "Updated sample 1: Updated Sample for project ID 1" in output


def test_cli_delete_sample(tmp_path: Path, capsys) -> None:
    database_path = tmp_path / "test.db"

    main(["add", "Microbiome Study"], database_path)
    capsys.readouterr()

    main(["add-sample", "Sample 1", "1"], database_path)
    capsys.readouterr()

    main(["delete-sample", "1"], database_path)

    output = capsys.readouterr().out

    assert "Deleted sample with ID 1" in output

def test_cli_add_sample_rejects_missing_project(tmp_path: Path) -> None:
    database_path = tmp_path / "test.db"

    with pytest.raises(
        ValueError,
        match="Project with ID 999 does not exist.",
    ):
        main(["add-sample", "Sample 1", "999"], database_path)
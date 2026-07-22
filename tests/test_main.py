import pytest

from sample_tracker.main import create_project, create_sample


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
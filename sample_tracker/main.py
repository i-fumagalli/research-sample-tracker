from sample_tracker.database import create_tables, insert_project

def create_project(name: str) -> dict[str, str]:
    """Create a research project representation."""
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Project name must not be empty.")

    return {"name": cleaned_name}


def main() -> None:
    create_tables()

    project = create_project("Microbiome Study")
    project_id = insert_project(project["name"])

    print(f"Created project {project_id}: {project['name']}")

if __name__ == "__main__":
    main()
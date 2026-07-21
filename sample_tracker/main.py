from sample_tracker.database import (create_tables, insert_project, list_projects,)

def create_project(name: str) -> dict[str, str]:
    """Create a research project representation."""
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Project name must not be empty.")

    return {"name": cleaned_name}


def main() -> None:
    create_tables()

    project_name = input("Project name: ")
    project = create_project(project_name)
    
    project_id = insert_project(project["name"])

    print(f"Created project {project_id}: {project['name']}")

    projects = list_projects()

    print("Saved projects:")

    for saved_project_id, saved_project_name in projects:
        print(f"{saved_project_id}: {saved_project_name}")

if __name__ == "__main__":
    main()
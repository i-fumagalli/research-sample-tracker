import argparse #this module is used to parse command-line arguments

from sample_tracker.database import (create_tables, 
                                     insert_project, 
                                     list_projects,
                                     insert_sample,
                                     list_samples
                                     )

def create_project(name: str) -> dict[str, str]:
    """Create a research project representation."""
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Project name must not be empty.")

    return {"name": cleaned_name}

def create_sample(name: str, project_id: int) -> dict[str, str | int]: #str | int e.g. {"name": "Sample 1", "project_id": 1}
    """Create a biological sample representation."""
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Sample name must not be empty.")

    return {"name": cleaned_name, "project_id": project_id}


def main() -> None:
    create_tables()

    parser = argparse.ArgumentParser(description="Research Sample Tracker") #ArgumentParser is used to create a command-line interface (CLI) for the application

    subparsers = parser.add_subparsers(dest="command") #subparsers allow us to define different commands for the CLI

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new research project") #add command is used to add a new research project

    add_parser.add_argument("name", type=str, help="Name of the research project") #name argument is used to specify the name of the research project

    # List command
    subparsers.add_parser("list", help="List all research projects") #list command is used to list all saved research projects

    # Add sample command
    add_sample_parser = subparsers.add_parser("add-sample", help="Add a new biological sample")

    add_sample_parser.add_argument("name", type=str, help="Name of the biological sample") #name argument is used to specify the name of the biological sample

    add_sample_parser.add_argument("project_id", type=int, help="ID of the associated research project") #project_id argument is used to specify the ID of the associated research project

    #list samples command
    subparsers.add_parser("list-samples", help="List all biological samples")


    args = parser.parse_args() #parse the command-line arguments

    # Handle add command
    if args.command == "add":
        project = create_project(args.name)

        project_id = insert_project(project["name"])

        print(f"Created project {project_id}: {project['name']}")

        projects = list_projects()

        print("Saved projects:")

        for saved_project_id, saved_project_name in projects:
            print(f"{saved_project_id}: {saved_project_name}")

    # Handle list command
    elif args.command == "list":
        projects = list_projects()

        print("Saved projects:")
        for saved_project_id, saved_project_name in projects:
            print(f"{saved_project_id}: {saved_project_name}")

    # Handle add-sample command
    elif args.command == "add-sample":
        sample = create_sample(args.name, args.project_id)
        
        sample_id = insert_sample(sample["name"], sample["project_id"])

        print(f"Created sample {sample_id}: {sample['name']} for project ID {sample['project_id']}")

    # Handle list-samples command
    elif args.command == "list-samples":
        samples = list_samples()

        print("Saved samples:")
        for saved_sample_id, saved_sample_name, saved_project_id in samples:
            print(f"{saved_sample_id}: {saved_sample_name} (Project ID: {saved_project_id})")
    


if __name__ == "__main__":
    main()
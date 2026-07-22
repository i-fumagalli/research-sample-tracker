import argparse #this module is used to parse command-line arguments

from sample_tracker.database import (create_tables, 
                                     insert_project, 
                                     list_projects,
                                     insert_sample,
                                     list_samples,
                                    project_exists,
                                    list_samples_with_projects,
                                    delete_sample,
                                    update_sample,
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

    #delete sample command
    delete_sample_parser = subparsers.add_parser("delete-sample", help="Delete a biological sample")

    delete_sample_parser.add_argument("sample_id", type=int, help="ID of the biological sample to delete") #sample_id argument is used to specify the ID of the biological sample to delete

    #update sample command
    update_sample_parser = subparsers.add_parser("update-sample", help="Update a biological sample")

    update_sample_parser.add_argument("sample_id", type=int, help="ID of the biological sample to update") #sample_id argument is used to specify the ID of the biological sample to update

    update_sample_parser.add_argument("name", type=str, help="New name for the biological sample") #name argument is used to specify the new name for the biological sample

    update_sample_parser.add_argument("project_id", type=int, help="New project ID for the biological sample") #project_id argument is used to specify the new project ID for the biological sample

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
        if not project_exists(args.project_id):
            raise ValueError(f"Project with ID {args.project_id} does not exist.")
        
        sample = create_sample(args.name, args.project_id)

        sample_id = insert_sample(sample["name"], sample["project_id"])

        print(f"Created sample {sample_id}: {sample['name']} for project ID {sample['project_id']}")

    # Handle list-samples command
    elif args.command == "list-samples":
        samples = list_samples_with_projects()

        print("Saved samples:")
        for (saved_sample_id, saved_sample_name, saved_project_id, saved_project_name) in samples:
            print(f"{saved_sample_id}: {saved_sample_name} "f"(Project: {saved_project_name}, ID: {saved_project_id})")

    # Handle delete-sample command
    elif args.command == "delete-sample":
        deleted = delete_sample(args.sample_id)

        if not deleted:
            raise ValueError(f"Sample with ID {args.sample_id} does not exist.")

        print(f"Deleted sample with ID {args.sample_id}")

    # Handle update-sample command
    elif args.command == "update-sample":
        if not project_exists(args.project_id):
            raise ValueError(f"Project with ID {args.project_id} does not exist.")

        sample = create_sample(args.name, args.project_id)

        updated = update_sample(args.sample_id, sample["name"], sample["project_id"])

        if not updated:
            raise ValueError(f"Sample with ID {args.sample_id} does not exist.")

        print(f"Updated sample {args.sample_id}: {sample['name']} for project ID {sample['project_id']}")

    else:
        parser.print_help() #print the help message if no command is provided
    

if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Error: {error}")
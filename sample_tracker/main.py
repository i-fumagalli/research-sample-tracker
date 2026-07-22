import argparse #this module is used to parse command-line arguments

from sample_tracker.database import (create_tables, insert_project, list_projects,)

def create_project(name: str) -> dict[str, str]:
    """Create a research project representation."""
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Project name must not be empty.")

    return {"name": cleaned_name}


def main() -> None:
    create_tables()

    parser = argparse.ArgumentParser(description="Research Sample Tracker") #ArgumentParser is used to create a command-line interface (CLI) for the application
    subparsers = parser.add_subparsers(dest="command") #subparsers allow us to define different commands for the CLI

    # Define add_project command
    add_parser = subparsers.add_parser("add", help="Add a new research project") #add command is used to add a new research project

    add_parser.add_argument("name", type=str, help="Name of the research project") #name argument is used to specify the name of the research project

    args = parser.parse_args() #parse the command-line arguments

    #args.command == "add"
    #args.name == "Microbiome Study"

    ###
    if args.command == "add":
        project = create_project(args.name)

        project_id = insert_project(project["name"])

        print(f"Created project {project_id}: {project['name']}")

        projects = list_projects()

        print("Saved projects:")

        for saved_project_id, saved_project_name in projects:
            print(f"{saved_project_id}: {saved_project_name}")


if __name__ == "__main__":
    main()
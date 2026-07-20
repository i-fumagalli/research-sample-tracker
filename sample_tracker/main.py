def create_project(name: str) -> dict[str, str]:
    """Create a research project representation."""
    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValueError("Project name must not be empty.")

    return {"name": cleaned_name}


def main() -> None:
    project = create_project("Microbiome Study")
    print(f"Created project: {project['name']}")


if __name__ == "__main__":
    main()
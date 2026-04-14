import os
from datetime import datetime


def create_project_structure():
    folders = [
        "sample_input",
        "output/generated_docs",
        "templates",
        "docs"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def generate_sample_hld():
    content = f"""
# High Level Design (HLD)

## Project Name
Automated Regulatory Compliance Document Generation

## Generated On
{datetime.now()}

## Modules
- Input Parser
- Compliance Rule Engine
- Document Generator
- API Layer
- Audit Logger

## Workflow
Input → Parse → Validate → Generate HLD/PLD/API docs → Save Output
"""

    with open("output/generated_docs/HLD.md", "w", encoding="utf-8") as f:
        f.write(content)


def main():
    create_project_structure()
    generate_sample_hld()
    print("Project setup completed successfully.")
    print("Sample HLD generated successfully.")


if __name__ == "__main__":
    main()

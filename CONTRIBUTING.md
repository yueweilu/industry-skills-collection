# Contributing to AI Agent Skills Collection

> [中文](CONTRIBUTING_zh-CN.md)

We are excited that you want to contribute! This project relies on community submissions to build a diverse library of tools for AI agents.

## 🛠 How to Add a New Skill

To add a new skill, please follow these steps:

1.  **Create a Directory**:
    Inside the `skills/` folder, create a new directory with a kebab-case name (e.g., `pdf-reader`, `currency-converter`).

2.  **Add Your Script**:
    Write a Python (or Node.js) script that performs the task.
    *   **Requirement**: The script should output **JSON** to stdout.
    *   **Requirement**: Handle errors gracefully (return a JSON object with an `error` key).
    *   **Dependency**: If you use external libraries, please list them in the PR description.

3.  **Create Documentation**:
    Create a `SKILL.md` file in your directory. Copy the format from existing skills:
    *   **Frontmatter**: `name` and `description`.
    *   **Tools**: Path to the script and usage instructions.
    *   **IO**: Example input and output.
    *   **Acknowledgments**: Credit original authors if applicable.

4.  **(Optional) Chinese Documentation**:
    If you can, create a `SKILL_zh-CN.md` file.

5.  **Submit a Pull Request**:
    Push your changes and open a PR. We will review it shortly!

## 🧪 Testing

Before submitting, please test your skill using the CLI:

```bash
python main.py
```

Ensure your skill appears in the list and executes correctly.

## 📄 License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

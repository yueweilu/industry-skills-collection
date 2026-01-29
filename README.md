# AI Agent Skills Collection 🤖

> A curated collection of modular skills (tools) designed for AI agents.

This repository hosts a set of standardized skills that AI agents (like Large Language Models) can utilize to interact with the real world—fetching data, controlling software, or processing files.

Each skill is self-contained with its own documentation and executable scripts.

## 📂 Available Skills

| Skill Name | Description |
| :--- | :--- |
| [**weather-lookup**](skills/weather-lookup/SKILL.md) | Retrieve current weather conditions for a specific city. |

## 🚀 How to Use

Each skill is located in the `skills/` directory and contains a `SKILL.md` file. This file describes:
1.  **Purpose**: When the AI should use this skill.
2.  **Tools**: The specific scripts (Python/Node.js) to execute.
3.  **IO**: Expected input arguments and output JSON format.

## 🤝 Contributing

We welcome contributions! If you have built a useful tool for AI agents, please submit a PR.

1.  Create a new folder in `skills/`.
2.  Add your script (e.g., `tool.py`).
3.  Add a `SKILL.md` following the standard format.
4.  Add an `Acknowledgments` section in your `SKILL.md` if adapted from another project.

## 📄 License

MIT License

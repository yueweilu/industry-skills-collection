# AI Agent 技能合集 (AI Agent Skills Collection) 🤖

> [English](README.md)

> 一个为 AI Agent 精心策划的模块化技能（工具）合集。

本仓库托管了一组标准化的技能，AI Agent（如大型语言模型）可以利用这些技能与现实世界互动——获取数据、控制软件或处理文件。

每个技能都是独立的，拥有自己的文档和可执行脚本。

## 📂 可用技能 (Available Skills)

| 技能名称 | 描述 |
| :--- | :--- |
| [**weather-lookup**](skills/weather-lookup/SKILL_zh-CN.md) | 查询特定城市的实时天气状况。 |
| [**stock-price**](skills/stock-price/SKILL_zh-CN.md) | 获取实时股票价格和市场数据。 |
| [**web-search-duckduckgo**](skills/web-search-duckduckgo/SKILL_zh-CN.md) | 执行匿名网络搜索以查找信息。 |
| [**system-info**](skills/system-info/SKILL_zh-CN.md) | 检查主机的 CPU、内存和磁盘使用情况。 |

## 🚀 如何使用

每个技能都位于 `skills/` 目录下，并包含一个 `SKILL.md` (或 `SKILL_zh-CN.md`) 文件。该文件描述了：
1.  **目的**: AI 何时应该使用此技能。
2.  **工具**: 要执行的具体脚本 (Python/Node.js)。
3.  **IO**: 预期的输入参数和输出 JSON 格式。

### 交互式 CLI

我们提供了一个简单的命令行界面来测试这些技能：

```bash
python main.py
```

## 📦 安装依赖

你可以一次性安装所有技能所需的依赖：

```bash
pip install -r requirements.txt
```

## 🤝 参与贡献

我们欢迎贡献！如果您为 AI Agent 构建了有用的工具，请提交 PR。

请参阅 [贡献指南](CONTRIBUTING_zh-CN.md) 了解详细步骤。

1.  在 `skills/` 中创建一个新文件夹。
2.  添加您的脚本（例如 `tool.py`）。
3.  添加符合标准格式的 `SKILL.md`。
4.  如果是改编自其他项目，请在 `SKILL.md` 中添加 `Acknowledgments`（致谢）部分。

## 📄 许可证

MIT License

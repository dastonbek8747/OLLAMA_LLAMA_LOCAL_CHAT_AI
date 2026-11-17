# Ollama Local Coding Assistant

> A coding assistant that runs fully offline with Ollama and Llama 3.2 through LangChain. No API key and no internet needed after the model is pulled.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)


## Features

- Runs fully local, so code never leaves the machine.
- LangChain prompt pipeline on top of Ollama.
- Small, readable codebase.

## Tech Stack

| Layer | Technology |
|---|---|
| Local LLM runtime | Ollama (Llama 3.2) |
| Orchestration | LangChain |
| Packaging | uv (pyproject.toml) |

## Quick Start

```bash
# 1. install Ollama and pull the model
ollama pull llama3.2

# 2. run the assistant
git clone https://github.com/dastonbek8747/ollama-local-coding-assistant.git
cd ollama-local-coding-assistant
uv sync
uv run main.py
```

## Project Structure

```
main.py          # assistant entry point
pyproject.toml   # uv project definition
```

## Why Local Models

Cloud models are strong but cost money and send code off the machine. This project shows I can also build against a local runtime, which matters for privacy-sensitive work.

## License

MIT © 2026 Doston Sultonov.

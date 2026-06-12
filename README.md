# Travel Planner

A lightweight Python-based travel planning assistant that provides tools for searching flights and interacting with the Tavily tool. This repository contains a small backend and a simple frontend runner for experimenting and extending travel-related automation.

## Features

- Flight lookup helper (`tools/flight_tool.py`).
- Tavily integration helper (`tools/tavily_tool.py`).
- Simple CLI/runner (`main.py`) and an example frontend entrypoint (`frontend.py`).

## Requirements

- Python 3.10+ recommended
- See `requirements.txt` for exact dependencies

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash / WSL) use: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

- Run the main runner:

```bash
python main.py
```

- Run the frontend example (if it uses Streamlit or similar):

```bash
python frontend.py
```

Adjust these commands according to how you want to exercise the tools.

## Project Structure

- `main.py` — application entrypoint / demo runner
- `frontend.py` — example frontend script
- `tools/flight_tool.py` — flight-related helper functions
- `tools/tavily_tool.py` — Tavily integration helper
- `requirements.txt` / `pyproject.toml` — dependency metadata

## Development

- Add or modify helper functions in the `tools/` directory.
- When adding dependencies, update `requirements.txt` or `pyproject.toml` accordingly.

## Contributing

Contributions welcome. Open issues or PRs with a clear description of the change and a short test or example demonstrating the behavior.

## License

MIT License — see `LICENSE` if present, otherwise contact the repository owner.

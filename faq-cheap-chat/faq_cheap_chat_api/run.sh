# poetry add fastapi uvicorn sentence-transformers requests

# Install all dependencies specified in the `pyproject.toml` file.
# This includes packages required for running the application.
poetry install

# Run the FastAPI application using Uvicorn.
# 'main:app' refers to the `app` instance in the `main.py` file.
# --host 127.0.0.1 binds the application to localhost.
# --port 8000 makes the application available on port 8000.
poetry run uvicorn main:app --host 127.0.0.1 --port 8000

# Set Poetry to use the Python interpreter managed by pyenv.
# $(pyenv which python) dynamically retrieves the path to the currently active Python interpreter.
poetry env use $(pyenv which python)

# List all the virtual environments created by Poetry for the current project.
# This helps confirm the environment was set up correctly.
# poetry env list

# Activate the virtual environment created by Poetry.
# This switches to the environment where dependencies will be installed.
poetry shell
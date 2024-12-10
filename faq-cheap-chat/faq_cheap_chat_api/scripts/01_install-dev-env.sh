# #########################
# Install dev environment
# #########################

# Install Poetry, a dependency management and packaging tool for Python.
brew install poetry

# Install pyenv, a version management tool for Python.
brew install pyenv

# Uncomment the following lines if you need to configure pyenv for Zsh shell:
# Add pyenv to the shell startup file to initialize it properly.
# This ensures pyenv runs when you open a new terminal.
# echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
# echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Install Python version 3.10.0 using pyenv.
# This downloads and builds the specified Python version.
pyenv install 3.10.0

# Set the Python version locally to 3.10.0 for the current directory/project.
# This creates a `.python-version` file, locking the project to Python 3.10.0.
pyenv local 3.10.0
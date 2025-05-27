# playwright-python
playwright-python is a python based automation framework.

## Requirements to run make shell command
```shell
brew install make
```

## Setting up your environment from scratch and running the tests
```shell
make
```

## Initialize a new project
```shell
pdm init
```
### Adding dependencies
```shell
pdm add requests  # Example dependency
pdm add BeautifulSoup # Example dependency
```

### Installing Playwright
```shell
pdm add pytest-playwright
pdm run python -m playwright install
```

### Running Tests
```shell
pdm run pytest
```
# Setting up a Repository Similar to this one
These steps are not necessary for this repo, but are provided in case you want to create a repository and need the steps to initialize the settings with the package manager.
## Perform the Init Step
For this, you will run the pdm command and answer the prompts which will result in the init of the environment for this project directory:
```shell
pdm init
```

## Add the dependencies
Add the dependencies needed for the application:
```shell
pdm add langchain openai playwright langgraph
```
Add dev/test dependencies:
```shell
pdm add --dev pytest ruff
pdm add --dev black mypy
pdm add typer rich
```
Verify with:
```shell
pdm list
```

Run a script
```shell
pdm run calgentik.py
```

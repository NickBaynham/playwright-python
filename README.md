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

### Running a Script
```shell
pdm run python simple-webcrawler.py
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



.PHONY: all init install_browsers test clean

# The default target runs all steps: environment setup, browser install, and test suite.
all: init install_browsers test

# Step 1: Initialize the environment (install dependencies)
init:
	pdm install
	pdm list

# Step 2: Install Playwright browser binaries
install_browsers:
	pdm run python -m playwright install

# Step 3: Run the test suite
test:
	pdm run pytest

# Optional: Clean command to remove any temporary files or caches if needed
clean:
	rm -rf __pycache__

# GitHub Repository Validation Script

This Python script uses Playwright to automate the validation of certain details on a GitHub repository page. The script performs the following tasks:
1. Opens the GitHub homepage.
2. Validates the user is logged out.
3. Searches for the repository `org:microsoft typescript`.
4. Navigates to the `TypeScript-Handbook` repository page.
5. Validates that the repository page shows the "is now read-only" message.
6. Validates that there are 38 branches.
7. Validates that there are more than 150 watchers.
8. Validates that there is at least one contributor coming from Huddersfield.
9. Exits with exit code 0 if all validations pass or with a non-zero exit code if any validation fails.

## Requirements

To run this project, you will need:

1. Python 3.7+
2. Playwright
3. pytest (optional, for running tests)
4. A code editor like Visual Studio Code

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ShaniSapir/GithubAssig.git
    cd GithubAssig
    ```


2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install playwright
    playwright install
    ```

4. **Save the script** in a file named `github_test.py`.

## Usage

1. **Run the script**:
    ```sh
    python github_test.py
    ```

2. **Check the exit code**:
    After the script execution, you can check the exit code in the terminal and this is what you should see when running the script: 
    INFO: Open Github home-page

    INFO: Validate the user is logged out
    INFO: Search the repo: 'org:microsoft typescript'
    INFO: Navigate to 'TypeScript-Handbook' page
    INFO: Validate the repo page shows the 'is now read-only' message
    INFO: Validate that there are 38 branches
    INFO: Validate that there are more than 150 watchers
    INFO: Validate that there is at least one contributor coming from Huddersfield
    INFO: All validations passed


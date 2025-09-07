# together

Automated testing of web applications using **Python, Selenium, Pytest**.

Features
- UI tests to check basic user scenarios
- Page Object Model for easy test support
- Test parameterization (Pytest)
- Report generation 
- GitHub Actions for CI/CD

Project structure
project/
│
├── .github/ # Settings GitHub Actions (CI/CD)
│ └── workflows/
│ └── run_tests.yml # Script for running tests in CI
│
├── pages/ # Page Object Model 
│ ├── base_page.py # Base class with helper methods
│ └── homepage.py # Homepage Locators and Methods
│
├── tests/ # UI tests (Pytest)
│ ├── conftest.py # Fixtures Pytest (setup/teardown)
│ ├── test_dropdown.py # Tests for dropdown lists
│ └── test_home_page.py # Home Page Tests
│
├── venv/ # Virtual environment Python
│
├── requirements.txt # Project dependencies
├── .gitignore # Ignored files Git
└── README.md # Project documentation

Installation and launch
1.  ```bash
git clone https:https://github.com/andriisultanovskyi/together
cd project
2. ```bash
Install dependencies
pip install -r requirements.txt
3. ```bash
Run tests
pytest -v

Technologies used
selenium==4.0.0
pytest==8.4.1
GitHub Actions (CI/CD)

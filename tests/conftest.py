import pytest
from tests.fixtures.driver import driver
from tests.fixtures.db_fixtures import db_connection
from tests.fixtures.test_data_fixtures import room_templates_list


def pytest_addoption(parser):
    """
    Adds command-line option --browser for cross-browser testing.
    Example: pytest tests/ --browser=firefox
    """
    parser.addoption(
        # Name of the option that can be passed on the command line
        "--browser",
        # The value will be saved (stored in parser)
        action="store",
        # Default value if the option is not passed in
        default="chrome",
        # Restriction of allowable values (protects against misprints)
        choices=["chrome", "firefox"],
        # Help message when `pytest -h` is called
        help="Choose browser: chrome or firefox"
    )

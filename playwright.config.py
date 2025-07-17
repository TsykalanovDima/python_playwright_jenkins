import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=BASE_URL,
        help="base URL for the application",
    )

from typing import Generator

import pytest
from flask.testing import FlaskClient

from {{cookiecutter.project_slug}} import api


@pytest.fixture
def graphql_client() -> Generator[FlaskClient, None, None]:
    app = api.app
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

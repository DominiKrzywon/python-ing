import os
from pathlib import Path

import pytest
from playwright.sync_api import Page, Route


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.ing.pl"


@pytest.fixture(autouse=True)
def mock_ing_on_ci(page: Page) -> None:
    if os.environ.get("CI"):
        mock_html = (
            Path(__file__).parent / "fixtures" / "ing-mock.html"
        ).read_text(encoding="utf-8")

        def handle(route: Route) -> None:
            route.fulfill(
                content_type="text/html; charset=utf-8",
                body=mock_html,
            )

        page.route("https://www.ing.pl/**", handle)

from playwright.sync_api import Page, Locator


class CookiePolicyPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.customize_button: Locator = page.locator(
            ".js-cookie-policy-main-settings-button"
        )
        self.analytical_toggle: Locator = page.locator("#header-2-analytical")
        self.accept_selected_button: Locator = page.locator(
            ".js-cookie-policy-settings-decline-button"
        )

    def open(self) -> None:
        self.page.goto("/")

    def open_customize(self) -> None:
        self.customize_button.click()

    def enable_analytical(self) -> None:
        self.analytical_toggle.click()

    def accept_selected(self) -> None:
        self.accept_selected_button.click()

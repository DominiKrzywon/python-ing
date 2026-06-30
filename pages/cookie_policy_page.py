from playwright.sync_api import Page, Locator, expect


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
        expect(self.customize_button).to_be_visible()
        self.customize_button.click()

    def enable_analytical(self) -> None:
        expect(self.analytical_toggle).to_be_visible()
        self.analytical_toggle.click()

    def accept_selected(self) -> None:
        expect(self.accept_selected_button).to_be_visible()
        self.accept_selected_button.click()

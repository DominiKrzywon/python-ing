from playwright.sync_api import Page, BrowserContext, expect

from pages.cookie_policy_page import CookiePolicyPage

ANALYTICAL_BIT = 2


def test_user_enables_analytical_cookies_and_choice_is_persisted(
    page: Page, context: BrowserContext
) -> None:
    cookie_page = CookiePolicyPage(page)

    cookie_page.open()
    
    expect(cookie_page.customize_button).to_be_visible()
    cookie_page.open_customize()

    expect(cookie_page.analytical_toggle).to_be_visible()
    cookie_page.enable_analytical()
    
    expect(cookie_page.accept_selected_button).to_be_visible()
    cookie_page.accept_selected()

    expect(cookie_page.customize_button).to_be_hidden()

    cookies = context.cookies()
    consent_cookie = next(
        (c for c in cookies if c["name"] == "cookiePolicyGDPR"), None
    )
    details_cookie = next(
        (c for c in cookies if c["name"] == "cookiePolicyGDPR__details"), None
    )

    assert consent_cookie is not None, "Expected cookiePolicyGDPR cookie to be saved"
    assert details_cookie is not None, (
        "Expected cookiePolicyGDPR__details cookie to be saved"
    )

    consent_mask = int(consent_cookie["value"])
    assert consent_mask & ANALYTICAL_BIT == ANALYTICAL_BIT, (
        f"Expected analytical consent in cookiePolicyGDPR (mask={consent_mask})"
    )

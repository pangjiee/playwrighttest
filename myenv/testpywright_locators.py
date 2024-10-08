import pytest
from playwright.sync_api import Page, expect, sync_playwright


# @pytest.mark.skip(reason="Skipping test_navigate_to_api")
def test_navigate_to_api(page: Page):
    nav_to_playwright(page)
    # check visible and click
    page.locator('a.navbar__item.navbar__link[href="/docs/api/class-playwright"]').click()
    expect(page).to_have_url("https://playwright.dev/docs/api/class-playwright")


# @pytest.mark.skip(reason="Skipping test_select_python")
def test_select_python(page: Page):
    nav_to_playwright(page)
    select_nav_lang(page, 'python', 2)


# @pytest.mark.skip(reason="Skipping test_select_java")
def test_select_java(page: Page):
    nav_to_playwright(page)
    select_nav_lang(page, 'java', 3)


def test_select_net(page: Page):
    nav_to_playwright(page)
    select_nav_lang(page, 'dotnet', 4)


def test_navigate_to_community(page: Page):
    nav_to_playwright(page)
    page.locator('a.navbar__item.navbar__link.navbar__link--active[href="/community/welcome"]').click()
    expect(page).to_have_url('https://playwright.dev/community/welcome')


def nav_to_playwright(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get Started").click()


def select_nav_lang(page: Page, language: str, index: int):
    page.wait_for_timeout(2000)
    index_selector_xpath = f'//*[@id="__docusaurus"]/nav/div[1]/div[1]/div/ul/li[{index}]/a'
    selected_lang_url = f'https://playwright.dev/{language}/docs/intro'
    page.locator('//*[@id="__docusaurus"]/nav/div[1]/div[1]/div/a').hover()
    page.locator(index_selector_xpath).click()
    expect(page).to_have_url(selected_lang_url)


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    test_navigate_to_api(page)
    test_select_python(page)
    test_select_java(page)
    test_select_net(page)
    test_navigate_to_community(page)
    browser.close()

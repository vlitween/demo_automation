import allure
import pytest


@pytest.mark.parametrize('device', ['chrome'], indirect=True)
class TestHeaderNavigation:

    @pytest.fixture(autouse=True)
    def setup(self, page):
        with allure.step('Open Main page'):
            page.main_page.open_page()

    @allure.title('Top navigation: {button_name}')
    @pytest.mark.smoke
    @pytest.mark.parametrize('button_name, page_attr', [
        ('Downloads', 'downloads_page'),
        ('Documentation', 'documentation_page'),
        ('Projects', 'projects_page'),
        ('Support', 'support_page'),
        ('Blog', 'blog_page')
    ])
    def test_top_navigation(self, device, page, button_name, page_attr):
        header = page.header_component

        with allure.step(f'Click "{button_name}"'):
            method_name = f"click_{button_name.lower()}_button"
            getattr(header, method_name)()
        with allure.step(f'Verify transition to {button_name}'):
            target_page = getattr(page, page_attr)
            target_page.check_page_presence(fast_check=True)

    @allure.title('About dropdown navigation: {button_name}')
    @pytest.mark.parametrize('button_name, page_attr', [
        ('About Selenium', 'about_selenium_page'),
        ('Structure and Governance', 'structure_and_governance_page'),
        ('Events', 'events_page'),
        ('Ecosystem', 'ecosystem_page'),
        ('History', 'history_page'),
        ('Get Involved', 'get_involved_page'),
        ('Sponsors', 'sponsors_page'),
        ('Sponsor Us', 'sponsor_us_page')
    ])
    def test_about_navigation(self, device, page, button_name, page_attr):
        header = page.header_component

        with allure.step('Open About dropdown'):
            header.click_about_button()
        with allure.step(f'Click "{button_name}"'):
            suffix = button_name.lower().replace(' ', '_')
            getattr(header, f"click_{suffix}_button")()
        with allure.step(f'Verify {button_name} presence'):
            getattr(page, page_attr).check_page_presence(fast_check=True)

    @allure.title('Logo navigation')
    def test_logo_navigation(self, device, page):
        header = page.header_component

        with allure.step('Open Documentation page'):
            page.documentation_page.open_page()
        with allure.step('Click header logo'):
            header.click_logo()
        with allure.step('Check presence Main page'):
            page.main_page.check_page_presence(fast_check=True)

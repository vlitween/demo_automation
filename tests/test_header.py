import allure
import pytest


class TestHeader:
    @allure.title('Test header navigation')
    @pytest.mark.parametrize('device', ['chrome'], indirect=True)
    def test_navigation(self, device, page):
        header = page.header_component
        with allure.step('Open Main page'):
            page.main_page.open_page()
        with allure.step('Check presence page header'):
            header.check_presence()
        with allure.step('Click header button "About"'):
            header.click_about_button()
        with allure.step('Check presence About dropdown buttons'):
            header.check_about_dropdown_buttons()
        with allure.step('Click header button "About Selenium"'):
            header.click_about_selenium_button()
        with allure.step('Check transition to About Selenium page'):
            page.about_selenium_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "About"'):
            header.click_about_button()
        with allure.step('Click header button "Structure and Governance"'):
            header.click_structure_and_governance_button()
        with allure.step('Check transition to Structure and Governance page'):
            page.structure_and_governance_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "About"'):
            header.click_about_button()
        with allure.step('Click header button "Events"'):
            header.click_events_button()
        with allure.step('Check transition to Events page'):
            page.events_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "About"'):
            header.click_about_button()
        with allure.step('Click header button "Ecosystem"'):
            header.click_ecosystem_button()
        with allure.step('Check transition to Ecosystem page'):
            page.ecosystem_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "About"'):
            header.click_about_button()
        with allure.step('Click header button "History"'):
            header.click_history_button()
        with allure.step('Check transition to History page'):
            page.history_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "About"'):
            header.click_about_button()
        with allure.step('Click header button "Get Involved"'):
            header.click_get_involved_button()
        with allure.step('Check transition to Get Involved page'):
            page.get_involved_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "About"'):
            header.click_about_button()
        with allure.step('Click header button "Sponsors"'):
            header.click_sponsors_button()
        with allure.step('Check transition to Sponsors page'):
            page.sponsors_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "About"'):
            header.click_about_button()
        with allure.step('Click header button "Sponsor Us"'):
            header.click_sponsor_us_button()
        with allure.step('Check transition to Sponsor Us page'):
            page.sponsor_us_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "Downloads"'):
            header.click_downloads_button()
        with allure.step('Check transition to Downloads page'):
            page.downloads_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "Documentation"'):
            header.click_documentation_button()
        with allure.step('Check transition to Documentation page'):
            page.documentation_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "Projects"'):
            header.click_projects_button()
        with allure.step('Check transition to Projects page'):
            page.projects_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "Support"'):
            header.click_support_button()
        with allure.step('Check transition to Support page'):
            page.support_page.check_page_presence(fast_check=True)
        with allure.step('Click header button "Blog"'):
            header.click_blog_button()
        with allure.step('Check transition to Blog page'):
            page.blog_page.check_page_presence(fast_check=True)
        with allure.step('Click header logo'):
            header.click_logo()
        with allure.step('Check transition to Main page'):
            page.main_page.check_page_presence(fast_check=True)

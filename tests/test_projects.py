import allure
import pytest


class TestProjects:
    @allure.title('Test Projects page')
    @pytest.mark.parametrize('device', ['chrome'], indirect=True)
    def test_positive(self, device, page):
        projects_page = page.projects_page
        with allure.step('Open site'):
            projects_page.actions.open_url(projects_page.url)
        with allure.step('Check Projects page'):
            projects_page.check_projects_page()
